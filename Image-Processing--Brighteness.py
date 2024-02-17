from PIL import Image, ImageEnhance

# Open the image file
image_path = r"C:\Users\khush\OneDrive\Desktop\Furqan Python\Image Processing Sample.BMP"
image = Image.open(image_path)

# Adjust the brightness (increase or decrease)
brightness_factor = 1.5  # You can adjust this value for desired brightness
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(brightness_factor)

# Display the original and brightened images
image.show(title="Original Image")
brightened_image.show(title="Brightened Image")

# Save the brightened image
brightened_image.save("brightened_image.bmp")

# Close the images
image.close()
brightened_image.close()
