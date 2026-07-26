# Portable NLP study-agent setup

This bundle contains the reusable agent configuration for slide-by-slide NLP exam study. All source files are kept in visible directories so they are easy to inspect and share.

## Install

1. Copy the `exam/` directory into the recipient's repository.
2. Copy each directory under `skills/` to either:
   - `<recipient-repository>/.cursor/skills/` for project-local installation; or
   - `~/.cursor/skills/` for user-wide installation.
3. Put the recipient's lecture materials under `exam/`.
4. Start a session with `/study-topic` or “let's study <topic>”.
5. Use `/remember` to save the current slide for later review.

## Expected material layout

```text
exam/
├── progress.md
├── weak-spots.md
├── pre-exam-review.md
├── slides-to-review.md
├── exam-style-notes.md          # optional
├── transcripts/
└── NN-Topic-Name/
    ├── full-lecture.pdf
    ├── transcript.md            # optional
    └── subtopic-name/
        ├── subtopic-name.pdf
        └── transcript.md        # optional
```

The skill sources use repository-relative paths and should work from any checkout location after installation.

## Not included

- Lecture PDFs or transcripts
- Past exams
- The original student's progress and weak spots

Only share course materials separately when permitted.
