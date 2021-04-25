from tensorflow.keras.datasets import mnist
import numpy as np

def load_az_dataset(datasetPath):
    data = []
    labels = []
    
    for row in open(datasetPath):
        row = row.split(',')
        label = int(row[0])
        image = np.array([int(x) for x in row[1:]], dtype='uint8')

        image = image.reshape((28,28))

        data.append(image)
        labels.append(label)



