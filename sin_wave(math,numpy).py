# -*- coding: utf-8 -*-
"""Sin wave(math,numpy).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E6kzgSTQ_XNnV8S7TUOHLAX0JYYsxfNg
"""

import matplotlib.pyplot as plt

import numpy as np
import math

x= np.arange(0 , math.pi*2 , 0.05)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sine')
plt.title('Sine wave')

plt.show()

"""#matplotlib.pyplot"""