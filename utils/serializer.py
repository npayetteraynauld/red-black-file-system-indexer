import pickle

def save_trees(*trees, filepath="./data/index.pk1"):
    with open(filepath, "wb") as f:
        pickle.dump(trees, f)
         
def load_trees(filepath="./data/index.pk1"):
    with open(filepath, "rb") as f:
        return pickle.load(f)
