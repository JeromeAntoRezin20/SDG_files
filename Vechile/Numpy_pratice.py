# import numpy as np
# n2 = [1,2,3,4,5]
# my_n2 = np.array(n2)
# print(my_n2)
# into_list = my_n2.tolist()
# print(into_list)
# print(np.linspace(0,10,50))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Define the dimensions of the image
height = 300  # Height of the image
width = 400   # Width of the image

# Create a blank image with the red color
# Initialize a 3D NumPy array with the shape (height, width, 3)
red_image = np.zeros((height, width, 3), dtype=np.uint8)

# Set the red channel to 255 (maximum intensity)
red_image[:, :, 0] = 255  # Red channel

# Display the image using matplotlib
plt.imshow(red_image)
plt.axis('off')  # Turn off axes
plt.show()
