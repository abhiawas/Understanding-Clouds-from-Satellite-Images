<h1>Understanding Clouds from Satellite Images</h1>
<img src="https://github.com/abhiawas/Understanding-Clouds-from-Satellite-Images/blob/master/resources/img1.JPG">
<h3>PROBLEM DESCRIPTION & MOTIVATION</h3>
<p>Climate change has been at the top of our minds and there are many ways in which clouds can
organize, but the boundaries between different forms of organization are not fully explained.
This makes it challenging to build traditional rule-based algorithms to separate cloud features to
better understand the clouds. Shallow clouds play a huge role in determining the Earth's climate
and they are difficult to understand and to represent in climate models. In this Project we will be
identifying regions in satellite images that contain certain cloud formations shown below, with
label names: Fish, Flower, Gravel and Sugar. The segment for each cloud formation label for an
image is encoded into a single row, even if there are several non-contiguous areas of the same
formation in an image. Each image has at least one cloud formation, and can possibly contain up
to all four. Stating the above we can consider this as a multiclass segmentation task which is
finding 4 different patterns in the images. Since, we make predictions for each pair of image and
segmentation mask(label) separately, this could be treated as a 4 binary segmentation problem.
In order to solve this task, we decided to implement two deep learning segmentation models
Mask Region based Convolution neural network(Mask-RCNN) and UNET</p>
<img src="https://github.com/abhiawas/Understanding-Clouds-from-Satellite-Images/blob/master/resources/img2.JPG">

<h3>Data Acquisition</h3>
<p>Data set has been taken from kaggle competition “Understanding Clouds from Satellite
Images” which is acquired by NASA Worldwide. Data set can be found
https://www.kaggle.com/c/understanding_cloud_organization/data</p>

<h3>EDA and Preprocessing</h3>
<ul>
  <li>The experimental data considered in this project consists of a „train_images‟ folder which
has the 5546 training images with size 2100*1400 and a train.csv file containing the run
length encoded segmentations for each image-label pair in the „train_images‟.</li>
  <li>We have total 22184 Image labels (segmentation masks) and while looking for null values
,we observed that 10348 rows don‟t have encoded pixels i.e. they have
empty segmentation maps, as a result we have deleted those data entries and will be
working with 11836 image labels.</li>
  <li>Counting the number of labels of each cloud type we found that there are 2781
of Fish, 2365 of Flower, 2939 of Gravel and 3751 of Sugar observations respectively. From
the plots below we can see that the dataset is somewhat balanced making the task a bit
easier.</li>
  <li>We wanted to see the number of mask labels per image and observed that 2372 Images
which has two classes, 1560 Images with three classes, 266 images with all the four classes
and 1348 with only one mask. We can conclude from figure-6 that most of the times we
have 2 or 3 types of cloud formations in one image, all the 4 types of cloud formation in
one image is very rare. Only one type of cloud formation in the image is also somewhat
common</li>
  <li>In preprocessing after the removal of missing values stated above, we resized the images
into sizes 512*512 and 320*320 and created custom image data generator classes for the
two models(Mask-RCNN and UNET) respectively. We also used a train-validation split
with a ratio of 90:10 for both the models.</li>
</ul>

<h2>Model Selection</h2>
<h3>Mask RCNN</h3>
<p>Mask RCNN is an artificial deep neural network aimed to solve object instance segmentation
problem in machine learning or computer vision. Mask R-CNN efficiently detects objects in
an image while simultaneously generating a high-quality segmentation mask for each instance.
It extends Faster R-CNN by adding a branch for predicting a binary object mask in parallel
with the existing branch for bounding box recognition [1].
There are two stages of Mask R-CNN shown in figure-8. The first stage, called an RPN,
proposes potential regions where there might be objects for a given image. The second stage,
extracts features using ROI Pool from each candidate box(proposed potential regions),
performs classification along with bounding box regression and generates a binary mask for
each ROI. Both stages are connected to an FPN style deep neural network usually termed as
the backbone structure. The backbone is usually a pretrained network like ConvNet, VGG or
ResNet.
In the first stage the RPN scans all the feature maps and proposes regions which may contain
objects. To bind features to its raw image location efficiently the network uses a set of boxes
with predefined locations and scales relative to the image called Anchors. The true masks and
the bounding boxes are assigned to individual anchors according to some preset IoU value.
The RPN uses anchors with different scales bind to different levels of feature map to figure
out where the feature map „should‟ get an object and what size of its bounding box is [3].
In the second stage the regions proposed by the first stage are assigned to several specific
areas of a feature map, scans these areas, and generates object classes, bounding boxes and
masks. This procedure looks similar to RPN, but the difference is that, stage-two uses
ROIAlign to locate the relevant areas of feature map instead of anchors, and there is an
additional branch which generates masks for each object in pixel level (pixel level
classification).</p>
<img src="https://github.com/abhiawas/Understanding-Clouds-from-Satellite-Images/blob/master/resources/img4.JPG">

<h3>U-Net</h3>
<p>The Artificial deep neural network takes the shape of an „U‟ hence termed as U-net. The UNet
architecture for the most part is symmetric and consists of two major parts shown in
Figure-9, the left/down part which is a contracting/downsampling path and the right/up part
which is an expanding/upsampling path.
The contracting path is similar to an encoder and consists of several convolution layers
followed by an activation function(ReLU), batch norm and max-pooling layers. Its purpose is
to capture the context of the input image via a compact feature map in order to perform
segmentation. This coarse contextual information will then be transferred to the upsampling
path by means of skip connections [5]. The encoder part is referred as a backbone of the U-Net
and is usually a pretrained network like VGG, ResNet, InceptionNet, EfficientNet, DenseNet,
etc.
The expanding path is similar to a decoder which consists of deconvolution layers (upsampling)
and concatenation followed by a symmetrical number of convolution layers with an
activation function (ReLU) and batch normalization to that of the encoder part. The decoder
part‟s purpose is to enable precise localization combined with contextual information from the
contracting path. This step is done to retain boundary information (spatial information) despite
down sampling and max-pooling performed in the encoder stage [2].
In general terms the encoder part encodes the input image into feature representation at
multiple different levels and the decoder part semantically projects the discriminative lower
resolution features learnt by the encoder into higher resolution pixel space to get a dense
classification.</p>
<img src="https://github.com/abhiawas/Understanding-Clouds-from-Satellite-Images/blob/master/resources/img5.JPG">
