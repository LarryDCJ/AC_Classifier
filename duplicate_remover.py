import hashlib
import os
import PIL
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
import matplotlib.gridspec as gridspec
import time
import numpy as np

from pathlib import Path

def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return md5(f.read()).hexdigest()

os.chdir('/Users/larrydcj/Documents/Programming/Projects/AC_Classifier/images')

duplicates = []
hash_keys = dict()
folders = os.listdir('/Users/larrydcj/Documents/Programming/Projects/AC_Classifier/images')

for folder in folders:
    if Path(f'/Users/larrydcj/Documents/Programming/Projects/AC_Classifier/images/{folder}').is_dir():
        os.chdir(f'/Users/larrydcj/Documents/Programming/Projects/AC_Classifier/images/{folder}')
        for index, filename in enumerate(os.listdir('.')):
            if os.path.isfile(filename):
                with open(filename, 'rb') as f:
                    filehash = hashlib.md5(f.read()).hexdigest()
                    if filehash not in hash_keys:
                        hash_keys[filehash] = index
                    else:
                        duplicates.append((index,hash_keys[filehash]))

print(duplicates)
#for file_indexes in duplicates[:30]:
#    try:
#
#        plt.subplot(121), plt.imshow(imread(duplicates[file_indexes[1]]))
#        plt.title(file_indexes[1]), plt.xticks([]), plt.yticks([])
#
#        plt.subplot(122), plt.imshow(imread(duplicates[file_indexes[0]]))
#        plt.title(str(file_indexes[0]) + ' duplicate'), plt.xticks([]), plt.yticks([])
#        plt.show()
#
#   except OSError as e:
#       continue


for index in duplicates:
    os.remove(duplicates[index[0]])