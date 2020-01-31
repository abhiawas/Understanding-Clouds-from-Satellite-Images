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
