import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.widgets import Slider, Button
import ImageCompressor

# List of image filenames
image_filenames = ["Image1.jpg", "Image2.jpg", "Image3.jpg", "Image4.jpg", "Image5.jpg"]

image_compressor_list = [ImageCompressor.ImageCompressor(filename) for filename in image_filenames]

# Load the initial image
current_image_index = 0
current_k = 0
current_image = image_compressor_list[current_image_index]

# Create the initial plot
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.3)  # Adjust space for buttons and slider
ax.set_title("Kmeans Clustering")
ax.axis('off')

# Display the initial image
img_display = ax.imshow(current_image.get_image(0))

# Add a slider for brightness control
ax_slider = plt.axes([0.25, 0.1, 0.5, 0.03])  # x, y, width, height
slider = Slider(ax_slider, 'Number of Clusters', 0, 64, valinit=0, valstep=1)

# Update function for slider
def update(val):
    global current_k
    current_k = int(slider.val)
    current_image = image_compressor_list[current_image_index]

    # Get the correct image based on current_k
    if current_k == 0:
        img_display.set_data(current_image.get_image(current_k))  # Original image
    else:
        if current_k not in current_image.kmeans_images:
            current_image.kmeans(current_k)  # Perform clustering if necessary
        img_display.set_data(current_image.get_image(current_k))  # Compressed image

    fig.canvas.draw_idle()  # Refresh the canvas


slider.on_changed(update)

# Add "Previous" and "Next" buttons
ax_prev = plt.axes([0.1, 0.01, 0.1, 0.075])  # x, y, width, height
ax_next = plt.axes([0.8, 0.01, 0.1, 0.075])
button_prev = Button(ax_prev, 'Previous')
button_next = Button(ax_next, 'Next')


# Function to load and display the next/previous image
def change_image(direction):
    global current_image_index, current_k, current_image
    if direction == 'next':
        # Move to the next image, wrapping around if necessary
        current_image_index = (current_image_index + 1) % len(image_filenames)
    elif direction == 'prev':
        # Move to the previous image, wrapping around if necessary
        current_image_index = (current_image_index - 1) % len(image_filenames)

    current_image = image_compressor_list[current_image_index]
    if current_k == 0:
        img_display.set_data(current_image.get_image(0))  # Show original image
    else:
        if current_k not in current_image.kmeans_images:
            current_image.kmeans(current_k)  # Perform clustering if necessary
        img_display.set_data(current_image.get_image(current_k))  # Show clustered image

    fig.canvas.draw_idle()  # Redraw the canvas

# Define the button callbacks
button_prev.on_clicked(lambda event: change_image('prev'))
button_next.on_clicked(lambda event: change_image('next'))

# Show the plot
plt.show()