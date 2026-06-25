"""Run all four Ex5 models end-to-end, printing results and saving plots."""
import exercise5_skeleton as ex5

if __name__ == "__main__":
    for name, fn in [
        ("SECTION 6: one-hot log-linear",        ex5.train_log_linear_with_one_hot),
        ("SECTION 7: transformer-avg log-linear", ex5.train_log_linear_with_transformer),
        ("SECTION 8: bi-LSTM",                    ex5.train_lstm_with_transformer),
        ("SECTION 9: fine-tuned distilroberta",   ex5.train_transformer),
    ]:
        print("\n" + "=" * 70)
        print(name)
        print("=" * 70, flush=True)
        fn()
