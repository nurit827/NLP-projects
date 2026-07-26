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
