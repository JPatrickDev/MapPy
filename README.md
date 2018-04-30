# MapPy
A Python library for generating Map Charts

## Dependencies
MapPy depends on [Pillow](https://pillow.readthedocs.io/en/5.1.x/) to run.

## Currently Supported Maps
Currently, the only map provided is the map of the UK split up in to the top level regions used for statistics. 
New maps are always welcome, the format is pretty simple. map.json and map.png are an example of how to make your own.



## Different Sizes
Currently the program has limited support for different sizes. It will resize the scale/title images and boxes, but the text will always be the same size. You can use "\n" characters in your text to force newlines.

## Output
MapPy can generate charts as show in the file "finished.png", which was made entirely using MapPy

## Usage
(Better tutorial is coming soon)
1. Edit "resources/config.json" as required
2. Run main.py
3. Input the name of the map you want to load
    1. Not including any file extesions - Example: input "map" for the files map.png and map.json
4. Input your values for each map section
5. Input your title, subtitle and scale caption
6. Once the program exits, the file "output.png" should contain your finished chart.