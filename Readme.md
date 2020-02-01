<h1>Understanding Clouds from Satellite Images</h1>
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

<h3>REFERENCES</h3>
<li> He, K., Gkioxari, G., Dollár, P., & Girshick, R. (2017). Mask r-cnn. In Proceedings of the
IEEE international conference on computer vision (pp. 2961-2969)</li>
<li> Ronneberger, O., Fischer, P., & Brox, T. (2015, October). U-net: Convolutional networks
for biomedical image segmentation. In International Conference on Medical image
computing and computer-assisted intervention (pp. 234-241). Springer, Cham</li>
<li> https://wiki.ubc.ca/CNNs_in_Image_Segmentation</li>
<li>Rasp, S., Schulz, H., Bony, S., & Stevens, B. (2019). Combining crowd-sourcing and deep
learning to understand meso-scale organization of shallow convection. arXiv preprint
arXiv:1906.01906</li>
<li>Zantedeschi, V., Falasca, F., Douglas, A., Strange, R., Kusner, M. J., & Watson-Parris, D.
(2019). Cumulo: A Dataset for Learning Cloud Classes. arXiv preprint arXiv:1911.04227</li>
<li>https://www.kaggle.com/c/understanding_cloud_organization/data#_=_</li>
<li>Segmentation models: https://github.com/qubvel/segmentation_models</li>
<li> Mask RCNN: https://github.com/matterport/Mask_RCNN</li>
<li> https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-andtensorflow-
7c761e238b46</li>
