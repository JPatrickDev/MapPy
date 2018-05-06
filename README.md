# MapPy
A Python library for generating Map Charts

## Dependencies
MapPy depends on [Pillow](https://pillow.readthedocs.io/en/5.1.x/) to run.

## Currently Supported Maps
Currently there are two maps included: A map of the UK and a map of England split in to the statistical regions.

New maps are always welcome, the format is pretty simple. map.json and map.png are an example of how to make your own.



## Different Sizes
Currently the program has limited support for different sizes. It will resize the scale/title images and boxes, but the text will always be the same size. You can use "\n" characters in your text to force newlines.

## Output
MapPy can generate charts as show in the file "finished.png", which was made entirely using MapPy

## Usage
1. Edit "resources/config.json" as required. Please see the next section for details.
2. Run main.py
3. Input the name of the map you want to load
    1. Not including any file extesions - Example: input "map" for the files map.png and map.json
4. Input your values for each map section
5. Input your title, subtitle and scale caption
6. Once the program exits, the file "output.png" should contain your finished chart.

## config.json
The config.json file(Found in the resources folder) is used to specify settings for MapPy to use when run.

"startColor" : The Color for the minimum scale value - "R,G,B" (0-255)

"endColor" : The Color for the maximum scale value - "R,G,B" (0-255)

"max" : The "resolution" of the gradient used to convert values to color.A smaller number here will make small differences in values be more obvious on the map

"scaleMin" : The minimum number on the scale

"scaleMax" : The maximum number on the scale

"fontSize" : The size of the font to use for the labels.
