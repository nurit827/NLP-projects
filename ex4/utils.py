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
