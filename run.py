import argparse

from helpers.logger import create_logger
from data.preprocessing import preprocess_data, download_data
from model.model import train_model

"""
Main running script:
    - For downloading data run:     python run.py -dd=True
    - For preprocessing data run:   python run.py -dp=True
    - for training run:             python run.py -dt=True
        - model:                        -mo, --use_model    Options: ['model1', 'model2'], default='model1'
        - data:                         -da, --use_data     Options: ['all'], default='?'
        - training query structures:    -ts, --train_str    Options: ['all'], default='?'
        - num hyperplanes:              -hy, --num_hyp      Default=16
        - num buckets:                  -bk, --num_buck     Default=4
        - aggregation function          -ag, --agg_func     Options: ['?'], default='?'
        - loss function                 -ls, --loss_func    Options: ['?'], default='?'
        - learning rate                 -lr, --learn_rate   Default=1e-5
        - eval query structures:        -es, --eval_str     Options: ['all'], default='?'
"""

def main(config):

    logger = create_logger(config)
    logger.info(config)

    if config.do_download:
        download_data(logger)

    if config.do_preprocess:
        preprocess_data(config, logger)

    if config.do_train:
        train_model(config, logger)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # logging
    parser.add_argument('-l', '--log', type=bool, default=True, help="Save log to ../logs (default: True)")
    
    # downloading
    parser.add_argument('-dd', '--do_download', type=bool, default=False, help="If raw data needs to be downloaded (default: False)")
    
    # preprocessing
    parser.add_argument('-dp', '--do_preprocess', type=bool, default=False, help="If raw data needs to be preprocessed (default: False)")
    
    # training
    parser.add_argument('-dt', '--do_train', type=bool, default=False, help="If raw data needs preprocessing (default: False)")
    parser.add_argument('-m', '--use_model', type=str, default='test', help="Model used for training (default: test)")
    

    args = parser.parse_args()
    main(args)
