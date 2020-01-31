<h1>Understanding Clouds from Satellite Images</h1>
<h2>PROBLEM DESCRIPTION & MOTIVATION</h2>
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
