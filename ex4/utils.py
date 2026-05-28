import random
from collections import defaultdict

import nltk
from nltk.corpus import dependency_treebank

from chu_liu_edmonds import cle_min


def load_data():
    nltk.download('dependency_treebank', quiet=True)
    sentences = dependency_treebank.parsed_sents()
    split = int(len(sentences) * 0.9)
    train = sentences[:split]
    test = sentences[split:]
    return train, test


feature_index = {}

def get_index(key):
    if key not in feature_index:
        feature_index[key] = len(feature_index)
    return feature_index[key]

def feature_function(u, v):
    u_word = u['word'] if u['address'] != 0 else 'ROOT'
    u_tag  = u['tag']  if u['address'] != 0 else 'ROOT'
    v_word = v['word']
    v_tag  = v['tag']
    word_key = ('W', u_word, v_word)
    pos_key  = ('P', u_tag, v_tag)
    return [get_index(word_key), get_index(pos_key)]


def edge_features(g, edges):
    feats = defaultdict(int)
    for u_addr, v_addr in edges:
        for idx in feature_function(g.nodes[u_addr], g.nodes[v_addr]):
            feats[idx] += 1
    return feats


def gold_edge_features(g):
    edges = [(node['head'], addr)
             for addr, node in g.nodes.items() if addr != 0]
    return edge_features(g, edges)


def infer(g, weights):
    n = len(g.nodes)  # includes ROOT at 0
    scores = {}
    for u_addr in range(n):
        for v_addr in range(1, n):  # v is never ROOT
            if u_addr == v_addr:
                continue
            u, v = g.nodes[u_addr], g.nodes[v_addr]
            score = sum(weights.get(idx, 0.0) for idx in feature_function(u, v))
            scores[(u_addr, v_addr)] = -score  # negate for min arborescence
    tree = cle_min(scores, n)  # {child: parent}
    return [(parent, child) for child, parent in tree.items()]


def train(train_sents, n_iterations=2, lr=1.0):
    weights = defaultdict(float)
    weights_sum = defaultdict(float)
    total_steps = 0

    for _ in range(n_iterations):
        order = list(range(len(train_sents)))
        random.shuffle(order)
        for i in order:
            g = train_sents[i]

            pred_edges = infer(g, weights)
            pred_feats = edge_features(g, pred_edges)
            gold_feats = gold_edge_features(g)

            for idx in set(gold_feats) | set(pred_feats):
                weights[idx] += lr * (gold_feats[idx] - pred_feats[idx])

            for idx, val in weights.items():
                weights_sum[idx] += val
            total_steps += 1

    avg_weights = {idx: s / total_steps for idx, s in weights_sum.items()}
    return avg_weights, dict(weights)


def compute_uas(test_sents, weights):
    correct = total = 0
    for g in test_sents:
        pred = {child: parent for parent, child in infer(g, weights)}
        for addr, node in g.nodes.items():
            if addr == 0:
                continue
            if pred.get(addr) == node['head']:
                correct += 1
            total += 1
    return correct / total


## Part 2 — Attention-Based Parsing


def attn_to_arc_scores(attn_matrix):
    n = attn_matrix.shape[0] - 1  # number of words (excluding ROOT)
    scores = {}
    for u in range(n + 1):
        for v in range(1, n + 1):  # v is never ROOT
            if u == v:
                continue
            scores[(u, v)] = -float(attn_matrix[u, v])  # negate for cle_min
    return scores


def compute_uas_attn(test_sents, tokenizer, model, layer):
    from transformer_parser_utils import get_attention_matrix
    correct = total = 0
    for g in test_sents:
        words = [g.nodes[i]['word'] for i in range(1, len(g.nodes))]
        attn_matrix = get_attention_matrix(words, tokenizer, model, layer=layer, head_mode="mean")
        scores = attn_to_arc_scores(attn_matrix)
        tree = cle_min(scores, len(g.nodes))  # {child: parent}
        for addr, node in g.nodes.items():
            if addr == 0:
                continue
            if tree.get(addr) == node['head']:
                correct += 1
            total += 1
    return correct / total
