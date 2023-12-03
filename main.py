import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models


def main():
    model = models.load_model('image_classification.model')


if __name__ == '__main__':
    main()
