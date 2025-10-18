import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load image
img = mpimg.imread("/content/landscape-nature-sky-236047.jpg").astype(np.float32)
if img.max() > 1:
    img = img / 255.0

# Brightness control
bright_img = np.clip(img + 0.3, 0, 1)
dark_img = np.clip(img - 0.3, 0, 1)

# Show all images
plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.imshow(img)
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(bright_img)
plt.title("Brighter (+0.3)")

plt.subplot(1,3,3)
plt.imshow(dark_img)
plt.title("Darker (-0.3)")

plt.show()