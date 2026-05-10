

###################################################
# Exercise 2 - Natural Language Processing 67658  #
###################################################

import numpy as np

# subset of categories that we will use
category_dict = {'comp.graphics': 'computer graphics',
                 'rec.sport.baseball': 'baseball',
                 'sci.electronics': 'science, electronics',
                 'talk.politics.guns': 'politics, guns'
                 }

def get_data(categories=None, portion=1.):
    """
    Get data for given categories and portion
    :param portion: portion of the data to use
    :return:
    """
    # get data
    from sklearn.datasets import fetch_20newsgroups
    data_train = fetch_20newsgroups(categories=categories, subset='train', remove=('headers', 'footers', 'quotes'),
                                    random_state=21)
    data_test = fetch_20newsgroups(categories=categories, subset='test', remove=('headers', 'footers', 'quotes'),
                                   random_state=21)

    # train
    train_len = int(portion*len(data_train.data))
    x_train = np.array(data_train.data[:train_len])
    y_train = data_train.target[:train_len]
    # remove empty entries
    non_empty = x_train != ""
    x_train, y_train = x_train[non_empty].tolist(), y_train[non_empty].tolist()

    # test
    x_test = np.array(data_test.data)
    y_test = data_test.target
    non_empty = np.array(x_test) != ""
    x_test, y_test = x_test[non_empty].tolist(), y_test[non_empty].tolist()
    return x_train, y_train, x_test, y_test


# Q1,2
def MLP_classification(portion=1., model=None):
    """
    Train a torch classifier (linear or MLP) on TFIDF features.
    :param portion: portion of the train data to use
    :param model:   instantiated nn.Module to train
    :return:        (train_losses, val_accs) per epoch
    """
    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader, TensorDataset
    from sklearn.feature_extraction.text import TfidfVectorizer
    from tqdm import tqdm

    x_train, y_train, x_test, y_test = get_data(categories=category_dict.keys(), portion=portion)

    feature_dim = 2000
    epochs = 20
    batch_size = 16
    lr = 1e-3

    vectorizer = TfidfVectorizer(max_features=feature_dim)
    X_train = vectorizer.fit_transform(x_train).toarray().astype(np.float32)
    X_test  = vectorizer.transform(x_test).toarray().astype(np.float32)
    y_train_a = np.array(y_train, dtype=np.int64)
    y_test_a  = np.array(y_test,  dtype=np.int64)

    train_loader = DataLoader(
        TensorDataset(torch.from_numpy(X_train), torch.from_numpy(y_train_a)),
        batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(
        TensorDataset(torch.from_numpy(X_test), torch.from_numpy(y_test_a)),
        batch_size=batch_size)

    dev = torch.device('cuda' if torch.cuda.is_available()
                       else ('mps' if torch.backends.mps.is_available() else 'cpu'))
    model = model.to(dev)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    train_losses, val_accs = [], []
    for epoch in range(1, epochs + 1):
        model.train()
        running, n = 0.0, 0
        for xb, yb in train_loader:
            xb, yb = xb.to(dev), yb.to(dev)
            optimizer.zero_grad()
            loss = criterion(model(xb), yb)
            loss.backward()
            optimizer.step()
            running += loss.item() * xb.size(0)
            n += xb.size(0)
        train_losses.append(running / n)

        model.eval()
        correct, total = 0, 0
        with torch.no_grad():
            for xb, yb in test_loader:
                xb, yb = xb.to(dev), yb.to(dev)
                correct += (model(xb).argmax(1) == yb).sum().item()
                total += yb.size(0)
        val_accs.append(correct / total)
        print(f'Epoch {epoch:02d} | train loss {train_losses[-1]:.4f} | val acc {val_accs[-1]:.4f}')
    return train_losses, val_accs


# Q3
def transformer_classification(portion=1.):
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    from torch.utils.data import DataLoader
    import evaluate
    from tqdm import tqdm

    class Dataset(torch.utils.data.Dataset):
        """
        Dataset for loading data
        """
        def __init__(self, encodings, labels):
            self.encodings = encodings
            self.labels = labels

        def __getitem__(self, idx):
            item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
            item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
            return item

        def __len__(self):
            return len(self.labels)

    def train_epoch(model, data_loader, optimizer, dev='cpu'):
        """
        Perform an epoch of training of the model with the optimizer
        :return: Average per-example loss over the epoch
        """
        model.train()
        total_loss, n = 0.0, 0
        for batch in tqdm(data_loader):
            input_ids = batch['input_ids'].to(dev)
            attention_mask = batch['attention_mask'].to(dev)
            labels = batch['labels'].to(dev)
            optimizer.zero_grad()
            outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
            outputs.loss.backward()
            optimizer.step()
            total_loss += outputs.loss.item() * input_ids.size(0)
            n += input_ids.size(0)
        return total_loss / n

    def evaluate_model(model, data_loader, dev='cpu', metric=None):
        model.eval()
        for batch in tqdm(data_loader):
            input_ids = batch['input_ids'].to(dev)
            attention_mask = batch['attention_mask'].to(dev)
            labels = batch['labels'].to(dev)
            with torch.no_grad():
                outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            preds = outputs.logits.argmax(dim=-1)
            metric.add_batch(predictions=preds.cpu(), references=labels.cpu())
        return metric.compute()['accuracy']

    x_train, y_train, x_test, y_test = get_data(categories=category_dict.keys(), portion=portion)

    # Parameters
    dev = torch.device('cuda' if torch.cuda.is_available()
                       else ('mps' if torch.backends.mps.is_available() else 'cpu'))
    num_labels = len(category_dict)
    epochs = 3
    batch_size = 16
    learning_rate = 5e-5

    # Model, tokenizer, and metric
    torch.manual_seed(42)
    model = AutoModelForSequenceClassification.from_pretrained('distilroberta-base', num_labels=num_labels).to(dev)
    tokenizer = AutoTokenizer.from_pretrained('distilroberta-base')
    metric = evaluate.load("accuracy")

    # Datasets and DataLoaders
    train_dataset = Dataset(tokenizer(x_train, truncation=True, padding=True), y_train)
    val_dataset = Dataset(tokenizer(x_test, truncation=True, padding=True), y_test)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)

    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
    train_losses, val_accs = [], []
    for epoch in range(1, epochs + 1):
        avg_loss = train_epoch(model, train_loader, optimizer, dev=dev)
        acc = evaluate_model(model, val_loader, dev=dev, metric=metric)
        train_losses.append(avg_loss)
        val_accs.append(acc)
        print(f'Epoch {epoch:02d} | train loss {avg_loss:.4f} | val acc {acc:.4f}')
    return train_losses, val_accs


if __name__ == "__main__":
    portions = [0.1, 0.2, 0.5, 1.]
    # Q1 - single layer MLP
    pass

    # Q2 - multi-layer MLP
    pass

    # Q3 - Transformer
    print("\nTransformer results:")
    for p in portions[:2]:
        print(f"Portion: {p}")
        transformer_classification(portion=p)
