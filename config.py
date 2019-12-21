# -*- coding: utf-8 -*-

GPU_ID = 0
TRAIN_BATCH_SIZE = 64
TEST_BATCH_SIZE = 32
EXTRACT_BATCH_SIZE = 128
TEST_BATCH_COUNT = 30
NUM_WORKERS = 4
LR = 0.001
MOMENTUM = 0.5
EPOCH = 10
DUMPED_MODEL = "model_10_final.pth.tar"

LOG_INTERVAL = 10
DUMP_INTERVAL = 500
TEST_INTERVAL = 100

DATASET_BASE = 'data/'
ENABLE_INSHOP_DATASET = False
INSHOP_DATASET_PRECENT = 0.8
IMG_SIZE = 256
CROP_SIZE = 32
IMG_CHANNELS = 3
INTER_DIM = 512
CATEGORIES = 20
N_CLUSTERS = 50
COLOR_TOP_N = 10
TRIPLET_WEIGHT = 2.0
ENABLE_TRIPLET_WITH_COSINE = False  # Buggy when backward...
COLOR_WEIGHT = 0.1
DISTANCE_METRIC = ('euclidean', 'euclidean')
FREEZE_PARAM = False