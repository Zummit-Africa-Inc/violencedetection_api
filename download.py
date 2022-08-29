import os
try:
    from model import classify_image
except OSError as e:
    os.system("wget -O bestmodel.h5 https://huggingface.co/spaces/SIB/violence_api/resolve/main/bestmodel.h5")
    print("File downloaded!")
    from model import classify_image
from PIL import Image
import numpy as np


image = Image.open("images.jpeg")
image = image.resize((224, 224), Image.ANTIALIAS)
image = np.array(image)
print(classify_image(image))

