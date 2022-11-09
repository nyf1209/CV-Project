# CV-Project
Computer Vision final project


Fall 2022 Computer Vision Project

Title: Facial Expression Detection based on Different ImageNet
Group Members: Yifeng Ni, Zuhua Cao, Hengning Rao

Project description and goals:
The goal of this project is to explore different kinds of ImageNet that are used to train the
deep learning model in the area of facial expression detection. The main idea is that we can
use our program to identify a human's facial expression by input such as Laugh, Angry, Sad and
so on. We Find that VGG and ResNet are two popular models that are used in facial expression
detection so we want to compare those two methods by analyzing the running time , parameter
tuning and running time of them.
The minimum goal is to implement two typical ImageNet from VGG and ResNet such as
VGG-16 and ResNet-18 on images of facial expression. The maximum goal is to explore other
more powerful ImageNets that can improve the performance of facial expression detection. We
can also make facial expressions detection into a real time detection in video instead of an
image and other interesting implementations such as replacing people’s faces with correct
emoji.

Member roles:
1. Build up suitable VGG ImageNet, parameter tuning and train the dataset
2. Build up suitable ResNet ImageNet,parameter tuning and train the dataset
3. Image preprocessing and postprocessing , analyze and visualize the result of facial
expression detection

Resources:
The data we would utilize is FER2013.The data consists of 48x48 pixel grayscale images
of faces. The faces have been automatically registered so that the face is more or less centered and
occupies about the same amount of space in each image. There are seven categories of facial
expression. (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral). The training set
consists of 28,709 examples and the public test set consists of 3,589 examples.

Here are the examples of our images:
We will train and test our model’s performance in the Jupyter Notebook using Python. Currently,
we may need some outsource code about VGG ImageNet and ResNet ImageNet. We would do
more extension performance tests and training for analyzing the differences. Also, this
large-scale dataset could fulfill our need of adequate computational resources.
The link to the resource: https://www.kaggle.com/datasets/msambare/fer2013?select=test

Reservations:
Firstly, the test results may not meet the expectations. It is necessary to continuously
experiment and adjust the parameters. Secondly, the selected data set may not be suitable, and
different data sets need to be replaced for multiple experiments. Besides, there are also various
situations that require special handling when writing code. Our minimum goal is to implement
two typical ImageNet from VGG and ResNet such as VGG-16 and ResNet-18 on images of
facial expression.

Relationship to your background:

Yifeng Ni: I’m a graduate from ECEMeng Program.I am already familiar with the python package to
process the images such as Pillow, Skimage and Scipy. Previously, I didn't have any experience in either
deep learning or Image Processing before. So this project is my first time to learn how to use deep
learning to solve the problem of image processing. I haven’t used any deep learning libraries before such
as TensorFlow and PyTorch. So this project is an opportunity for me to learn how to use these powerful
tools and learn about algorithms of different popular models(VGG,ResNet) that are used in the area of
face recognition.

Zuhua Cao: As a MCS student, I’ve taken CS445 in the previous semester. Thus, I may have some
relative experience about processing images. Also, I’ve done a final project about black and white image
colorizing based on the GAN model. Though this project is my first time learning facial expression
detection, it really attracts me and I believe that I could devote myself to building models and to make
analysis about the results.

Hengning Rao: I’m an ECE Meng student. I have some research experience in building models to deal
with deep learning problems, and I’ve participated in some projects about natural language processing
and graph embedding before. This is my first project of computer vision. I’m excited about it and I believe
I can learn a lot from it.
