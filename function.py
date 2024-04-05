import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_filter(image_path, filter_type, cutoff_frequency):
    original_image = cv2.imread(image_path, 0)  

    f_transform = np.fft.fft2(original_image)
    f_shift = np.fft.fftshift(f_transform)

    rows, cols = original_image.shape
    crow, ccol = rows // 2, cols // 2

    if filter_type == "low-pass":
        mask = np.zeros((rows, cols), np.uint8)
        mask[crow - cutoff_frequency:crow + cutoff_frequency, ccol - cutoff_frequency:ccol + cutoff_frequency] = 1
    elif filter_type == "high-pass":
        mask = np.ones((rows, cols), np.uint8)
        mask[crow - cutoff_frequency:crow + cutoff_frequency, ccol - cutoff_frequency:ccol + cutoff_frequency] = 0

    f_shift_filtered = f_shift * mask

    
    f_ishift = np.fft.ifftshift(f_shift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    return img_back


if __name__ == "__main__":
    
    filtered_image = apply_filter("example_image.jpg", "low-pass", 50)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Filtered Image')
    plt.show()
