import tensorflow as tf
model_0 = tf.keras.models.load_model('bestmodel.h5')


def classify_image(inp):
    inp = inp.reshape((-1, 224, 224, 3))
    prediction = model_0.predict(inp)
    output  = ""
    if prediction[0][prediction.argmax()] < 0.84:
      output = "Good Image."
    elif prediction.argmax() == 0:
      output = "Rifle Violence!"
    elif prediction.argmax() == 1:
      output = "Guns Violence!"
    elif prediction.argmax() == 2:
      output = "Knife Violence!"
    elif prediction.argmax() == 3:
      output = "Pornographic Image!"
    elif prediction.argmax() == 4:
      output = "Normal Person." 
    else:
      output = "Tank Violence!" 
    return output
