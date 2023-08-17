from PIL import Image, ImageChops

# # Load the images
# img1 = Image.open('flag.png').convert('L')
# img2 = Image.open('lemur.png').convert('L')

# # Ensure the images have the same dimensions
# assert img1.size == img2.size

# # Create a new image with the same size as the input images
# result = Image.new('L', img1.size)

# # Iterate over each pixel and perform the XOR operation
# for x in range(img1.width):
#     for y in range(img1.height):
#         pixel1 = img1.getpixel((x, y))
#         pixel2 = img2.getpixel((x, y))
#         result.putpixel((x, y), pixel1 ^ pixel2)

# # Save the result as a new image
# result.save('result.png')

## better code. 
img1 = Image.open('lemur.png')
img2 = Image.open('flag.png')

img3 = ImageChops.add(ImageChops.subtract(img2,img1), ImageChops.subtract(img1,img2))
img3.save("img3.png")