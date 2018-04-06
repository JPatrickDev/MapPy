#MapPy
A Python library for generating Map Charts

## Dependencies
MapPy depends on Pillow to run.

##Currently Supported Maps
Currently, the only map provided is the map of the UK split up in to the top level regions used for statistics. 
New maps are always welcome, the format is pretty simple. map.json and map.png are an example of how to make your own.
Currently you will have to edit the source before running the program to change which file is used, or replace the existing map.json and map.png with your own versions in the same format. 
##Different Sizes
Currently the program has limited support for different sizes. It will resize the scale/title images and boxes ,but the text will always be the same size. You can use "\n" characters in your text to force newlines. 

##Output
MapPy can generate charts as show in the file "finished.png", which was made entirely using MapPy