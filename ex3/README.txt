NLP Exercise 3 — Question 3 (HMM POS tagger)
==============================================

Files
-----
- tagger.py     Python module with all logic (corpus loading, baseline tagger,
                bigram HMM training, MLE / Add-one emissions, Viterbi decoding,
                evaluation helpers, diagnostic utilities).
- notebook.ipynb  Jupyter notebook orchestrating the experiments and showing
                  results for parts (a) through (d) plus a diagnostic
                  inspection of low-frequency and unknown words.
- README.txt    This file.

Running
-------
1. Create a Python 3.10+ environment and install the dependencies:

       python -m venv venv
       source venv/bin/activate     (Windows: venv\Scripts\activate)
       pip install nltk numpy matplotlib jupyter

2. Open the notebook and run all cells:

       jupyter notebook notebook.ipynb

   The first call to load_brown_news downloads the Brown corpus via NLTK
   automatically (quiet mode).

Notes
-----
- All logic lives in tagger.py; the notebook only imports, calls, and prints.
- Tags from the Brown corpus are simplified by taking the prefix before the
  first '+' or '-' (per the exercise footnote).
- The last 10% of the "news" sentences are used as the test set.
- Pure MLE Viterbi pins unknown words to "NN"; Add-one smoothing makes
  every (word, tag) pair nonzero so Viterbi can tag unknowns freely.
