NLP Exercise 4 — MST Parser and Attention-Based Parsing
========================================================

Files
-----
- utils.py      Python module with all logic (corpus loading, feature function,
                MST inference via Chu-Liu/Edmonds, averaged perceptron training,
                evaluation helpers).
- notebook.ipynb  Jupyter notebook orchestrating the experiments and showing
                  results for Parts 1 and 2.
- chu_liu_edmonds.py   Provided implementation of the Chu-Liu/Edmonds algorithm.
- transformer_parser_utils.py  Provided utilities for BERT attention extraction.
- README.txt    This file.

Running
-------
1. Create a Python 3.10+ environment and install the dependencies:

       python -m venv venv
       source venv/bin/activate     (Windows: venv\Scripts\activate)
       pip install nltk numpy transformers torch jupyter

2. Open the notebook and run all cells:

       jupyter notebook notebook.ipynb

   The first call to load_data() downloads the dependency_treebank corpus via
   NLTK automatically (quiet mode).

Notes
-----
- All logic lives in utils.py; the notebook only imports, calls, and prints.
- The last 10% of the dependency_treebank sentences are used as the test set.
- The perceptron uses 2 iterations with learning rate 1 and averaged weights.
- Inference uses Chu-Liu/Edmonds on negated scores (min arborescence = max tree).
- For Part 2, BERT attention weights are used directly as arc scores (no training).

AI usage declaration
--------------------
AI usage declaration - We used Claude Code to assist with writing and
debugging parts of the code for the practical section of this project.
