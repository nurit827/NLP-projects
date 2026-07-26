# Pre-exam review — read right before the exam

Short notes worth rereading the day before. Add to this file during study sessions.

## Zipf's law & the long-tail / sparsity problem (intro lecture, orphaned — no deck)

- Zipf: frequency of the r-th most frequent word ∝ 1/r. Few words dominate; enormous long tail of rare words; in any corpus a large share of word types appear once (hapax) or never.
- Growing the corpus does NOT close the tail — new unseen words keep arriving at a steady rate. Word-level sparsity is intrinsic.
- Sequences make it combinatorially hopeless: possible n-grams/sentences grow like |V|^n, so "collect more data" can never fix the trivial (empirical) LM.
- This is THE argument motivating structural assumptions: Markov independence + smoothing (share statistical strength instead of demanding coverage).
- Connects to: trivial LM gives P=0 to any unseen sentence; smoothing redistributes mass to the tail; Pereira's answer to Chomsky's "colorless green ideas" (a good model must assign sensible probability to never-seen-but-plausible strings).

## Correlated features: Naive Bayes vs discriminative models

- Let \(x_1\) indicate that `election` appears and \(x_2\) indicate that `win the election` appears. Since \(x_2=1\Rightarrow x_1=1\), the features are dependent even after conditioning on a class in the general case.
- Formally, \(P(x_1=1,x_2=1\mid y)=P(x_2=1\mid y)\), whereas Naive Bayes assumes this equals \(P(x_1=1\mid y)P(x_2=1\mid y)\). These are equal only in special cases.
- A discriminative linear model can still include both features because it models a score or \(P(y\mid x)\), not a factorized generative distribution \(P(x\mid y)\). It treats \(x\) as given and learns a separate weight for each feature.
