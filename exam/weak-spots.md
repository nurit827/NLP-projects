# Weak spots — spaced repetition queue

- 2026-07-09 | markov/language-modeling | Zipf's law exact form: said "each rank half the previous" (geometric); correct is freq ∝ 1/r, slow decay ⇒ heavy tail | zipf-form
- 2026-07-09 | markov/language-modeling | Sentence-level sparsity argument: missed |V|^n combinatorial explosion vs word-level slow coverage | sentence-sparsity
- 2026-07-09 | markov/language-modeling | "Why prediction ⇒ pushes toward understanding" rationale (Omri's proxy argument) | prediction-understanding
- 2026-07-09 | markov/language-modeling | Strength of scalar LM view: answered circularly; wanted "one concrete universal density-estimation problem, all text = training data" | scalar-strength
- 2026-07-09 (watch-item) | markov/language-modeling | "Define LM formally": defaults to conditional view, skips joint-over-V* + STOP normalization subtlety | lm-formal-def
- 2026-07-09 | markov/prompt | Reads questions partially — missed the explicit "and the risk" half of a two-part question | read-full-question
- 2026-07-09 (watch-item) | markov/prompt | Conflates capability limits (context window, attention) with objective mismatch (likelihood ≠ task success) | objective-vs-capability
- 2026-07-23 | markov/unigram-model | Normalization over finite strings: showing each fixed infinite sequence has probability 0 is insufficient; sum mass over finite lengths or bound the never-stopping event | unigram-finite-normalization
- 2026-07-23 (watch-item) | markov/unigram-model | Recurring omission of the final \(p(\mathrm{STOP})\) factor in sentence-probability formulas | unigram-STOP-factor
- 2026-07-23 | markov/bigram-model | Free parameters vs raw table entries: subtract one normalization constraint for every categorical-distribution row | bigram-free-parameters
- 2026-07-23 | markov/higher-order | Parameter counting with boundaries: legal START-padded contexts are \(1+m+\cdots+m^k\), while the boundary-free question has \(m^k\) contexts; multiply by \(m\) free next-token parameters | higher-order-free-parameters
- 2026-07-23 | markov/higher-order | Refuting fixed-context independence: example must hold the last \(k\) tokens fixed while a more distant token changes the correct prediction; also explain why dependencies can exceed every fixed \(k\) | fixed-k-counterexample
- 2026-07-23 | classification/naive-bayes | Bernoulli NB parameter counting: \(d\) features are \(d\) separate binary distributions per class, not \(d\) outcomes of one categorical distribution; total \(Kd+K-1\) free parameters | bernoulli-nb-parameters
- 2026-07-23 (watch-item) | classification/discriminative | Block notation dimensions: each class block has dimension \(d\); concatenating \(K\) blocks gives global \(w,\phi(x,y)\in\mathbb{R}^{Kd}\) | block-notation-dimensions
- 2026-07-23 | classification/sentiment | `NOT_` scope and composition: punctuation-based marking stops at the comma, so later `excellent` is not negated; bag-of-words still cannot resolve contrast, aspect weighting, or overall composition | sentiment-negation-scope
