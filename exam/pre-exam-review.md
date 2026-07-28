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

## Viterbi practice — do 1–2 days before the exam

- Write the recurrence and work through a small sequence by hand.
- Keep the best prefix for **each** possible ending Markov state, not only the globally best prefix.
- This pruning is valid because prefixes ending in the same state receive identical future factors. In a second-order MEMM, the state is the final tag pair.

## MEMM label bias

- MEMMs normalize outgoing transitions separately at every state.
- A state with one possible exit must assign it probability \(1\); more generally, states with few or low-entropy exits can unfairly preserve probability mass.
- Therefore, Viterbi may favor entering such a state despite weak evidence. The path is highly probable under the MEMM, but the local normalization has artificially inflated it.

## Forward–backward versus Viterbi

- Both use the same trellis dynamic-programming structure.
- Viterbi uses \(\max_u\delta_{i-1}(u)M_i(u,v)\) to retain the best path.
- Forward uses \(\sum_u\alpha_{i-1}(u)M_i(u,v)\) to sum all paths; backward performs the analogous computation from the end.
- Consequently, Viterbi supports MAP decoding, while forward–backward supports \(Z(x)\) and edge-marginal computation.

## Greedy decoding versus beam search

- Autoregressive decoding extends a target prefix one token at a time using \(P(y_t\mid y_{<t},x)\).
- Greedy decoding retains only the locally best extension; it is beam search with \(b=1\).
- Beam search expands the surviving prefixes, scores extensions by cumulative sequence probability (usually summed log-probabilities), and retains the best \(b\).
- It is approximate: pruning can discard a prefix that would eventually produce the globally best complete sequence.
