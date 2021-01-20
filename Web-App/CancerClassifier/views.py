from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import json

with open('./model/cancerModelClasses.json', 'r') as f:
    predIndo = f.read()

predIndo = json.loads(predIndo)

model_graph = tf.compat.v1.Graph()
with model_graph.as_default():
    sess = tf.compat.v1.Session()
    with sess.as_default():
        model=load_model('./model/CancerClassifier_v1.h5')

def index(request):
    context = {'a' : 1}
    return render(request, 'index.html', context)

def predictImage(request):
    print(request)
    print(request.POST.dict())
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    testimage = '.' + filePathName

    img = image.load_img(testimage, target_size=(28, 28))
    x = image.img_to_array(img)
    x /= 255
    x = x.reshape(1, 28, 28, 3)

    with model_graph.as_default():
        with sess.as_default():
            final_prediction = model.predict(x)

    import numpy as np
    predictedLabel = predIndo[str(np.argmax(final_prediction[0]))]

    context={'filePathName':filePathName,'predictedLabel':predictedLabel[0]}
    return render(request,'index.html',context)
