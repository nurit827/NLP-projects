# Exam style notes — NLP 67658 (HUJI, Omri Abend), distilled from 2017–2025 exams

Source: all 17 PDFs in `past-exams/`. Purpose: generate NEW practice questions in this style. NEVER reuse the real questions (see "Off-limits scenarios" at the bottom).

## Format shell (stable 2017–2020, 2023–2025)

- 2 hours, closed material, 100 pts, **all open questions — zero multiple choice, zero rote recall**.
- Part A (80): answer exactly **2 of 3** questions × 40 pts, each with 2–5 escalating sub-parts (5–30 pts).
- Part B (20): answer exactly **1 of 2** questions × 20 pts, usually 2×10 sub-parts, single-concept.
- 2021–2022 were 72-hour COVID take-homes (5 mandatory questions, harder design/proof flavor) — style still relevant, format not.
- Appendices (transition-system definitions, POS tag lists) appeared 2018–2019 only; since then all setup is inline in the question.
- Since 2024B: blanket rule — an answer without justification earns no credit.

## Question archetypes (ranked; mix these in practice sessions)

1. **Define formally** — "define X, defining every symbol/notation; no need to describe training/inference." 5–15 pts. Expected answer: the formula with every symbol defined, nothing more. (CRF, MEMM, HMM, k-gram LM, Kneser-Ney, PCFG, NB, MST scorer, RNN, perplexity, BLEU, beam search, sibling model…)
2. **Design an efficient algorithm / write pseudo-code** — the signature high-value item (15–30 pts). Most common flavor: given a *trained* CRF/HMM/MEMM, compute a constrained or clamped marginal (P of a tagging with boundary conditions; P(y2=t1, y4=t2 | x); total mass of "legal" sequences) → forward–backward / sum-Viterbi variants. Also: CKY (max and sum), greedy/oracle for transition systems, perceptron with a black-box argmax oracle, Viterbi over product tag spaces with runtime in M and n. Conventions: black-box helpers may be assumed; "no need to prove correctness"; runtime must be stated; "informal answers not accepted."
3. **Invent a variant model / novel toy task, then interrogate it** — the exam defines a new formalism (pair-emission HMM, POS-marginalized LM, custom back-off formula, modified transition system, a new tag-scheme task) and runs the standard battery on it: joint formula → parameter count → pseudo-code → assumptions → small proof.
4. **Prove/derive a small property** — a few lines each: normalization conditions (interpolation λ's, KN constant), invariances (IBM-1 word order), temperature T=1 identity and T→0 limit, LM-without-STOP sums >1, MEMM conditional independence, transition-system expressivity containment, PCFG can't disambiguate given tree pairs.
5. **Count the parameters** — given set sizes (|V|, n_Y, m1, m2…); often re-count after adding an independence assumption to show the shrink.
6. **State the independence assumption and refute it** with a concrete natural-language example (long-distance agreement is the canonical full-credit example).
7. **Break-the-model / ablation what-ifs** — force uniform HMM transitions or emissions; remove positional encodings; tie attention W_Q/W_K/W_V across heads; drop the partition function in Viterbi; remove REDUCE from arc-eager; set add-d's d too large; one global λ set. Characterize exactly what changes/breaks, why, with an example.
8. **Expressiveness yes/no batteries** — "can feature X be represented in edge-factored / sibling / CRF / MEMM / BoW model Y?" Full-credit answer = one sentence pinpointing what the score function's arguments can and cannot see.
9. **Diagnose a weakness / compare models on a shared task** — label bias, negation in BoW, sparsity, distant-supervision confounds; NB vs log-linear+embeddings vs fine-tuned BERT; Markov vs RNN; CRF vs pointwise. "Which handles X and why"; how the newer model fixes the older one's problem.
10. **Design a tag scheme / adapt machinery to a new task** — invent CRF label sets for span tasks, encode/decode pseudo-code between annotation formats and label sequences, hybrid pipelines (neural detector feeding a classical parser).

## Phrasing conventions (imitate these)

- Real exams: Hebrew prose, English technical terms inline. Practice in English unless asked otherwise, keeping the conventions.
- Notation: sentences x1…xn, tags y1…yn from set L, START/STOP symbols; assumptions labeled (A), (B) and referenced across sub-parts.
- Sub-parts escalate within one scenario: (a) define → (b) analyze/apply → (c) fix/code → (d) prove/stress-test.
- Systematic scope-limiting: "no need to describe training/inference", "no need to prove correctness", "no need to solve the optimization, only define it", "feature functions out of scope".
- "Justify your answer" on nearly every part; "accompany your explanation with an example" is a standard tail.
- Toy setups are tiny, concrete, and force a *qualitative provable decision*, not arithmetic: a few symbols/numbers, minimal-pair sentences, 2 candidates + 1 reference.

## Expected answer depth (from the 2024A/2025A/2025B solution files)

Full-credit answers are **short and surgical**: one clean formula with all symbols defined + 2–5 sentences of justification, or 3–10 lines of numbered pseudo-code, or a one-line-per-item bullet list for pros/cons. A 30-point pseudo-code answer fits in ~10 lines. Grade practice answers to this bar: every symbol explained, justification mandatory, no essays.

## Topic frequency map (for balancing sessions)

- **Every year, 40-pt core**: sequence models (HMM/MEMM/CRF) with DP inference; n-gram LMs + smoothing (interpolation / Kneser-Ney).
- **Nearly every year**: dependency parsing (MST edge-factored expressiveness, transition systems, higher-order features); classification (NB / log-linear, BoW, negation).
- **Since 2024**: Transformer *mechanics* (self-attention computation, multi-head, positional encodings, encoder-decoder MT training/decoding) and BERT (fine-tuning design, hybrids with classical parsers) as 40-pt cores.
- **Part B rotation**: perplexity, BLEU (+ limitations), distant supervision (+ SRL, path features), RNN definition, interpolation, beam search, oracles/dynamic oracles, PCFG lexicalization, sibling model, evaluation metrics (PARSEVAL, many-to-one accuracy).
- **Absent through 2025** (low priority): LLM usage/prompting, RLHF/post-training, RAG. The center of gravity is statistical sequence models + Transformer mechanics.
- Realistic mock exam = 2 of {CRF/HMM constrained inference, n-gram+smoothing variant, parsing, Transformer/BERT hybrid} at 40 pts + 1 of {perplexity, BLEU, distant supervision, RNN, higher-order parsing} at 20 pts.

## Cross-topic link patterns (use for the mandatory linking questions)

- Smoothing grafted onto other components: KN on HMM emissions; pseudowords vs embeddings/BERT; add-d × temperature sampling; frequency-bucketed / context-dependent interpolation λ's.
- Sequence models re-viewed as LMs (HMM induces an LM; does MEMM?).
- Classical ↔ neural: RNN vs Markov assumption; CRF label schemes with BERT features; BERT detector feeding an MST-parser pipeline; count-based vs prediction-based embeddings.
- Same constraint enforced in two paradigms (transition-based vs graph-based parsing).
- Sequence machinery lifted to a new level (documents as a chain; segmentation tasks as tagging).
- Classification ↔ embeddings ↔ domain adaptation.

## Off-limits scenarios (already used by real exams — never reuse in practice questions)

Toy tasks/setups: Chinese word segmentation (MEMM), married-couples relation extraction, gappy multi-word expressions ("made his sister laugh"), chapter segmentation of a document, punctuation restoration, clause-coordinating "and" detection + split-parse pipeline, article-country classification, sentiment three-model comparison (NB/word2vec/BERT), MWE tag scheme of size 2|L|+1.
Invented variants: pair-emission HMM (x,w), POS-marginalized LM, Arc-normal transition system, arc-eager minus REDUCE, "total character length of a tree" feature, temperature sampling on trigram LM, three-RNN interpolation with a-/b-prefix context weights, KN-on-emissions, joint two-task tagging over product tag space.
Signature examples: "colorless green ideas", "dog bit man"/"man bit dog", "hungry car mechanic" tree pairs, "u 2" spelling errors, (Ben-Gurion, Plonsk)/(Tim Cook, Apple), boundary-constrained NER (first word Person, last word Location), P(y2,y4,y6) clamped marginal, ?/! joint punctuation marginal.
Rule of thumb: change the task domain AND the twist, not just the numbers.
