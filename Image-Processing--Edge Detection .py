from PIL import Image, ImageFilter

# Open the image file
image_path = r"C:\Users\khush\OneDrive\Desktop\Furqan Python\Image Processing Sample.BMP"
image = Image.open(image_path)

# Apply the Sobel filter for edge detection
edges = image.filter(ImageFilter.FIND_EDGES)

# Display the original and edge-detected images
image.show(title="Original Image")
edges.show(title="Edge-Detected Image")

# Save the edge-detected image
edges.save("edge_detected_image.bmp")

# Close the images
image.close()
edges.close()