import os, sys

"""
Script that orchestrates the preprocessing: sampling and saving queries
of different structures from the raw graphs. Based on Hamilton et al. (2018).
"""

# Set main folder as working directory
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

from data.data_utils import (
    make_train_test_edge_data,
    make_train_queries,
    make_test_queries,
    clean_test_queries,
    discard_negatives
)

DATA_DIR = "./data/graphs/"
DATASETS = ['BIO'] #['AIFB', 'MUTAG', 'AM', 'BIO']


def download_data(logger):
    for dataset in DATASETS:
        logger.info(f"Downloading {dataset} dataset...")
        # to implement!
    return


def preprocess_data(config, logger):
    for dataset in DATASETS:
        logger.info(f"Preprocessing {dataset} dataset...")
        preprocess_single_dataset(config, logger, dataset)
    return


def preprocess_single_dataset(config, logger, dataset):
    data_folder = f"{DATA_DIR}/{dataset}/processed/"
    make_train_test_edge_data(data_folder)
    make_train_queries(data_folder)
    make_test_queries(data_folder)
    clean_test_queries(data_folder)
    discard_negatives(data_folder)
    return

