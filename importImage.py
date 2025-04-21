import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage.io import imread
from skimage.color import rgb2gray

# Load the image
image_path = '/Users/juanparra/Library/CloudStorage/Dropbox/Juan/Classes/SpatialEcology/CursoAplicacionesSIGBiologia/2025_1/Clase01/Taller01/tc_2000_ant.tif'  # Replace with your image path
image = imread(image_path)

# Convert the image to grayscale
gray_image = rgb2gray(image)

# Flatten the image for clustering
pixels = gray_image.flatten().reshape(-1, 1)

# Perform KMeans clustering
n_clusters = 3  # Number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(pixels)

# Reshape the clustered labels to the original image shape
clustered_image = kmeans.labels_.reshape(gray_image.shape)

# Plot the original and clustered images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Clustered Image")
plt.imshow(clustered_image, cmap='viridis')
plt.axis('off')

plt.show()