import cv2
import random
import numpy as np
import os


'''
0 = Anger
1 = Disgust
2 = Fear
3 = Happiness
4 = Sadness
5 = Surprise
6 = Neutral
'''
# prepossing the image 
def transform_img(img):
    img = cv2.resize(img, (224, 224))
    img = np.transpose(img, (2,0,1))
    img = img.astype('float32')
    
    img = np.clip(img, 0, 255.0)
    img = img / 255
    #mg = np.clipimg * 2.0 - 1.0
    return img

# define data reader 
def data_loader(datadir, batch_size=100, mode = 'train'):
    filenames = os.listdir(datadir)
    def reader():
        if mode == 'train':
            #shuffle the data
            random.shuffle(filenames)
        batch_imgs = []
        batch_labels = []
        for name in filenames:
            filepath = os.path.join(datadir, name)
            img = cv2.imread(filepath)
            img = transform_img(img)
            
            #read happy file 
            if name[0] == 'H':
                label = 1
            else:
                raise('Other File')
                   
            batch_imgs.append(img)
            batch_labels.append(label)
            if len(batch_imgs) == batch_size:
                imgs_array = np.array(batch_imgs).astype('float32')
                labels_array = np.array(batch_labels).reshape(-1, 1)
                yield imgs_array, labels_array
                batch_imgs = []
                batch_labels = []

        if len(batch_imgs) > 0:
            imgs_array = np.array(batch_imgs).astype('float32')
            labels_array = np.array(batch_labels).reshape(-1, 1)
            yield imgs_array, labels_array

    return reader


def valid_data_loader(datadir, batch_size=100, mode='valid'):
    filenames = os.listdir(datadir)
    def reader():
        batch_imgs = []
        batch_labels = []
            
        for name in filenames:
            filepath = os.path.join(datadir, name)
            img = cv2.imread(filepath)
            img = transform_img(img)
            
            
            if name[0] == 'H':
                label = 1
            
            else:
                raise('Other File')
           
            batch_imgs.append(img)
            batch_labels.append(label)
            if len(batch_imgs) == batch_size:
                imgs_array = np.array(batch_imgs).astype('float32')
                labels_array = np.array(batch_labels).reshape(-1, 1)
                yield imgs_array, labels_array
                batch_imgs = []
                batch_labels = []

        if len(batch_imgs) > 0:
            imgs_array = np.array(batch_imgs).astype('float32')
            labels_array = np.array(batch_labels).reshape(-1, 1)
            yield imgs_array, labels_array

    return reader



#test data loader
DATADIR = 'train'
train_loader = data_loader(DATADIR,batch_size=20, mode='train')
data_reader = train_loader()
data = next(data_reader) 
#print("train mode's shape:")
#print("data[0].shape = %s, data[1].shape = %s" %(data[0].shape, data[1].shape))

eval_loader = data_loader(DATADIR,batch_size=20, mode='eval')
data_reader = eval_loader()
data = next(data_reader)
#print("eval mode's shape:")
#print("data[0].shape = %s, data[1].shape = %s" %(data[0].shape, data[1].shape))