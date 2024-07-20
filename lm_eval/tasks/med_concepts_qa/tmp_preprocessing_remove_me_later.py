import os

import datasets


def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    if len(dataset) > 5:
        return dataset.shuffle(seed=int(os.environ["DATA_SEED"]))
    else:
        return dataset