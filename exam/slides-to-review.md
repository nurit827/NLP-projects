# Slides to review

Slides worth rereading before the exam. Keep entries brief and point to the original deck.

## 2026-07-23 — Linear interpolation optimization
- **Lecture/subtopic:** 02-Markov-LM / linear-interpolation
- **Deck:** `02-Markov-LM/linear-interpolation/linear-interpolation.pdf`
- **Slide:** 3/4 — Back-off: Linear Interpolation
- **Why revisit:** Dense derivation of validation-corpus log-likelihood and the constrained concave optimization used to choose \(\lambda_1,\lambda_2,\lambda_3\).
- **Key expressions:** \(L=\sum C'(w_1,w_2,w_3)\log q(w_3\mid w_1,w_2)\), with \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\).

## 2026-07-23 — Pereira's latent-category factorization
- **Lecture/subtopic:** 02-Markov-LM / generalization-pereiras-solution
- **Deck:** `02-Markov-LM/generalization-pereiras-solution/generalization-pereiras-solution.pdf`
- **Slide:** 3/4 — Pereira's Solution
- **Why revisit:** The marginalization, product-rule factorization, and final conditional-independence assumption are easy to conflate.
- **Key expressions:** \(P(w_i\mid w_{i-1})=\sum_cP(c\mid w_{i-1})P(w_i\mid c)\); \(W_i\perp W_{i-1}\mid C\).

## 2026-07-23 — Log-linear likelihood gradient derivation
- **Lecture/subtopic:** 03-Classification-LogLinear / log-linear-models
- **Deck:** `03-Classification-LogLinear/log-linear-models/log-linear-models.pdf`
- **Slide:** 7/12 — Derivation
- **Why revisit:** Dense differentiation of the gold score minus log-partition function into observed features minus model-expected features.
- **Key expressions:** \(\log P(y\mid x;w)=w^\top\phi(x,y)-\log\sum_{y'}e^{w^\top\phi(x,y')}\); \(\nabla L=\sum_i[\phi(x_i,y_i)-\sum_{y'}P(y'\mid x_i;w)\phi(x_i,y')]\).

## 2026-07-23 — Scherer's affective-state typology
- **Lecture/subtopic:** 03-Classification-LogLinear / sentiment-analysis
- **Deck:** `03-Classification-LogLinear/sentiment-analysis/sentiment-analysis.pdf`
- **Slide:** 4/11 — Scherer Typology of Affective States
- **Why revisit:** Distinguishes emotion, mood, interpersonal stance, attitude, and personality trait; sentiment analysis primarily concerns attitudes.
- **Key ideas:** Emotion is a brief event response; mood is diffuse and longer-lived; attitude is an enduring affectively colored disposition toward an object or person.

## 2026-07-26 — MEMM feature vector versus probability
- **Lecture/subtopic:** 05-MEMM-CRF / memm
- **Deck:** `05-MEMM-CRF/memm/memm.pdf`
- **Slide:** 3/15 — Feature/History Representation
- **Why revisit:** \(f(x,y)\) is a feature vector, not a probability or score; the distinction between features, scores, and probabilities caused confusion.
- **Key ideas:** \(f(x,y)\) jointly describes context \(x\) and candidate label \(y\); \(w^\top f(x,y)\) is the score; softmax over candidate-label scores produces \(P(y\mid x)\).

## 2026-07-26 — MEMM history notation
- **Lecture/subtopic:** 05-MEMM-CRF / memm
- **Deck:** `05-MEMM-CRF/memm/memm.pdf`
- **Slide:** 4/15 — Feature/History Representation
- **Why revisit:** The slide mostly renames the local classifier arguments; distinguish packaged history from the candidate current tag.
- **Key ideas:** \(h_i=(t_{i-2},t_{i-1},x_{1:n},i)\) contains previous tags, the full observed sentence, and position; \(t=t_i\) is the candidate current label, so \(f(h,t)\) is equivalent to writing every argument explicitly.

## 2026-07-26 — MEMM sequence likelihood
- **Lecture/subtopic:** 05-MEMM-CRF / memm
- **Deck:** `05-MEMM-CRF/memm/memm.pdf`
- **Slide:** 8/15 — MLE in MEMMs
- **Why revisit:** Connects the familiar local softmax to training: multiply the probability of the correct label across every position and sentence; implementations equivalently add log-probabilities.
- **Key expressions:** \(L(w)=\prod_i\prod_j P(y_j^{(i)}\mid y_{j-1}^{(i)},x^{(i)};w)\); \(\log L(w)=\sum_i\sum_j\log P(y_j^{(i)}\mid y_{j-1}^{(i)},x^{(i)};w)\).

## 2026-07-26 — MEMM log-softmax decomposition
- **Lecture/subtopic:** 05-MEMM-CRF / memm
- **Deck:** `05-MEMM-CRF/memm/memm.pdf`
- **Slide:** 9/15 — MLE in MEMMs
- **Why revisit:** Clarifies that \(Z(h;w)\) is simply the local softmax denominator and explains why each log-probability becomes a gold-label score minus a log-normalizer.
- **Key expressions:** \(Z(h;w)=\sum_{y'\in T}e^{f(h,y')^\top w}\); \(\log P(y\mid h)=f(h,y)^\top w-\log Z(h;w)\).
