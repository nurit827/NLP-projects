# Lecture 02 — Markov Language Models

Study summary based on the lecture slides and our sessions on 2026-07-09 and 2026-07-23.

## 1. Language models

A language model is a normalized probability distribution over all finite token sequences:

\[
P:V^*\rightarrow[0,1],
\qquad
\sum_{x\in V^*}P(x)=1.
\]

Using the chain rule:

\[
P(w_1,\ldots,w_n)
=
\left(\prod_{i=1}^{n}P(w_i\mid w_1,\ldots,w_{i-1})\right)
P(\mathrm{STOP}\mid w_1,\ldots,w_n).
\]

Important ideas:

- An LM measures plausibility, not merely grammaticality.
- A single scalar probability makes every text sequence part of one density-estimation problem.
- Predicting the next token can push a model toward learning linguistic and world regularities, but likelihood is still only a proxy for understanding or task success.
- Training corpora are treated as samples from an unknown text distribution; domain shift weakens this assumption.
- Zipf's law is approximately \(f(r)\propto 1/r\), producing a heavy tail of rare words.

## 2. Prompting

A prompt can be viewed as a transformation \(\pi(x)\) that turns an input \(x\) into a text prefix specifying a task. Generation then uses the LM conditionally:

\[
P(y\mid \pi(x)).
\]

The task description is carried in-band as text. Prompting does not change the model parameters; it changes the conditioning context. A recurring distinction is:

- **Capability limitation:** the model cannot represent or access what is needed.
- **Objective mismatch:** likelihood of text is not identical to success on the user's task.

## 3. Unigram model

The unigram model generates independent tokens until `STOP`:

\[
P(w_1,\ldots,w_n)
=
\left(\prod_{i=1}^{n}p(w_i)\right)p(\mathrm{STOP}).
\]

It generalizes beyond complete training sentences because a novel sentence can receive positive probability when all its words were observed. Its central weakness is order invariance:

\[
P(w_1,w_2)=P(w_2,w_1).
\]

### Why it normalizes

Let \(s=p(\mathrm{STOP})>0\) and \(q=1-s=\sum_{w\in V}p(w)\). The total probability of all sentences of length \(k\) is:

\[
q^ks.
\]

Summing over every finite length:

\[
\sum_{k=0}^{\infty}q^ks
=
\frac{s}{1-q}
=1.
\]

The infinite upper limit indexes all finite values of \(k\); it does not add an infinite-length sentence. Equivalently:

\[
P(\text{never STOP})=\lim_{k\to\infty}q^k=0.
\]

Showing that each particular infinite sequence has probability zero is not sufficient by itself; the never-stopping event must be handled as a whole.

## 4. Bigram and first-order Markov models

A bigram LM assumes:

\[
P(w_i\mid w_1,\ldots,w_{i-1})
=
P(w_i\mid w_{i-1}).
\]

Thus:

\[
P(w_1,\ldots,w_n)
=
P(w_1\mid\mathrm{START})
\left(\prod_{i=2}^{n}P(w_i\mid w_{i-1})\right)
P(\mathrm{STOP}\mid w_n),
\]

where the displayed factors are multiplied.

### Markov-chain view

- States are tokens plus `START` and `STOP`.
- An edge \(u\rightarrow v\) has probability \(P(v\mid u)\).
- Each transition-matrix row is a normalized distribution:

\[
T_{u,v}=P(v\mid u),
\qquad
\sum_vT_{u,v}=1.
\]

- A sentence probability is the product of transition probabilities along its path from `START` to `STOP`.
- The model is homogeneous when transition probabilities do not depend on the absolute position in the sentence.

### Maximum-likelihood estimate

\[
P_{\mathrm{ML}}(v\mid u)
=
\frac{C(u,v)}{\sum_{v'}C(u,v')}
=
\frac{C(u,v)}{C(u)}.
\]

For `START`, \(C(\mathrm{START})\) equals the number of training sentences.

### Eventual stopping

If every non-`STOP` state satisfies \(P(\mathrm{STOP}\mid u)\ge\varepsilon>0\), then:

\[
P(\text{no STOP in the first }k\text{ steps})
\le(1-\varepsilon)^k\rightarrow0.
\]

Therefore the model reaches `STOP` with probability \(1\).

## 5. Higher-order Markov models

A \(k\)-th order model conditions on the preceding \(k\) tokens:

\[
P(x_1,\ldots,x_n)
=
\prod_iP(x_i\mid x_{i-1},\ldots,x_{i-k}).
\]

It can be represented as a first-order chain over tuple states. For a second-order model:

\[
(a,b)\rightarrow(b,c)
\quad\text{with probability}\quad
P(c\mid a,b).
\]

The overlap is mandatory; a transition such as \((a,b)\rightarrow(d,c)\) with \(b\ne d\) is invalid.

Longer contexts can capture more dependencies, but they create exponentially many contexts. With \(m\) ordinary tokens and \(m^k\) boundary-free contexts:

\[
\text{free parameters}=m^k\cdot m=m^{k+1}.
\]

If legal `START`-padded contexts are included, their number is:

\[
1+m+\cdots+m^k,
\]

and the corresponding free next-token parameters are:

\[
m(1+m+\cdots+m^k).
\]

The fundamental limitation remains: for any fixed \(k\), dependencies can occur farther than \(k\) tokens away. A valid counterexample must hold the last \(k\) tokens fixed while changing a more distant word that determines the correct prediction.

## 6. Sparsity and smoothing

One zero transition makes the entire sentence probability zero. Low nonzero counts are also unreliable because MLE can overestimate events observed only once or twice.

### Add-\(\delta\)

\[
P_{\text{add-}\delta}(w\mid h)
=
\frac{C(h,w)+\delta}{C(h)+\delta|V|}.
\]

This removes zeros but generally reallocates too much probability mass in large language-model tables.

### Absolute discounting

\[
C^*(h,w)=\max(C(h,w)-d,0).
\]

The removed mass is:

\[
\lambda(h)
=
1-\sum_w\frac{C^*(h,w)}{C(h)}
=
\frac{d\,N_{1+}(h,*)}{C(h)},
\]

where \(N_{1+}(h,*)\) is the number of distinct observed continuations of \(h\).

### Kneser–Ney continuation probability

Ordinary unigram frequency asks how often \(w\) appeared. Kneser–Ney instead asks in how many distinct contexts \(w\) appeared:

\[
P_{\mathrm{cont}}(w)
=
\frac{|\{u:C(u,w)>0\}|}
{|\{(u,v):C(u,v)>0\}|}.
\]

The denominator is the total number of distinct bigram types in the corpus. Repetitions of the same pair do not increase it.

Full interpolated Kneser–Ney:

\[
P_{\mathrm{KN}}(w\mid h)
=
\frac{\max(C(h,w)-d,0)}{C(h)}
+\lambda(h)P_{\mathrm{cont}}(w).
\]

This keeps discounted higher-order evidence and redistributes removed mass according to continuation diversity.

## 7. Back-off and interpolation

### Hard back-off

Use the longest context considered reliable:

1. trigram estimate;
2. otherwise bigram estimate;
3. otherwise unigram estimate.

Basic hard back-off selects one context length.

### Linear interpolation

Interpolation combines all levels:

\[
q(w_i\mid w_{i-2},w_{i-1})
=
\lambda_1q_3(w_i)
+\lambda_2q_2(w_i)
+\lambda_3q_1(w_i),
\]

with:

\[
\lambda_i\ge0,
\qquad
\lambda_1+\lambda_2+\lambda_3=1.
\]

The \(n\)-gram distributions are estimated on training data. The lambda hyperparameters are selected to maximize held-out validation log-likelihood:

\[
L(\lambda)
=
\sum_{w_1,w_2,w_3}
C'(w_1,w_2,w_3)
\log q(w_3\mid w_1,w_2).
\]

### Reliability buckets

Different context-frequency groups may use different weight vectors:

\[
q(w\mid h)
=
\sum_{r=1}^{R}\lambda_{r,\Pi(h)}q_r(w\mid h).
\]

\(\Pi(h)\) is a bucket label, not an exponent. With \(B\) buckets and \(R\) component models:

- lambda values: \(BR\);
- free lambda parameters: \(B(R-1)\).

Each bucket's weight vector sums to \(1\), so no additional normalization is required:

\[
\sum_wq(w\mid h)
=
\sum_r\lambda_{r,\Pi(h)}\sum_wq_r(w\mid h)
=1.
\]

## 8. Pereira's latent-category generalization

Pereira introduced an unobserved category \(c\) associated with the preceding word:

\[
P(w_i\mid w_{i-1})
=
\sum_cP(c\mid w_{i-1})P(w_i\mid c).
\]

The derivation first marginalizes over \(c\), then applies the product rule. The final step makes the modeling assumption:

\[
W_i\perp W_{i-1}\mid C.
\]

The category is intended to summarize the information in \(w_{i-1}\) relevant to predicting \(w_i\). An unseen pair \((u,w)\) can receive positive probability whenever some category satisfies:

\[
P(c\mid u)>0
\quad\text{and}\quad
P(w\mid c)>0.
\]

The model was trained with EM because categories were latent. Modern word representations pursue a related generalization goal with continuous multidimensional vectors rather than a small set of discrete categories.

## 9. Perplexity and cross-entropy

For \(M\) held-out tokens:

\[
H
=
-\frac1M\sum_{t=1}^{M}\log P(x_t\mid x_{<t}).
\]

Perplexity is:

\[
\mathrm{PPL}=e^H
\]

for natural logarithms, or:

\[
\mathrm{PPL}=2^H
\]

for base-2 logarithms.

A uniform model over \(N\) tokens has:

\[
H=\log N,
\qquad
\mathrm{PPL}=N.
\]

Perplexity is therefore interpreted as an effective average branching factor. A non-uniform model has perplexity below \(N\) only when it assigns better-than-uniform probability to the observed test tokens. A badly mismatched model can exceed \(N\), and a zero-probability test event yields infinite perplexity.

Perplexity values are comparable only with the same corpus, vocabulary, and tokenization. Lower perplexity does not guarantee better downstream performance, so extrinsic evaluation remains important.

## 10. What went well

- Bigram factorization, Markov-chain semantics, path probabilities, transition matrices, and MLE counts were understood well.
- The proof of eventual stopping in the bigram model was strong.
- Tuple-state conversion for higher-order models was understood after clarification.
- Discount normalization and Kneser–Ney continuation probability were handled correctly.
- Interpolated-mixture normalization and lambda parameter counting were answered correctly.
- Pereira's factorization, conditional-independence assumption, and unseen-pair generalization were understood well.

## 11. Items to revisit

1. **Formal LM definition:** begin with a joint distribution over \(V^*\), not only a next-token conditional.
2. **`STOP` factor:** include it in every complete sentence-probability formula.
3. **Unigram normalization:** distinguish the never-stopping event from individual infinite sequences.
4. **Free parameters:** subtract one normalization constraint per categorical distribution.
5. **Higher-order boundary contexts:** distinguish \(m^k\) ordinary contexts from legal `START`-padded contexts \(1+m+\cdots+m^k\).
6. **Fixed-\(k\) counterexamples:** keep the final \(k\) tokens identical and vary only the distant dependency.
7. **Zipf's law:** \(f(r)\propto1/r\), not geometric decay.
8. **Sentence-level sparsity:** contrast \(|V|^n\) possible length-\(n\) strings with much slower word-level coverage.
9. **Objective versus capability:** likelihood mismatch is different from architectural or context-window limitations.
10. **Read every sub-part:** one earlier answer omitted the explicitly requested risk component.

## 12. Slides marked for rereading

- `linear-interpolation/linear-interpolation.pdf`, slide 3/4: validation log-likelihood and constrained lambda optimization.
- `generalization-pereiras-solution/generalization-pereiras-solution.pdf`, slide 3/4: latent-category marginalization and the final independence assumption.
