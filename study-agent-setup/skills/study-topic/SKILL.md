---
name: study-topic
description: Run an interactive exam-prep session on one NLP course topic or subtopic. Invoke for /study-topic, “let's study <topic>”, or “quiz me on <topic>”. Reads lecture slides and transcripts, asks exactly two new exam-style questions, revisits prior weak spots, and logs progress.
---

# Study topic

## Purpose

Run topic-by-topic NLP exam preparation using materials under the repository's `exam/` directory. Questions must be new; past exams are style references only.

## Material layout

- `exam/exam-scope.md` — current official inclusion/exclusion rules; authoritative when selecting topics and questions.
- `exam/NN-Topic-Name/` — lecture folders containing full decks and subtopic folders.
- `transcript.md` — lecturer transcript beside a lecture or subtopic deck when available.
- `exam/transcripts/exam-hints-from-lectures.md` — optional exam remarks and announcements.
- `exam/past-exams/` — style reference and off-limits checking only.
- `exam/exam-style-notes.md` — optional distilled exam conventions.
- `exam/progress.md` — completed sessions and results.
- `exam/weak-spots.md` — spaced-repetition queue.
- `exam/pre-exam-review.md` — critical concepts to reread before the exam.
- `exam/slides-to-review.md` — slides explicitly marked for rereading.

## Cardinal rule: never reuse past-exam questions

- Never ask a past-exam question verbatim or paraphrased.
- Do not reuse its toy values, example sentences, or invented model variant.
- Imitate only the archetype, phrasing, structure, and difficulty.
- If uncertain, change both the task domain and the model twist.
- Do not reveal specific past-exam content during study.

## Exam-question archetypes

Mix these styles:

1. Formal definition with every symbol explained.
2. Efficient algorithm or pseudocode.
3. Parameter counting with normalization constraints.
4. Conditional-independence assumption plus counterexample.
5. Small proof or derivation for a new model variant.
6. Manual algorithm trace.
7. Weakness or failure-mode diagnosis.
8. Comparison explaining how a newer model fixes an older limitation.

Use short, precise expected answers. Require justification.

## Session flow

1. **Choose an in-scope topic.** Read `exam/exam-scope.md` first. Never select excluded material or use it in questions, link-backs, reviews, or mock exams. Then read `exam/progress.md` and `exam/weak-spots.md`.
2. **Load the material.** Read the subtopic PDF, its transcript when available, and `exam/exam-style-notes.md` when present. Open the PDF for the user when starting a subtopic.
3. **Walk one slide at a time.** Briefly explain its key idea and any lecturer emphasis from the transcript. Stay until the user asks to move.
4. **Do not ask slide-level questions.** Move immediately when the user says “next.” Reserve retrieval questions for subtopic end.
5. **Ask exactly two exam-level questions at subtopic end.** Ask them one at a time. Include at least one formal/prove-or-derive item and, when possible, one link to a previously studied in-scope topic. Never quiz unseen or excluded material.
6. **Grade tersely.** State what earned credit, what is missing, and a brief model answer. Do not advance until the user explicitly continues.
7. **Track weaknesses.** Append shaky or missed concepts to `exam/weak-spots.md`. When later answered solidly, strike them through with the clearing date instead of deleting them.
8. **Log completion.** Append the date, topic, slides covered, question archetypes, and verdicts to `exam/progress.md`.
9. **Save critical notes.** Add compact concepts to `exam/pre-exam-review.md` when the user asks or when a concept is unusually important.

## Tone

Terse and direct. One question at a time. Do not lecture unless asked.
