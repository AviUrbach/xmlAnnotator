# xmlAnnotator
CSci 435 Programming assignment #1

The python script takes pairs of files, one xml and one png, and outputs an annotated png file for each input pair in which each leaf node GUI element has a red box around it.

> How to Run

To set up required modules, run "pip install -r requirements.txt"

To use the annotator, run the python script annotate.py, giving the path to the input files as the first argument. For example, "python annotate.py C:\Users\aviku\Downloads\Programming-Assignment-Data"

On my computer, the code approximately 30 seconds to process all of the provided input.

Output images are stored as "[image_name]_output.png" in a folder "output" in the working directory.

> Solution Design

The code goes through the input xml files, loads the corresponding png image, then finds each leaf node in the xml file. For each leaf node, it gets the bound of the node from the xml file and draws a box around the bounds on the loaded png. It then writes the png to the output folder.

I decided to use the pypng library as it seemed the most natural way to load, edit, and save png files specifically. I used the numpy library to make the png editing simpler. For string parsing, I decided to write my own parsing from scratch as I only needed to look for a few specific things. I used the find method a lot and made sure to not create slices with each search for runtime efficiency. I admit that my string parsing code is not elegant, and if I were to do this again I would probably try a different approach. To draw the boxes, the code simply processes from the lower to the upper bound, first in x then in y, filling in each pixel as it goes.