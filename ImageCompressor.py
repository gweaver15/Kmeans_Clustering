from PIL import Image
import numpy as np

class ImageCompressor:

    image_filenames = ["test1.jpg", "test2.jpg", "test3.jpg", "test4.jpg", "test5.jpg"]

    def __init__(self, filename):
        self.original_image = np.array(Image.open(filename))
        self.kmeans_images = {}

    def kmeans(self, k):
        data = self.original_image.reshape(-1, 3)  # Flatten image into (pixels, 3) array
        centroids = np.random.randint(0, 256, size=(k, 3))  # Randomly initialize centroids

        stable = False
        while not stable:

            # Compute distances from all pixels to all centroids in one step
            distances = np.linalg.norm(data[:, None, :] - centroids[None, :, :], axis=2)
            labels = np.argmin(distances, axis=1)  # Find the closest centroid for each pixel

            # Update centroids as the mean of assigned pixels
            new_centroids = np.array([
                data[labels == k].mean(axis=0) if np.any(labels == k) else np.random.randint(0, 256, size=3)
                for k in range(k)
            ])

            # Check if centroids have stabilized (converged within a tolerance)
            if np.allclose(centroids, new_centroids, atol=1):
                stable = True
            centroids = new_centroids

        # Map each pixel to its corresponding centroid
        compressed_data = centroids[labels].reshape(self.original_image.shape)
        self.kmeans_images[k] = compressed_data.astype(np.uint8)

    def get_image(self, k):
        if k == 0:
            return self.original_image
        elif k not in self.kmeans_images:
            self.kmeans(k)
        return self.kmeans_images[k]