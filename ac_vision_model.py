from fastai.data.all import *
from fastai.vision.all import *
from fastai.metrics import error_rate
import pathlib
from IPython.display import Image

path = ("images/") #define path to parent images folder
file_names = get_image_files(path)
print(len(file_names))
print(file_names[0])

def label_prepper(file_names):
	for file in file_names:
		file =

datablock = DataBlock()

datasets = datablock.datasets(file_names)

datablock = DataBlock(get_items=get_image_files)







