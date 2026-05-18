"""HMM POS tagger module for NLP Exercise 3, Question 3."""

import math
from collections import Counter, defaultdict
import nltk


START = "*"
STOP = "STOP"
NEG_INF = float("-inf")


def _simplify_tag(tag: str) -> str:
    """Take prefix of tag before first '+' or '-'."""
    for sep in ('+', '-'):
        if sep in tag:
            tag = tag.split(sep, 1)[0]
    return tag


def load_brown_news(test_fraction: float = 0.1):
    """Load Brown 'news' tagged sentences, simplify tags, split last 10% as test."""
    nltk.download('brown', quiet=True)
    sents = list(nltk.corpus.brown.tagged_sents(categories='news'))
    sents = [[(w, _simplify_tag(t)) for (w, t) in s] for s in sents]
    split = int(len(sents) * (1 - test_fraction))
    return sents[:split], sents[split:]


def train_most_likely_tag(train_sents):
    """Return dict: word -> most frequent tag for that word in training."""
    counts = defaultdict(Counter)
    for sent in train_sents:
        for w, t in sent:
            counts[w][t] += 1
    return {w: c.most_common(1)[0][0] for w, c in counts.items()}


def evaluate_baseline(word_to_tag, test_sents, unk_tag="NN"):
    """Return (total_err, known_err, unknown_err) on test_sents."""
    known_total = known_correct = 0
    unk_total = unk_correct = 0
    for sent in test_sents:
        for w, true_tag in sent:
            if w in word_to_tag:
                pred = word_to_tag[w]
                known_total += 1
                known_correct += (pred == true_tag)
            else:
                pred = unk_tag
                unk_total += 1
                unk_correct += (pred == true_tag)
    total = known_total + unk_total
    correct = known_correct + unk_correct
    return (
        1 - correct / total,
        1 - known_correct / known_total if known_total else 0.0,
        1 - unk_correct / unk_total if unk_total else 0.0,
    )


def train_bigram_hmm(train_sents):
    """
    MLE bigram HMM. Returns:
      q: dict[(prev_tag, tag)] -> probability
      tags: set of tags seen in training
      vocab: set of words seen in training
      word_tag_counts: Counter[(word, tag)] -> int
      emit_tag_counts: Counter[tag] -> int
    """
    tag_counts = Counter()
    bigram_counts = Counter()
    word_tag_counts = Counter()
    emit_tag_counts = Counter()
    tags = set()
    vocab = set()

    for sent in train_sents:
        prev = START
        for w, t in sent:
            tag_counts[prev] += 1
            bigram_counts[(prev, t)] += 1
            word_tag_counts[(w, t)] += 1
            emit_tag_counts[t] += 1
            tags.add(t)
            vocab.add(w)
            prev = t
        tag_counts[prev] += 1
        bigram_counts[(prev, STOP)] += 1

    q = {(p, t): c / tag_counts[p] for (p, t), c in bigram_counts.items()}

    return q, tags, vocab, word_tag_counts, emit_tag_counts


def make_mle_emission(word_tag_counts, emit_tag_counts):
    """Return e_fn(word, tag) using pure MLE. Returns 0 for unseen pairs."""
    def e_fn(word, tag):
        c_wt = word_tag_counts.get((word, tag), 0)
        c_t = emit_tag_counts.get(tag, 0)
        if c_t == 0:
            return 0.0
        return c_wt / c_t
    return e_fn


def make_addone_emission(word_tag_counts, emit_tag_counts, vocab):
    """Return e_fn(word, tag) using Add-one (Laplace) smoothing."""
    V = len(vocab)
    def e_fn(word, tag):
        c_wt = word_tag_counts.get((word, tag), 0)
        c_t = emit_tag_counts.get(tag, 0)
        return (c_wt + 1) / (c_t + V)
    return e_fn


def viterbi_bigram(words, q, e_fn, tags, vocab, force_unk_tag=None):
    """
    Run Viterbi on a single sentence (list of words).
    Returns predicted list of tags (same length as words).
    Works in log space.

    e_fn(word, tag) -> probability (must handle unseen pairs gracefully).
    If force_unk_tag is given, unknown words (not in vocab) are pinned to it.
    Otherwise unknown words use e_fn like any other word.
    """
    tags = list(tags)
    n = len(words)
    if n == 0:
        return []

    pi = [dict() for _ in range(n)]
    bp = [dict() for _ in range(n)]

    def log_q(prev, curr):
        p = q.get((prev, curr), 0.0)
        return math.log(p) if p > 0 else NEG_INF

    def log_e(word, tag):
        if force_unk_tag is not None and word not in vocab:
            return 0.0
        p = e_fn(word, tag)
        return math.log(p) if p > 0 else NEG_INF

    def candidates(word):
        if force_unk_tag is not None and word not in vocab:
            return [force_unk_tag]
        return tags

    for v in candidates(words[0]):
        pi[0][v] = log_q(START, v) + log_e(words[0], v)
        bp[0][v] = None

    for k in range(1, n):
        for v in candidates(words[k]):
            best_score, best_prev = NEG_INF, next(iter(pi[k-1]))
            for u, prev_score in pi[k-1].items():
                s = prev_score + log_q(u, v) + log_e(words[k], v)
                if s > best_score:
                    best_score, best_prev = s, u
            pi[k][v] = best_score
            bp[k][v] = best_prev

    best_score, best_last = NEG_INF, next(iter(pi[n-1]))
    for v, score in pi[n-1].items():
        s = score + log_q(v, STOP)
        if s > best_score:
            best_score, best_last = s, v

    out = [None] * n
    out[n-1] = best_last
    for k in range(n-1, 0, -1):
        out[k-1] = bp[k][out[k]]
    return out


def evaluate_tagger(predict_fn, test_sents, vocab):
    """Evaluate any tagger that maps a list of words -> list of tags."""
    known_total = known_correct = 0
    unk_total = unk_correct = 0
    for sent in test_sents:
        words = [w for w, _ in sent]
        gold = [t for _, t in sent]
        pred = predict_fn(words)
        for w, g, p in zip(words, gold, pred):
            if w in vocab:
                known_total += 1
                known_correct += (p == g)
            else:
                unk_total += 1
                unk_correct += (p == g)
    total = known_total + unk_total
    correct = known_correct + unk_correct
    return (
        1 - correct / total,
        1 - known_correct / known_total if known_total else 0.0,
        1 - unk_correct / unk_total if unk_total else 0.0,
    )


def word_counts_from_sents(sents):
    """Return Counter of word counts."""
    c = Counter()
    for sent in sents:
        for w, _ in sent:
            c[w] += 1
    return c


def diagnose_rare_and_unknown(train_sents, test_sents, low_freq_threshold=5, sample_size=40):
    """
    Return a dict with diagnostic info about low-frequency training words
    and unknown test words, to help design pseudo-word categories.
    """
    train_counts = word_counts_from_sents(train_sents)
    train_vocab = set(train_counts)

    low_freq_words = [w for w, c in train_counts.items() if c < low_freq_threshold]

    unknown_test_words = set()
    for sent in test_sents:
        for w, _ in sent:
            if w not in train_vocab:
                unknown_test_words.add(w)

    return {
        "num_low_freq": len(low_freq_words),
        "low_freq_sample": sorted(low_freq_words)[:sample_size],
        "num_unknown_test": len(unknown_test_words),
        "unknown_test_sample": sorted(unknown_test_words)[:sample_size],
        "low_freq_threshold": low_freq_threshold,
    }


def pseudo_word(w: str) -> str:
    """Map a word to its pseudo-word category based on surface features."""
    if w.startswith('$'):
        return 'dollarAmount'
    has_digit = any(c.isdigit() for c in w)
    if has_digit and ':' in w:
        return 'containsDigitAndColon'
    is_digits_punct = all(c.isdigit() or c in ',.-' for c in w) and len(w) > 0
    if has_digit and ',' in w and is_digits_punct:
        return 'containsDigitAndComma'
    if has_digit and '.' in w and is_digits_punct:
        return 'containsDigitAndPeriod'
    if has_digit and any(c.isalpha() for c in w):
        return 'containsDigitAndAlpha'
    if has_digit and '-' in w and is_digits_punct:
        return 'containsDigitAndDash'
    if w.isdigit():
        if len(w) == 2:
            return 'twoDigitNum'
        if len(w) == 4:
            return 'fourDigitNum'
        return 'otherNum'
    if len(w) == 2 and w[0].isupper() and w[1] == '.':
        return 'capPeriod'
    if w.isalpha():
        if w.isupper():
            return 'allCaps'
        if w[0].isupper() and w[1:].islower():
            return 'initCap'
        if w.islower():
            return 'lowercase'
    return 'other'


def apply_pseudo_words_to_training(train_sents, threshold=5):
    """
    Replace low-frequency words in training sentences by their pseudo-word.
    Returns (new_sents, new_vocab) where new_vocab is the set of tokens
    appearing in new_sents (both kept words and pseudo-word labels).
    """
    counts = word_counts_from_sents(train_sents)
    keep = {w for w, c in counts.items() if c >= threshold}
    new_sents = [
        [(w if w in keep else pseudo_word(w), t) for w, t in sent]
        for sent in train_sents
    ]
    new_vocab = set()
    for sent in new_sents:
        for w, _ in sent:
            new_vocab.add(w)
    return new_sents, new_vocab


def apply_pseudo_words_to_test(test_sents, train_vocab):
    """
    Replace test-set words not in train_vocab by their pseudo-word.
    Returns the transformed sentences.
    """
    return [
        [(w if w in train_vocab else pseudo_word(w), t) for w, t in sent]
        for sent in test_sents
    ]


def build_confusion_matrix(predict_fn, test_sents):
    """Return Counter[(true_tag, pred_tag)] -> int over all test tokens."""
    cm = Counter()
    for sent in test_sents:
        words = [w for w, _ in sent]
        gold = [t for _, t in sent]
        pred = predict_fn(words)
        for g, p in zip(gold, pred):
            cm[(g, p)] += 1
    return cm
