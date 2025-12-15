import os


WEIGHTS_DOWNLOAD_URL = "https://drive.usercontent.google.com/download?id=1wjOF9MWkrVJVo5uG3gVqZEW9pwRq_aIk&export=download&authuser=0&confirm=t&uuid=41f7a129-b788-4036-9535-fe93ca2789d0&at=ALWLOp5SvjCiSxZOmeZvSagKzp-h%3A1765787138684"
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
WEIGHTS_DIR = os.path.join(ROOT_DIR, 'weights')
WEIGHTS_FILE = os.path.join(WEIGHTS_DIR, 'geco_pretrained.pth')
