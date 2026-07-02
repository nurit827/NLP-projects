# NLP Exercise 5 — Sentiment Analysis with Neural Models

**Authors:** Nurit Tolkowsky and Shaul Tolkowsky

## Files

| File | Description |
|------|-------------|
| `exercise5_skeleton.py` | All model code and training logic: the `LogLinear` and `LSTM` classes, the fine-tuned `TransformerSentimentClassifier`, the data/embedding helpers, the training and evaluation utilities, and the four `train_*` functions for Sections 6–9. |
| `data_loader.py` | Provided dataset loader (unchanged). |
| `run_all.py` | Convenience runner that calls all four `train_*` functions in order and prints their results. |
| `README.md` | This file. |

The results and written answers for Sections 6–11, including all plots, are in the separate file **`answers.pdf`**, as required.

> The dataset folder `stanfordSentimentTreebank/` (extracted from `stanfordSentimentTreebank.zip`) must sit next to these files before running.

## Running

1. Create a Python environment and install the dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install torch transformers numpy matplotlib
   ```

2. Run all four models:

   ```bash
   python run_all.py
   ```

   or call an individual model from a Python shell:

   ```python
   import exercise5_skeleton as ex5
   ex5.train_log_linear_with_one_hot()
   ex5.train_log_linear_with_transformer()
   ex5.train_lstm_with_transformer()
   ex5.train_transformer()
   ```

   Each function trains the model, saves its train/validation loss and accuracy plots as PNG files, and prints the test loss/accuracy and the accuracy on the two special test subsets.

## Hyperparameters

Exactly as specified in the exercise:

| Section | Model | Settings |
|---------|-------|----------|
| 6 | one-hot log-linear | lr 0.01, 10 epochs, batch 64 |
| 7 | transformer-avg log-linear | lr 0.01, no weight decay, 10 epochs, batch 64 |
| 8 | bi-LSTM | lr 0.001, weight decay 1e-4, dropout 0.5, 4 epochs, batch 64, hidden dim 100, sequence length 52 |
| 9 | fine-tuned distilroberta | lr 1e-5, weight decay 0, 2 epochs, batch 64, 2500 training sentences, `BCEWithLogitsLoss`, Adam, native PyTorch (no HuggingFace Trainer) |

Sections 6–8 train on the full sentences together with their sub-phrases; Section 9 trains on full sentences only.

## Notes / deviations from the provided API

- **Pretrained model:** we use `distilroberta-base` from HuggingFace `transformers` for Sections 7–9. For Sections 7 and 8 its token embedding matrix is extracted once and used as a frozen look-up table (a plain numpy array, not a trainable `nn.Embedding`). `load_transformer_embeddings()` caches this matrix locally to `transformer_emb_cache.pkl` so it is not rebuilt on every run.

- **Section 9 training-set size:** the exercise asks to use `DataManager`'s `max_train_samples` argument to draw 2500 training sentences, but the provided `DataManager` in the skeleton has no such argument. We instead sample the 2500 sentences directly from the full training set with a fixed seed (`random.Random(42).sample`), which is numerically equivalent to what was asked. This is also documented in the docstring of `train_transformer()`.

- **Device selection:** the training code auto-detects the device, preferring CUDA, then Apple-Silicon MPS, then CPU (with `PYTORCH_ENABLE_MPS_FALLBACK` enabled for MPS). We ran the final training on a GPU node of the HUJI Moriah cluster (NVIDIA L40S); the same code runs unchanged on CPU or on a local Mac via MPS.

## AI usage declaration

We used Claude Code to assist with writing and debugging parts of the code.
