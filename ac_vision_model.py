from fastai.data.all import *
from fastai.vision.all import *
from fastai.metrics import error_rate
import pathlib
from IPython.display import Image
import re

path = ("images/")  # define path to parent images folder
file_names = get_image_files(path)

datablock = DataBlock()

datasets = datablock.datasets(file_names)

datablock = DataBlock(get_items=get_image_files)


def label_func(l): re.sub(r'_[^_]+$', '', l)

dls = ImageDataLoaders.from_name_func(path, file_names, label_func, item_tfms=Resize(224))

dls.show_batch()