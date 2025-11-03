# K-Means Image Compression and Viewer

This project implements a K-Means clustering-based image compression tool with an interactive graphical user interface (GUI). Users can view and compress images by selecting the number of clusters for compression, switch between different images, and explore the effects of compression interactively.

Learn more about the K-means algorithm [here](https://www.geeksforgeeks.org/k-means-clustering-introduction/).

Originally done as class work for CPS 352: Concepts and Implementations of programming languages

## Features
- **Image Compression**: Uses K-Means clustering to compress images by reducing the number of colors.
- **Interactive GUI**: Built with `matplotlib`, allowing users to:
  - Adjust the number of clusters with a slider.
  - Navigate between multiple images using "Next" and "Previous" buttons.
- **Customizable**: Supports any set of image files specified by the user.

---

## Installation

### Prerequisites
Ensure you have Python installed (3.8 or higher recommended). You also need the following Python libraries:
- `matplotlib`
- `Pillow`
- `numpy`

You can install the required libraries using:

```bash
pip install -r requirements.txt
