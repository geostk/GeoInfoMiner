#-*-coding:UTF-8-*-
"""
k-nearest neighbors classifier.

This file contains the basic implementation of the k-nearest neighbors 
algorithm on Landsat 8 data.

"""
# Authors: Jingge Xiao <jingge.xiao@gmail.com>
#
# Created on Fri Jul 28 10:21:50 2017


from sklearn.neighbors import KNeighborsClassifier
import sys

#Set the path of source files
sys.path.append(r'E:\Research\basic\github\GeoInfoMiner\code')
import utils

# If you have modified the "utils" file, then these two lines of code must be executed
from imp import reload
reload(utils)

# set the path of training samples
train_file_path = r'E:\Research\basic\github\GeoInfoMiner\data\training_sample.csv'

# set the path of image that is going to be classified
imagery_path = r'E:\Research\basic\github\GeoInfoMiner\data\image_sample.tif'

# set the path where to output the final classified image
class_file_path = r'E:\Research\basic\github\GeoInfoMiner\data\KNeighbors_class.tif'

# set the number the neighbours in k-NN
n_neighbors=15


# get all data ready for training and predicting
x_s, y_s, rows, cols, data_frame = utils.prepare_data(imagery_path, train_file_path)

# train the classifier
clf_KNeighbors = KNeighborsClassifier(n_neighbors = n_neighbors, weights='distance')
clf_KNeighbors.fit(x_s, y_s)

# predict lables based on image data
z_ps=clf_KNeighbors.predict(data_frame)

# output the classification result
utils.output_lables_to_tif(z_ps, class_file_path, rows, cols)