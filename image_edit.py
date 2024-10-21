from PIL import Image

# Define original dimensions (A, B) and new dimensions (C, D)
A, B = 693, 462  # Example original dimensions (replace with your values)
C, D = 1900, 870 # Example new dimensions (replace with your values)

# Open the original image
img = Image.open("img/Queens-Tower-at-night.jpeg")  # Replace with your image file path

img_resized = img.resize((C, D), Image.Resampling.LANCZOS)

# Save or show the resized image
img_resized.save("img/Queens-Tower-at-night-resized.jpeg")  # You can change the filename as needed
img_resized.show()
