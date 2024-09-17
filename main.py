from PIL import Image, ImageDraw
import math

# ASCII CHARACTER MAP
chars = ".'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

char_width = 10
char_height = 10

def getLuminosity(pixel):
    """Calculate luminosity of the pixel"""
    return math.floor(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])

def avgRGB(pixel):
    """Calculate average RGB value."""
    return math.floor((pixel[0] + pixel[1] + pixel[2]) / 3)

def resizeImage(image, new_width=100):
    """Resize image while maintaining aspect ratio."""
    width, height = image.size
    aspect_ratio = width / height
    new_height = int(new_width / aspect_ratio)
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

def imageToAscii(image, draw):
    """Convert image to ASCII art and draw it on a new image."""
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            luminosity = getLuminosity(pixel)
            ascii_index = luminosity * (len(chars) - 1) // 255
            asciiPixel = chars[ascii_index]
            draw.text((x * char_width, y * char_height), asciiPixel, fill=pixel)

def main(Image_width=100):
    """Main function to handle image processing and ASCII art creation."""
    image_path = input("Enter Valid Image Path:\n")
    
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Invalid Image Path: {e}\n")
        return
    
    # Convert image to RGB and resize
    image = image.convert("RGB")  # Ensure the image is in RGB mode
    image = resizeImage(image, Image_width)
    width, height = image.size

    # Create a new image for drawing ASCII art with a bright background
    ascii_img = Image.new("RGB", (width * char_width, height * char_height), color=(0, 0, 0))
    draw = ImageDraw.Draw(ascii_img)

    # Convert image to ASCII
    imageToAscii(image, draw)

    # Save the new image
    outputname = image_path.split(".")[0] + "_ascii_image.png"
    ascii_img.save(outputname)

    print(f"ASCII image saved as {outputname}")

if __name__ == "__main__":
    main()
