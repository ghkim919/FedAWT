import numpy as np
import os
# import tensorflow as tf
import random
import csv
from tqdm import tqdm
import random
from scipy.stats import betabinom
import argparse
from config_reader import ConfigReader

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulation Main")
    parser.add_argument('--config', type=str, required=True, help='Config 파일 경로')
    args = parser.parse_args()

    config_path = args.config
    config = ConfigReader(config_path).read()
    print("Loaded config:", config)
    # ...existing code...