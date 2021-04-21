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
