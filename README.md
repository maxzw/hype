# TITLE_HERE

Description

### Requirements

We recommend creating a virtual environment, e.g. with `conda`. Use `environment.yml` to install the dependencies:

```
conda env create -f environment.yml
```

### Datasets

Datasets from [BetaE](https://github.com/snap-stanford/KGReasoning) can be downloaded from the following [link](http://snap.stanford.edu/betae/KG_data.zip) After downloading them, unzip them and move them folders to ./data.

Each folder in the data represents a KG, including the following files.
- `train.txt/valid.txt/test.txt`: KG edges
- `id2rel/rel2id/ent2id/id2ent.pkl`: KG entity relation dicts
- `train-queries/valid-queries/test-queries.pkl`: `defaultdict(set)`, each key represents a query structure, and the value represents the instantiated queries
- `train-answers.pkl`: `defaultdict(set)`, each key represents a query, and the value represents the answers obtained in the training graph (edges in `train.txt`)
- `valid-easy-answers/test-easy-answers.pkl`: `defaultdict(set)`, each key represents a query, and the value represents the answers obtained in the training graph (edges in `train.txt`) / valid graph (edges in `train.txt`+`valid.txt`)
- `valid-hard-answers/test-hard-answers.pkl`: `defaultdict(set)`, each key represents a query, and the value represents the **additional** answers obtained in the validation graph (edges in `train.txt`+`valid.txt`) / test graph (edges in `train.txt`+`valid.txt`+`test.txt`)

### Training

From the root directory of the repository, use the following commands to reproduce our experiments...