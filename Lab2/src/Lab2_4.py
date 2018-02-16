
import numpy as npy
rnums = npy.random.randint(0, 20, 15)
print("Numbers List:")
print(rnums)
print("Frequest number in the list:")
print(npy.bincount(rnums).argmax())