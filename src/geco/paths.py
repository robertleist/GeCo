import os


GECO_WEIGHTS_DOWNLOAD_URL = "https://drive.usercontent.google.com/download?id=1wjOF9MWkrVJVo5uG3gVqZEW9pwRq_aIk&export=download&authuser=0&confirm=t&uuid=41f7a129-b788-4036-9535-fe93ca2789d0&at=ALWLOp5SvjCiSxZOmeZvSagKzp-h%3A1765787138684"
SAM_HQ_WEIGHTS_DOWNLOAD_URL = "https://drive.usercontent.google.com/download?id=1qobFYrI4eyIANfBSmYcGuWRaSIXfMOQ8&export=download&authuser=0&confirm=t&uuid=cf79c218-c8b5-45d4-a871-a558ac7ca00d&at=ALWLOp50K4vjEga7Hl8xIa_xD8r4%3A1765875026054"
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
WEIGHTS_DIR = os.path.join(ROOT_DIR, 'weights')
GECO_WEIGHTS_FILE = os.path.join(WEIGHTS_DIR, 'geco_pretrained.pth')
SAM_HQ_WEIGHTS_FILE = os.path.join(WEIGHTS_DIR, 'sam_hq_weights.pth')