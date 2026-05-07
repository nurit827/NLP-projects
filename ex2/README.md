# Ex2 — Q4: Comparison of the three models

## (a) Which model had the highest accuracy?

The fine-tuned **distilroberta-base** transformer with **portion = 0.2** of the training data — it reached the best validation accuracy of any run across the three models / four portions.

## (b) Which model was the most sensitive to training-set size?

The **transformer** — by a wide margin.

- At `portion=0.1`, validation accuracy **peaks around epoch 2 and then drops** — classic overfitting in only 3 epochs.
- At `portion=0.2`, validation accuracy **keeps climbing** for all 3 epochs and reaches the best score of the whole exercise.

That much sensitivity (overfit at 10% → still accelerating at 20%) doesn't show up in the smaller models:

- The **MLP** is moderately sensitive — bigger portions help, but the curves are not nearly as different as the transformer's.
- The **log-linear** classifier is the least sensitive — it improves slowly with more data and looks similar across portions.

So the order from most to least sensitive to training-set size is: **transformer > MLP > log-linear**.

## (c) Trainable parameter counts

| Model | Trainable parameters |
|---|---:|
| Log-linear (Q1) — `Linear(2000, 4)` | 8,004 |
| MLP (Q2) — `Linear(2000, 500) → ReLU → Linear(500, 4)` | 1,002,504 |
| distilroberta-base + classification head (Q3) | 82,121,476 |

**Do additional parameters help?**

Yes — given enough data — but they bring an overfitting cost.

- More parameters give the model more capacity to capture useful patterns, which is why the transformer (~82M params) beats the MLP (~1M), which beats the log-linear (~8K), when given enough training examples.
- But the same extra capacity makes the model more prone to overfitting when data is scarce — the transformer at `portion=0.1` overfits within 2 epochs, whereas the log-linear barely overfits at all on the same data.

In short: **more parameters → higher peak accuracy, but higher sensitivity to training-set size.**
