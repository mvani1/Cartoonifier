# Cartoonifier
Problem Statement
You are given a picture of a person or an animal and must manipulate it so it appears
cartoonish, as if from a comic book.

Solution
A cartoonish image has two characteristic features- homogeneous colors and thick,
defining edges. In this project, we go about the process of cartoonifying this way:

● Convert the image into grayscale

● Blur it

● Extract the edges

● Blur the colored version of the image

● Add a mask with the edges


We make use of OpenCV (cv2) to implement this functionality:

➔ imread() reads an image.

➔ cvtColor() helps convert it from one color space to another (In cv2, this is BGR because
the bytes are reversed).

➔ medianBlur() blurs and smoothes an image using the median filter. This filter takes the
median of all pixels under the kernel area and replaces the central element with its
median value. Here, ksize is the aperture linear size; it has to be odd and greater than 1.
A higher ksize leads to a more blurred image.

➔ adaptiveThreshold() helps us get the edges. In simple threshold, one threshold value is
used for the entire image. But here, different threshold values are calculated for smaller
regions. A pixel is assigned a value depending on whether its value is greater or lesser
than the threshold value.

◆ 255 is the maxValue used to assign a value to pixels satisfying the condition
(white).

◆ ADAPTIVE_THRESH_MEAN_C is the adaptive thresholding algorithm to use.

◆ THRESH_BINARY is the threshold type- this can be THRESH_BINARY or
THRESH_BINARY_INV.

◆ 9 is the blocksize- the size of the pixel neighborhood used to calculate threshold
value for a pixel. This can be 3, 5, 7,..

◆ 9 is C- the constant subtracted from the mean or the weighted mean.

➔ bilateralFilter() applies the bilateral filter to the image. This is a non-linear,
edge-preserving, and noise-reducing smoothing filter for images. It replaces the intensity
of each pixel with a weighted average of the intensity values from nearby pixels. It also
reduces unwanted noise while keeping the edges rather sharp.

◆ 9 is d- the diameter of each pixel neighborhood used for filtering.

◆ 300 and 300 are sigmaColor and sigmaSpace; higher sigma values make the
image look more cartoonish.

➔ bitwise_and() calculates the per-element bitwise conjunction of two arrays. So here, it
conjugates color with itself and optionally applies an operation mask to it- this is an 8-bit
single channel array.

➔ Finally, we return this.

We also use tkinter to build a brief GUI to support this project.
