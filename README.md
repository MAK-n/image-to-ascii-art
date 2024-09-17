# Image TO ASCII Art

This project provides a Python script to convert images into ASCII art. It uses the Python Imaging Library (PIL), now known as Pillow, to handle image processing and text drawing.


- Converts images to ASCII art.
- Maintains aspect ratio of the original image.
- Customizable ASCII character set.
- Outputs the ASCII art to a PNG image file.


## Requirements

- Python 3.x
- Pillow library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/ascii-art-image-converter.git
   cd ascii-art-image-converter
   ```

2. **Install the required libraries:**

   ```sh
   pip install Pillow
   ```

## How to use

1. **Run the script:**

   ```sh
   py ascii_art_converter.py
   ```

2. **Enter the path to the image file.**

   The script will:
   - Open the image.
   - Resize it while maintaining the aspect ratio.
   - Convert the image to ASCII art.
   - Save the resulting ASCII art image as a PNG file in the same directory as the input image.

   The output file will be named `<original_image_name>_ascii_image.png`.

## Customization

- **Character Set:**
  
  The `chars` variable in the script defines the set of ASCII characters used for rendering. You can modify this string to use different characters based on your preferences.

- **Character Size:**
  
  The `char_width` and `char_height` variables control the size of each ASCII character in the output image. Adjust these values to change the appearance of the ASCII art.

## Example

For an example of how the output looks, check out the [image](link-to-image).

