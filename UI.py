import numpy as np
import cv2
import keras

def predict(img):
    data = cv2.resize(img, (64, 64))
    data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
    data = np.reshape(data, (1, 64, 64, 3)) / 255.0
    res = model.predict(data)[0][0]
    print('Not Bald' if res <0.3 else 'Bald:',res)

model = keras.models.load_model('./models/bald_classify.h5')
img = cv2.imread('./test_data/2.png')
predict(img)
