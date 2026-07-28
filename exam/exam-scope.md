# Official exam scope — 2026-07-27

The official focus announcement (26/07/2026) and WhatsApp clarification (27/07/2026) state that there will be no exam questions on **four lecture presentations**:

1. **HMM**
2. **Dependency parsing** — including graph-based dependency parsing
3. **Grammar**
4. **LLM post-training**

## Repository mapping (4 excluded presentations)

| Excluded area | Directory / path |
|---|---|
| HMM | `04-HMM/` (entire lecture folder) |
| Dependency parsing (incl. graph-based) | `09-Dependency-Parsing/` — subtopics: `dependency-parsing/`, `graph-based-parsing/`, `mst-parser/`, `neural-mst-parsing/` |
| Grammar | `07-Syntax/grammar/` |
| Post-training | `12-PostTraining/` — subtopics: `post-training/`, `rlhf/`, `instruct-lm/`, `agents/` |

Other `07-Syntax/` subtopics (morphology, dependencies as linguistic concepts, noun phrases, etc.) remain **in scope** unless they are part of the excluded grammar deck.

## Viterbi — in scope (concept-specific exception)

Viterbi appears in the HMM slides (`04-HMM/viterbi-algorithm/`) but is also used in MEMM and CRF (`05-MEMM-CRF/`). The lecturer confirmed (27/07/2026) that **Viterbi must be known** for the exam — but only in MEMM/CRF (and other in-scope) contexts. Do not generate HMM-specific Viterbi or POS-tagging questions.

## Study-agent rule

Skip excluded material during exam preparation. Do not generate slide checks, exam questions, cross-topic links, weak-spot reviews, or mock-exam content about excluded topics.

**Concept-specific exclusions:** Never ask HMM-specific content (HMM definitions, forward/backward, Baum-Welch, POS tagging with HMM). Never ask grammar or dependency-parsing content. Do teach, review, and question **Viterbi** in MEMM/CRF contexts.

The next in-scope lecture after `03-Classification-LogLinear/` is `05-MEMM-CRF/`.
