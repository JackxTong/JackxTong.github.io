from PIL import Image


C, D = 1900, 870

# Open the original image
img = Image.open("img/imperial.png")  # Replace with your image file path

img_resized = img.resize((C, D), Image.Resampling.LANCZOS)

# Save or show the resized image
img_resized.save("img/imperial-resized.png")  # You can change the filename as needed
img_resized.show()
