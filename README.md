# Bit-Plane Slicing using OpenCV

##  Project Description

This project demonstrates **Bit-Plane Slicing** using Python, OpenCV, NumPy, and Matplotlib.

Bit-Plane Slicing is an image processing technique that separates a grayscale image into its individual **8-bit planes**. Each bit plane represents one bit position of the pixel values, from **Bit Plane 0 (LSB)** to **Bit Plane 7 (MSB)**.

##  Objective

* Load a grayscale image.
* Extract all 8 bit planes from the image.
* Convert each bit plane into a visible black-and-white image.
* Display the original image along with all 8 bit planes.

## 🛠️ Technologies Used

* **Python**
* **OpenCV (`cv2`)** – Image loading
* **NumPy (`numpy`)** – Bitwise operations
* **Matplotlib (`matplotlib`)** – Displaying images

## 📂 Project Structure

```text
Bit-Plane-Slicing/
│
├── bit_plane_slicing.py
├── NTR.jpg
└── README.md
```

##  How It Works

1. The image `nature.jpg` is loaded in grayscale.
2. The program checks whether the image was loaded successfully.
3. A loop runs from **0 to 7** to extract all eight bit planes.
4. The operation:

```python
bit_plane = (img >> i) & 1
```

extracts the **i-th bit** from every pixel.
5. The extracted values (`0` and `1`) are multiplied by `255` to make them visible as black and white.
6. The original image and all eight bit planes are displayed using Matplotlib.

##  Output

The output displays **9 images**:

* Original Image
* Bit Plane 0
* Bit Plane 1
* Bit Plane 2
* Bit Plane 3
* Bit Plane 4
* Bit Plane 5
* Bit Plane 6
* Bit Plane 7

**Bit Plane 0** represents the Least Significant Bit (LSB), while **Bit Plane 7** represents the Most Significant Bit (MSB).



Install the required libraries:

```bash
pip install opencv-python numpy matplotlib
```

Then run:

```bash
python bit_plane_slicing.py
```

Make sure `nature.jpg` is present in the same folder as the Python file.


The program successfully performs **8-bit Bit-Plane Slicing** and displays the original grayscale image together with its individual bit planes.
