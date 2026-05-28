import random
from collections import defaultdict

import nltk
from nltk.corpus import dependency_treebank


def load_data():
    nltk.download('dependency_treebank', quiet=True)
    sentences = dependency_treebank.parsed_sents()
    split = int(len(sentences) * 0.9)
    train = sentences[:split]
    test = sentences[split:]
    return train, test


feature_index = {}

def get_index(key):
    if key not in feature_index:
        feature_index[key] = len(feature_index)
    return feature_index[key]

def feature_function(u, v):
    u_word = u['word'] if u['address'] != 0 else 'ROOT'
    u_tag  = u['tag']  if u['address'] != 0 else 'ROOT'
    v_word = v['word']
    v_tag  = v['tag']
    word_key = ('W', u_word, v_word)
    pos_key  = ('P', u_tag, v_tag)
    return [get_index(word_key), get_index(pos_key)]


def edge_features(g, edges):
    feats = defaultdict(int)
    for u_addr, v_addr in edges:
        for idx in feature_function(g.nodes[u_addr], g.nodes[v_addr]):
            feats[idx] += 1
    return feats


def gold_edge_features(g):
    edges = [(node['head'], addr)
             for addr, node in g.nodes.items() if addr != 0]
    return edge_features(g, edges)


def train(train_sents, infer, n_iterations=2, lr=1.0):
    weights = defaultdict(float)
    weights_sum = defaultdict(float)
    total_steps = 0

    for _ in range(n_iterations):
        order = list(range(len(train_sents)))
        random.shuffle(order)
        for i in order:
            g = train_sents[i]

            pred_edges = infer(g, weights)  # list of (u_addr, v_addr)
            pred_feats = edge_features(g, pred_edges)
            gold_feats = gold_edge_features(g)

            for idx in set(gold_feats) | set(pred_feats):
                weights[idx] += lr * (gold_feats[idx] - pred_feats[idx])

            for idx, val in weights.items():
                weights_sum[idx] += val
            total_steps += 1

    return {idx: s / total_steps for idx, s in weights_sum.items()}
