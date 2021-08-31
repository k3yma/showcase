# Dicify

Dicify is a python script to turn an image into a dice collage. I originally created this in response to a question on reddit so thought I'd share it with the wider community.

## Usage

```bash
python3 dicify [options] source_file
```

## Options
```bash
usage: dicify.py [-h] [-d DiceSize] [-x MaxWidth] [-y MaxHeight] source

Convert a picture into Dice

positional arguments:
  source        Source image file

optional arguments:
  -h, --help    show this help message and exit
  -d DiceSize   Dice size
  -x MaxWidth   Maximum Width in Dice
  -y MaxHeight  Maximum Height in Dice
```

## Example
Input image.
![input_image](./boris.jpg?raw=true)

Output image.
![output](./output.png?raw=true)
