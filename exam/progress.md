# Study progress log

## 2026-07-09 — 02-Markov-LM / language-modeling (subtopic 1/12)
Walked all 10 slides (deck pp. 2–6, 18–22) + taught Zipf's law (orphaned intro-lecture material).
Slide checks: LM formal definition (shaky — gave conditional/masked-LM instead of joint-over-strings; later pushback partly accepted, downgraded to watch-item), entropy floor (solid), prediction→understanding rationale (missed — hadn't absorbed), joint↔conditional formula (solid), no-ground-truth (mostly solid), plausibility>grammaticality (solid), scalar strength/weakness (shaky — circular on strength), corpus-sampling assumption (solid, but reached for "manifold hypothesis" — vocabulary from outside course), trivial-LM zeros (solid).
Exam Q1 capped-uniform-patch [define+prove]: (a) 8/10 notation gaps (Σ over V*, finiteness of U_L support), (b) 10/10, (c) 6/10 vague on "no generalization = probability independent of content".
Exam Q2 Zipf/long-tail [qualitative+link-intro]: (a) missed — stated geometric decay instead of ∝1/r, (b) half — missed |V|^n combinatorial-impossibility contrast.

## 2026-07-09 — 02-Markov-LM / prompt (subtopic 2/12)
Walked 3 slides (deck pp. 15–17). Slide checks: uses-of-LMs + caveat (solid, good n-gram reasoning), what-changes-what-fixed (solid).
Good discussion: prompt-as-π(x)-template vs chaining mechanics, in-band task specification, "conditional not prior".
Exam Q1 prompting-as-reduction [formal define]: 7/10 → resolved to full understanding in discussion (missed π(x) initially, n-gram-specific framing).
Exam Q2 universality↔scalar-bet [link-back, diagnose]: 6.5/10 first pass (missed the risk half — didn't read full question), retry 8/10 (drifted into capability limits vs objective mismatch).

## 2026-07-09 — 02-Markov-LM / unigram-model (subtopic 3/12) — IN PROGRESS
Walked both slides. Slide check: unigram formula + two failure symptoms (solid; forgot STOP in formula — flagged, recurring-deduction risk).
PAUSED before exam questions. RESUME HERE: Q1 already posed = prove unigram-with-STOP normalizes over all finite strings (geometric-series proof); then one link-back question, then subtopics bigram-model onward.

## 2026-07-23 — 02-Markov-LM / unigram-model (subtopic 3/12) — COMPLETED
Exam Q1 unigram-STOP-normalization [prove]: 4/10 first pass — showed each particular infinite sequence has probability 0, which does not establish that the never-stopping event has mass 0; resolved in discussion via the geometric sum over all finite lengths and \(P(\text{no STOP in first }k)=q^k\to0\).
Exam Q2 unseen-sentence-generalization [compare+diagnose+link-back]: 9/10 — correctly contrasted empirical sentence probability 0 with positive unigram probability and diagnosed order invariance; omitted the final STOP factor.

## 2026-07-23 — 02-Markov-LM / bigram-model (subtopic 4/12) — COMPLETED
Walked all 6 slides. Slide checks: first-order Markov assumption (solid), states and transition semantics (solid after one follow-up), sentence path probability (solid), transition-matrix interpretation and row normalization (solid), corpus MLE/count estimator (solid; independently derived it).
Exam Q1 bigram-eventual-STOP [prove+link-unigram]: 9.5/10 — correct squeeze proof using \((1-\varepsilon)^k\); only terminology issue was “inverse” instead of “complement.”
Exam Q2 bigram-free-parameters [count]: 5/10 first pass — counted raw entries \((m+1)^2\) and \(m+1\), missing one normalization constraint per distribution; understood correction to \(m(m+1)\) versus \(m\).

## 2026-07-23 — 02-Markov-LM / markov-assumption (subtopic 5/12) — COMPLETED
Marked complete retroactively because its 4 slides exactly duplicate bigram-model slides 1–4, which were already walked and checked.

## 2026-07-23 — 02-Markov-LM / higher-order-markov-models (subtopic 6/12) — COMPLETED
Walked all 6 slides; slide checks skipped at the user's request. Covered long-distance dependencies, longer-context sparsity, \(k\)-th order factorization, tuple-state conversion, exponential parameter growth, and count-based MLE.
Exam Q1 higher-order-free-parameters [count+diagnose+retest]: missed — needed the answer \(m^{k+1}\) and did not answer why fixed-corpus MLE becomes unreliable; substantial clarification on legal START-padded contexts \(1+m+\cdots+m^k\).
Exam Q2 pair-state-conversion [formal]: 9/10 after clarification — correctly gave \((a,b)\to(b,c)\) with probability \(P(c\mid a,b)\) and understood overlap consistency.
Exam Q3 fixed-context-independence [formal+refute]: incomplete — formal assumption correct; proposed examples did not actually refute it, then understood a distant subject–verb agreement counterexample; skipped why no fixed \(k\) solves arbitrary-distance dependencies.

## 2026-07-23 — 02-Markov-LM / mle (subtopic 7/12) — COMPLETED
Marked complete without a separate walkthrough or exam questions because its 3 slides repeat the bigram transition-matrix MLE and higher-order count-MLE material already covered in subtopics 4 and 6.

## 2026-07-23 — 02-Markov-LM / smoothing (subtopic 8/12) — COMPLETED
Walked all 11 slides; slide checks skipped at the user's request. Covered zero counts, add-\(\delta\), low-count unreliability, absolute discounting, missing mass, lower-order interpolation, and Kneser–Ney continuation probability.
Exam Q1 two-level-discount-normalizer [derive]: solid — derived \(\lambda(h)=[d_1N_1(h)+d_2N_{2+}(h)]/C(h)\) after clarifying that the redistribution term is a normalized distribution, not a count.
Exam Q2 continuation-vs-frequency [compute+diagnose]: 10/10 — correctly computed \(1/20\) versus \(4/20\) and explained why Kneser–Ney and unigram interpolation rank the words oppositely.

## 2026-07-23 — 02-Markov-LM / back-off-models (subtopic 9/12) — COMPLETED
Walked both slides. Covered hard fallback from trigram to bigram to unigram estimates and homogeneous position-independent notation.
Single requested exam Q context-threshold-backoff [apply]: back-off part solid — correctly selected \(P(\mathrm{flooded}\mid\mathrm{river})\) when the longer context was below threshold. The interpolation comparison was withdrawn and left ungraded because the dedicated interpolation subtopic had not yet been studied.

## 2026-07-23 — 02-Markov-LM / linear-interpolation (subtopic 10/12) — COMPLETED
Walked all 4 slides; slide checks skipped at the user's request. Covered convex unigram–bigram–trigram mixtures, held-out likelihood tuning, corpus likelihood grouped by validation counts, and context-frequency-bucket-specific lambda vectors. Added slide 3/4 to `slides-to-review.md`.
Exam Q1 bucketed-mixture-normalization [prove+count+retest]: 10/10 — correctly proved normalization and counted \(BR\) lambda values with \(B(R-1)\) free parameters.
Exam Q2 numeric-backoff-comparison [compute+compare]: skipped at the user's request.

## 2026-07-23 — 02-Markov-LM / generalization-pereiras-solution (subtopic 11/12) — COMPLETED
Walked the 4-slide deck without slide checks. Covered the limitation of count-based generalization, Pereira's latent word categories, marginalization over categories, the conditional-independence assumption, and EM-trained structural generalization. Added slide 3/4 to `slides-to-review.md`.
Exam Q1 latent-category-normalization [prove+independence+generalization]: 9.5/10 — correctly proved normalization, stated \(W_i\perp W_{i-1}\mid C\), and explained positive probability for unseen pairs through shared latent categories.
Exam Q2: skipped at the user's request.

## 2026-07-23 — 02-Markov-LM / perplexity (subtopic 12/12) — COMPLETED
Walked both slides without slide checks. Covered held-out per-token log-likelihood, cross-entropy, perplexity as effective branching factor, the uniform-model baseline, comparability limitations, and extrinsic evaluation.
Exam Q1 four-token-perplexity [compute+interpret]: answer requested directly rather than graded; \(H_2=7/4=1.75\) bits and \(\mathrm{PPL}=2^{7/4}\approx3.36\).
Exam Q2: skipped at the user's request.

## 2026-07-23 — 03-Classification-LogLinear / classification (subtopic 1/7) — COMPLETED
Walked all 4 slides independently, then reviewed the transcript's main emphases: the in-domain train/test assumption, generative joint modeling versus discriminative conditional modeling, cancellation of \(P(x)\) during generative classification, and the fact that a joint determines a conditional but not conversely.
Exam questions: skipped at the user's request to move on.

## 2026-07-23 — 03-Classification-LogLinear / mle (subtopic 2/7) — COMPLETED
Walked both slides and reviewed the transcript. Covered joint likelihood for generative models, conditional likelihood for discriminative models, and MLE as selecting the parameterized model under which the observed training evidence is most probable.
Exam questions: skipped because the user considered the material straightforward.

## 2026-07-23 — 03-Classification-LogLinear / naive-bayes (subtopic 3/7) — COMPLETED
Walked all 6 slides and used the aligned lecture transcript. Covered the generative joint factorization, conditional independence of features given the class, exhaustive label inference, Bernoulli bag-of-words representation, likelihood factorization, closed-form MLE, and smoothing.
Exam Q1 Bernoulli-NB-free-parameters [count+retest]: 6/10 first pass — class-prior count \(K-1\) was correct, but treated \(d\) binary features as outcomes of one categorical distribution; resolved to \(Kd+K-1\) free parameters.
Exam Q2 Bernoulli-add-alpha [derive+link-smoothing]: 9/10 — correctly derived the smoothed presence probability, explained the \(2\alpha\) denominator and avoidance of zero class scores; initially omitted the corresponding absence formula.

## 2026-07-23 — 03-Classification-LogLinear / bag-of-words (subtopic 4/7) — COMPLETED
Slides 1–4 repeat the Naive Bayes material already covered. Walked slide 5 and reviewed the transcript's emphasis on richer, overlapping, and correlated features such as document length, source, layout, local context, syntactic relations, and \(n\)-grams.
Exam questions: skipped because the user considered this short transition subtopic straightforward.

## 2026-07-23 — 03-Classification-LogLinear / discriminative-approach (subtopic 5/7) — COMPLETED
Walked all 6 slides and used the lecture transcript. Covered direct conditional modeling, correlated and overlapping features, task-dependent input representations, label-specific block notation, and linear prediction with \(w^\top\phi(x,y)\).
Exam Q1 block-notation-equivalence [construct+dimensions]: 8/10 — correctly concatenated class-specific weights and activated only the candidate label's feature block, but initially confused block dimension \(d\) with full dimension \(Kd\).
Exam Q2 correlated-feature-dependence [formal+link-NB]: 8.5/10 — understood the implication-based dependence and why discriminative models can use both features; needed a more formal probability statement and the precise distinction that \(P(x\mid y)\) is not modeled.

## 2026-07-23 — 03-Classification-LogLinear / log-linear-models (subtopic 6/7) — COMPLETED
Walked all 12 slides and used the lecture transcript. Covered softmax normalization, conditional log-likelihood, the observed-minus-expected feature gradient and derivation, \(L_2\) regularization and weight decay, SGD versus perceptron updates, and NER as an example task. Added the gradient derivation slide 7/12 to `slides-to-review.md`.
Exam Q1 softmax-score-shift [prove]: 8/10 — correctly recognized cancellation of the common factor but initially gave an informal explanation and referred to the derivative rather than the softmax definition.
Exam Q2: skipped at the user's request.

## 2026-07-23 — 03-Classification-LogLinear / sentiment-analysis (subtopic 7/7) — COMPLETED
Walked all 11 slides and used the lecture transcript. Covered affective-state typology, attitude holder/target/type/span, polarity task variants, aspect and compositional sentiment, binary versus frequency features, sarcasm, thwarted expectations, ordering effects, and the limitations of punctuation-based `NOT_` marking. Added Scherer's typology slide 4/11 to `slides-to-review.md`.
Exam Q1 NOT-scope-and-composition [design+diagnose]: 5/10 — did not apply the stated “until punctuation” transformation and incorrectly suggested that `excellent` would be negated despite following the comma; understood after feedback that contrast and aspect composition remain unresolved.
Exam Q2: skipped when the user chose to wrap up the chapter.

## 2026-07-26 — OFFICIAL EXAM SCOPE UPDATE
The official focus announcement excludes HMM, grammar + dependency parsing, and LLM post-training. Skip `04-HMM/`, grammar topics in `07-Syntax/`, `09-Dependency-Parsing/`, and `12-PostTraining/` for exam preparation. The next in-scope lecture after Classification is `05-MEMM-CRF/`.

## 2026-07-27 — SCOPE CLARIFICATION (WhatsApp)
Four presentations are excluded: `04-HMM/`, `07-Syntax/grammar/`, all of `09-Dependency-Parsing/` (including `graph-based-parsing/`), and `12-PostTraining/`. **Viterbi remains in scope** — question it in MEMM/CRF contexts only, not as HMM/POS material.

## 2026-07-26 — 05-MEMM-CRF / memm — COMPLETED
Walked all 15 slides without slide-level questions. Covered discriminative sequence labeling, history/target notation, sparse label-conditioned features, local log-linear probabilities, sequence conditional likelihood and its gradient, first- and second-order Viterbi inference, grid representation, and label bias. Added slides 3, 4, 8, 9, 10, and 13 to `slides-to-review.md`; scheduled handwritten Viterbi practice and label-bias review before the exam.
Exam Q1 second-order-MEMM-Viterbi [define+derive+justify]: 9/10 — correctly defined the best-prefix state, wrote the recurrence after correcting \(\pi(k-1,t,v)\) to \(\pi(k-1,t,u)\), and precisely justified pruning by the second-order Markov property.
Exam Q2 absorbing-state-label-bias [compute+diagnose+link-log-linear]: 9/10 — correctly computed \(AA=0.3\) and \(BB=0.4\), recognized the absorbing-state advantage and connected repeated subunit factors to probability decay; needed to explicitly name label bias. Correctly explained that local softmax normalization forces the only legal outgoing transition to probability \(1\).

## 2026-07-27 — 05-MEMM-CRF / crf — COMPLETED
Slides 1–3 repeat the completed MEMM label-bias material. Walked slides 4–18 without slide-level questions; skipped the final applications list at the user's request. Covered global sequence normalization, CRF likelihood and observed-minus-expected gradient, edge marginals, forward–backward, efficient computation of \(Z(x)\), the sum-versus-max comparison with Viterbi, CRF inference, POS-tagging results, and domain effects. Added slides 7 and 11 to `slides-to-review.md`.
Single requested exam Q CRF-global-normalization-and-marginals [define+compare+algorithm]: 7.5/10 — correctly described the sequence-score product, label-bias fix, and forward/backward intuition, but omitted \(Z(x)\) and division by it from the formal CRF definition. Also described \(\alpha,\beta\) as probabilities rather than unnormalized path-score sums; the intended edge marginal is \(\alpha_{j-1}(a)M_j(a,b)\beta_j(b)/Z(x)\).

## 2026-07-27 — 06-RNNs / negation-in-sentiment-analysis — COMPLETED
Skipped the two-slide walkthrough because it repeats the previously completed sentiment-analysis discussion of punctuation-bounded `NOT_` marking, scope errors, and compositional limitations.

## 2026-07-27 — 06-RNNs / context-length — COMPLETED
Reviewed the three-slide motivation: fixed-order Markov models discard dependencies outside their last-\(n\)-token window, while increasing order causes exponential context growth. Connected subject–verb agreement and sentiment scope to an RNN's learned continuous state.
Single requested Q ngram-vs-rnn-context [compare+explain]: 8.5/10 — correctly explained fixed context versus recursive access to the full prefix and why this can exceed every fixed \(n\); notation used embeddings recursively instead of \(h_t=R(h_{t-1},e(x_t))\), and initially overstated that the state necessarily preserves all prior information.

## 2026-07-27 — 06-RNNs / rnn — COMPLETED
Walked all 6 slides. Covered the finite-state-automaton analogy, continuous learned history states, the shared recurrent transition \(s_i=R(s_{i-1},x_i)\), Elman recurrence and output softmax, unrolled computation, parameter sharing across sequence positions, recurrent neural language modeling, and empirical-risk training.
Exam questions: skipped at the user's request.

## 2026-07-27 — 06-RNNs / sentiment-analysis-with-rnns — COMPLETED
Walked all 3 slides. Covered bidirectional context, combining forward and backward states at each word, mean pooling of context-aware word outputs, binary log-linear sentence classification, end-to-end training from sentence labels, and the interpretability/computational trade-offs relative to bag-of-words.
Exam questions: skipped at the user's request.

## 2026-07-27 — 06-RNNs / backpropagation-through-time — COMPLETED
Walked all 10 slides, accelerating through repeated loss and per-token teacher-forcing diagrams. Covered next-token cross-entropy, sentence/document chunking versus minibatching, truncated temporal gradient connections, unrolled computation graphs, and summing gradient contributions from every reuse of the shared recurrent weight matrix.
Exam questions: skipped at the user's request.

## 2026-07-27 — 06-RNNs / generalization — COMPLETED
Reviewed the four-slide subtopic at overview level, then skipped the remaining walkthrough at the user's request. Covered neural versus count-based \(n\)-gram LMs, fixed-window feedforward neural LMs, and lexical generalization through learned similar representations (for example, transferring evidence from `cat gets fed` to `dog gets fed`).
Exam questions: skipped at the user's request.

## 2026-07-27 — 06-RNNs / vanishing-and-exploding-gradients — COMPLETED
Reviewed the seven-slide subtopic at overview level, then skipped the remaining walkthrough at the user's request. Covered long chain-rule products through repeated recurrent transitions: factors below one cause exponentially vanishing influence, factors above one can explode, destabilizing optimization and preventing ordinary RNNs from learning long-distance dependencies.
Exam questions: skipped at the user's request.

## 2026-07-27 — 06-RNNs / lstm — COMPLETED
Reviewed the three-slide subtopic at overview level, then skipped the remaining walkthrough at the user's request. Covered LSTM as an architecture designed to preserve memory and gradient flow over longer distances, plus the lecture's subject–verb agreement evidence. The lecturer explicitly did not teach the internal gate equations in depth.
Exam questions: skipped at the user's request.

## 2026-07-27 — 07-Syntax / morphology — COMPLETED
Reviewed the three-slide subtopic at overview level, then skipped the remaining walkthrough at the user's request. Covered morphology as internal word structure, tokenization, lemmatization, morpheme segmentation, and the fact that analysis schemes reflect linguistic and practical conventions rather than a unique correct decomposition.
Exam questions: skipped at the user's request.

## 2026-07-27 — 08-WordEmbeddings / distributional-hypothesis — COMPLETED
Reviewed the single-slide subtopic. Covered the distributional hypothesis and how observable context distributions provide a proxy for semantic similarity from unlabeled text.
Q1 unlabeled-context-signal [explain]: solid after clarification — identified self-supervised learning from proximity, but initially conflated the general hypothesis with its later prediction-based implementation.
Q2 rnn-vs-distributional-signal [compare]: skipped at the user's request.

## 2026-07-27 — 08-WordEmbeddings / count-based-methods — COMPLETED
Walked all 3 slides. Covered word-context co-occurrence vectors, context windows, cosine similarity, gradual semantic similarity versus one-hot identity, and the limitations of raw neighboring-word dimensions.
Q1 define-count-vector [formal definition]: solid — correctly identified each coordinate as a context word and its corpus-wide count within the target's \(K\)-word windows; clarified that this is not the context word's unrestricted corpus frequency.
Q2: skipped at the user's request.

## 2026-07-27 — 08-WordEmbeddings / dimensionality-reduction — COMPLETED
Reviewed both slides as an overview. Covered the excessive concreteness of raw context-word dimensions, latent semantic features produced by dimensionality reduction, and classical approaches such as SVD and the information bottleneck.
Exam questions: skipped at the user's request.

## 2026-07-27 — 08-WordEmbeddings / prediction-based-models — COMPLETED
Reviewed the first two slides, then moved on at the user's request. Covered neighbor prediction as a self-supervised auxiliary task whose compact hidden representation encodes context distributions, and using summed or averaged embeddings as features for supervised document classification.
Slide 3 and exam questions: skipped at the user's request.

## 2026-07-27 — 08-WordEmbeddings / skip-grams — COMPLETED
Reviewed slides 1–2, then moved on at the user's request. Covered skip-gram notation, the one-hot input selecting an input embedding from \(W\), the separate output embeddings in \(W'\), and the softmax neighbor distribution. Clarified that skip-gram resembles an encoder bottleneck but predicts context rather than reconstructing its input, and that its name reflects predicting words across a context window while skipping intervening words.
One formal question was requested but answered as a worked explanation rather than attempted by the user. Slides 3–4 and further questions were skipped.

## 2026-07-27 — 10-Machine-Translation / ambiguity-resolution — COMPLETED
Reviewed the single slide. Covered translation as implicit syntactic and semantic disambiguation rather than dictionary-based word replacement.
Q1 dictionary-ambiguity-failure [diagnose+example]: skipped at the user's request; Q2 skipped.

## 2026-07-27 — 10-Machine-Translation / linguistic-differences — COMPLETED
Reviewed slide 1, then moved on at the user's request. Covered systematic cross-language differences in word order, adposition placement, and pro-drop, emphasizing that translation must infer and transform grammatical information rather than only replace words.
Slides 2–4 and exam questions: skipped at the user's request.

## 2026-07-27 — 10-Machine-Translation / lexical-gaps — COMPLETED
Reviewed slide 1, then moved on at the user's request. Covered lexical gaps: concepts lexicalized as one word in one language may require a phrase or explanation in another, preventing one-to-one dictionary substitution.
Slide 2 and exam questions: skipped at the user's request.

## 2026-07-27 — 10-Machine-Translation / vauquois-triangle — COMPLETED
Reviewed the single slide. Covered direct translation, syntactic transfer, semantic transfer, and interlingua as progressively more abstract translation architectures, along with the greater analytical difficulty and narrow-domain practicality of interlingua.
Exam questions: skipped at the user's request.

## 2026-07-27 — 10-Machine-Translation / direct-transfer — COMPLETED
Walked both slides. Covered the classical morphological-analysis → lexical-transfer → reordering → morphological-generation pipeline, and syntactic transfer rules that transform phrase structures to handle substantial cross-language word-order differences.
Exam questions: skipped at the user's request.

## 2026-07-27 — 10-Machine-Translation / statistical-mt-methods — COMPLETED
Reviewed slide 1, then moved on at the user's request. Covered learning translation correspondences from aligned bilingual parallel corpora rather than manually crafting low-coverage rules.
Slides 2–4 and exam questions: skipped at the user's request.

## 2026-07-27 — 10-Machine-Translation / neural-mt — COMPLETED
Walked all 8 slides. Covered encoder–decoder conditional language modeling, the fixed-vector bottleneck, RNN attention as dynamic soft alignment over per-token encoder states, teacher forcing, greedy and beam-search decoding, and exposure bias. Added greedy versus beam search to `pre-exam-review.md`.
Q1 nmt-factorization-and-exposure-bias [formal definition+diagnose]: provided as a worked model answer at the user's request rather than attempted. Q2 skipped.

## 2026-07-28 — 10-Machine-Translation / attention-transformers — COMPLETED
Walked all 21 slides. Covered the transition from RNN attention to self-attention, contextual token representations, query/key/value projections, scaled dot-product attention, residual connections, multi-head attention, stacked encoder/decoder blocks, cross-attention, causal masking, positional embeddings, training/decoding, computational dimensions, and advantages over RNNs. Corrected two imprecise slide statements: standard cross-attention uses decoder \(Q\) and encoder \(K,V\), and standard positional information is added rather than concatenated.
Q1 transformer-qkv-sources [define+explain]: 7/10 — correctly described scaled attention and masking, but initially treated attention output as a next-token prediction and said cross-attention's query came from the decoded next token rather than the target prefix.
Q2 rnn-vs-transformer [compare+complexity]: 9/10 — correctly covered path length, token-level parallelization, positional encoding, parameter sharing, and \(O(n)\) recurrent versus \(O(n^2)\) attention sequence cost; slightly overstated that RNNs cannot parallelize anything and described \(QK^\top\), rather than the weighted values, as the direct information path.

## 2026-07-28 — 10-Machine-Translation / mt-evaluation — COMPLETED
Reviewed the evaluation overview. Covered human judgment as the gold standard, its cost and inconsistency, automatic reference-based evaluation as a reusable proxy, and BLEU's limited correlation with human judgments. Moved to the dedicated BLEU subtopic for the detailed metric.
Exam questions: deferred to the BLEU subtopic.

## 2026-07-28 — 10-Machine-Translation / bleu-score — COMPLETED
Reviewed the full metric, accelerating through the initial worked overlap examples. Covered clipped modified \(n\)-gram precision, the geometric mean across orders, brevity penalty, the final BLEU formula, and the distinction between corpus-level MT-system ranking and unreliable sentence-level or human-versus-machine quality judgment.
Q1 formal-BLEU-definition [define+justify]: provided as a worked model answer at the user's request.
Q2 bleu-paraphrase-failure [diagnose+reconcile]: 9/10 — correctly explained that surface overlap can favor literal machine output over fluent semantic paraphrases and that reported correlation is an aggregate tendency, not a guarantee; used “repetition” where “clipped overlap with references” would be more precise.

## 2026-07-28 — 11-Pretraining-ContextualizedEmb / contextualized-word-embeddings — COMPLETED
Reviewed slides 1–4, then moved on at the user's request. Covered limitations of static word2vec embeddings, contextual representations induced by ordered language modeling, and self-supervised prediction as a pressure to encode structure and word sense from unlabeled text.
Slide 5 and exam questions: skipped at the user's request.

## 2026-07-28 — 11-Pretraining-ContextualizedEmb / pretraining — COMPLETED
Walked all 3 slides. Covered self-supervised language-model pretraining, parameter transfer as initialization, supervised fine-tuning, replacing the vocabulary head with a task-specific classification head, and updating the pretrained feature-producing body.
Q1 why-pretraining-transfers [explain]: 9/10 — correctly identified reusable contextual and semantic representations; needed to state explicitly that the body is reused while the output head is replaced.
Q2 frozen-word2vec-vs-finetuned-lm [compare]: 7/10 — correctly explained the contextual and task-adaptive advantages of a fine-tuned LM, but incorrectly said frozen word2vec is trained by the supervised downstream signal rather than self-supervised neighbor prediction.

## 2026-07-28 — 11-Pretraining-ContextualizedEmb / bert — COMPLETED
Walked all 11 slides. Covered BERT as an encoder-only bidirectional Transformer, masked-language-model pretraining, 15% token selection and 80/10/10 corruption, selected-position cross-entropy, fine-tuning for token and sentence classification, NSP, `[CLS]`/`[SEP]`, and BERT's broad impact.
Q1 bert-mlm-procedure [formal definition]: 8/10 — correctly described random selection, corruption proportions, and independent per-position vocabulary distributions, but initially described random/unchanged cases as binary correctness judgments and called the target the next word rather than the original selected token.
Q2 bert-vs-autoregressive [compare]: 8.5/10 — correctly distinguished bidirectional from causal context, independent mask reconstruction from left-to-right generation, and understanding versus generation use cases; downstream-task characterization was somewhat vague and autoregressive models can also support classification.

## 2026-07-28 — 11-Pretraining-ContextualizedEmb / fine-tuning — COMPLETED
Skipped repeated slides 1–9 after summarizing the role of fine-tuning, then covered decoder-only sentence classification using the final appended token's hidden state. Clarified that BERT contextualizes an input `[CLS]` token rather than predicting it, and that decoder-only classification uses a hidden representation rather than a predicted vocabulary token.
Q1 encoder-vs-decoder-sentence-representation [compare]: 5.5/10 initially — conflated `[CLS]` with a predicted NSP token and the decoder's final hidden state with its next-token prediction; corrected through follow-up discussion.
Q2 fine-tuning-head-and-overfitting [explain+diagnose]: 8.5/10 — correctly connected a small head to scarce labeled data and overfitting, and explained adaptation of pretrained features; slightly conflated full fine-tuning with parameter-efficient partial unfreezing.

## 2026-07-28 — 11-Pretraining-ContextualizedEmb / decoder-only-models — COMPLETED
Walked all 3 slides. Covered GPT-style causal language modeling, removal of the encoder and cross-attention, decoder-only sentence classification from a final appended token, complete-string probability factorization, and trade-offs against bidirectional masked LMs.
Q1 prompted-decoder-translation [explain+compare]: 7.5/10 — correctly described concatenating the source prompt and generated translation into one autoregressive prefix; proposed shared vocabulary as the main disadvantage rather than the more central loss of bidirectional source encoding and cross-attention.
Q2: skipped at the user's request.

## 2026-07-28 — 11-Pretraining-ContextualizedEmb / zero-shot-few-shot — COMPLETED
Walked all 7 slides. Covered direct zero-shot decoding from MLMs, scaling toward very large language models, prompts as task-formulating prefixes, question answering and summarization as completion, few-shot demonstrations, and in-context learning without parameter updates.
Exam questions: skipped at the user's request.

## 2026-07-28 — 11-Pretraining-ContextualizedEmb / lm-evaluation — COMPLETED
Walked all 11 slides. Covered precision/recall framing, the difficulty of open-ended recall, multiple-choice evaluation, benchmark suites, embedding-based reference metrics and BERTScore-style precision/recall, and pairwise, scalar, and multi-dimensional LLM-as-judge evaluation with circularity and bias limitations.
Exam questions: skipped at the user's request.

## 2026-07-28 — 13-Tokenization / character-level-tokenization — COMPLETED
Reviewed the single slide. Covered the small-vocabulary and no-OOV benefits of character tokens, alongside longer sequences, higher attention cost, and the need to learn word composition from scratch.
Exam questions: skipped while continuing directly to the next slide/subtopic.

## 2026-07-28 — 13-Tokenization / subword-tokenization — COMPLETED
Walked all 3 slides. Covered subwords as a compromise between word and character tokens, byte-level fallback with statistical merges, vocabulary/sequence-length trade-offs, and the distinctions among BPE, WordPiece, and SentencePiece.
Exam questions: skipped at the user's request.

## 2026-07-28 — 13-Tokenization / bpe — COMPLETED
Reviewed the BPE algorithm and the first worked merge, then moved on at the user's request. Covered additive vocabulary construction from bytes/characters, frequency-weighted adjacent-pair counting, retaining component tokens as fallback, and repeated merging until a target vocabulary size.
Remaining worked iterations and exam questions: skipped.

## 2026-07-28 — 13-Tokenization / morphology-aware-tokenization — COMPLETED
Walked all 3 slides. Covered morphological pre-segmentation followed by statistical subword learning, restricting merge statistics to remain within morpheme boundaries, and benefits for Arabic and Hebrew. Corrected the misconception that morphology-aware BPE starts from whole morphemes and merges across their boundaries.
Exam questions: skipped while moving directly to the next topic.

## 2026-07-28 — 14-Semantics / information-extraction — COMPLETED
Walked all 7 slides. Covered structured extraction from text, closed binary relation classification over NER-marked ordered entity pairs, large-scale precision-oriented evaluation, OpenIE surface triples, and relation-boundary, normalization, and granularity limitations. Marked detailed dependency-path interpretation as excluded parsing material while retaining the semantic takeaway.
Exam questions: skipped at the user's request.

## 2026-07-28 — 14-Semantics / named-entity-recognition — COMPLETED
Reviewed the single slide. Covered NER as identifying entity mention boundaries and types that provide the building blocks for later information-extraction stages.
Exam questions: skipped while continuing directly.

## 2026-07-28 — 14-Semantics / co-reference-resolution — COMPLETED
Reviewed the single slide. Covered clustering names, descriptions, and pronouns into equivalence classes referring to the same real-world entity, and distinguished this semantic/document-level task from dependency parsing.
Exam questions: skipped while continuing directly.

## 2026-07-28 — 14-Semantics / relation-extraction — COMPLETED
Walked all 11 slides. Covered ontology-based semantic relation inventories, formal structures of entities/classes/relations, domain ontologies and Wikidata, hand-written and learned lexical patterns, NER-type constraints, neural closed-set classification, and precision-oriented evaluation. Treated syntactic phrase-boundary motivation at a high level while excluding parsing mechanics.
Exam questions: skipped while continuing directly.

## 2026-07-28 — 14-Semantics / distant-supervision — COMPLETED
Walked all 5 slides, noting that the path-feature slides were not covered in lecture and overlap excluded parsing material. Covered converting knowledge-base relation tuples and entity co-mentions into noisy labeled examples, recurring textual features, classifier training, and the central false-label problem when co-mention sentences express other relations.
Both exam questions were skipped at the user's request.

## 2026-07-28 — 14-Semantics / path-features — SKIPPED
The two slides were not covered in the lecture, and their detailed graph/dependency-path mechanics overlap excluded dependency-parsing material.

## 2026-07-28 — 14-Semantics / srl — COMPLETED (LOW PRIORITY)
Reviewed all 3 slides at a high level. Covered SRL as predicate/event representation with participant and adjunct roles, and FrameNet as frame-specific semantic-role inventories. The only slide discussed in Omri's lecture was the repeated OpenIE/syntactic-path motivation; the actual SRL and FrameNet slides were not taught.
Exam questions: skipped.
