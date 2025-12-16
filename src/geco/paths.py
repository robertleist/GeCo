import os


GECO_WEIGHTS_DOWNLOAD_URL = "https://drive.usercontent.google.com/download?id=1wjOF9MWkrVJVo5uG3gVqZEW9pwRq_aIk&export=download&authuser=0&confirm=t&uuid=a4f37f00-2a60-4742-8b2e-a52c58920523&at=ALWLOp5KGcPa8--3Gu7NfVmv5fia%3A1765876649194"
SAM_HQ_WEIGHTS_DOWNLOAD_URL = "https://drive.usercontent.google.com/download?id=1qobFYrI4eyIANfBSmYcGuWRaSIXfMOQ8&export=download&authuser=0&confirm=t&uuid=cf79c218-c8b5-45d4-a871-a558ac7ca00d&at=ALWLOp50K4vjEga7Hl8xIa_xD8r4%3A1765875026054"
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
WEIGHTS_DIR = os.path.join(ROOT_DIR, 'weights')
GECO_WEIGHTS_FILE = os.path.join(WEIGHTS_DIR, 'geco_pretrained.pth')
SAM_HQ_WEIGHTS_FILE = os.path.join(WEIGHTS_DIR, 'sam_hq_weights.pth')