from fastai.data.all import *
from fastai.vision.all import *
from fastai.metrics import error_rate
from pathlib import Path
from IPython.display import Image

path = Path("images")
fnames = get_image_files(path)

datablock = DataBlock()

datasets = datablock.datasets(fnames)

datablock = DataBlock(get_items = get_image_files)





