from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from keras.models import load_model
from PIL import Image
import numpy as np
import lime
from lime import lime_image
from io import BytesIO

def getPrediction(filename):
    best_fabric_path = 'C:/Users/yoosh/OneDrive/문서/fabric1.h5'
    model1 = load_model(best_fabric_path)
    best_color_path = 'C:/Users/yoosh/OneDrive/문서/color1.h5'
    model2 = load_model(best_color_path)
    best_length_path = 'C:/Users/yoosh/OneDrive/문서/length.h5'
    model3 = load_model(best_length_path)

    image = load_img(filename, target_size=(224, 224))

    image1 = load_img(filename, target_size=(150, 150))

    # imgs = Image.open(BytesIO)
    img_arr = np.asarray(image1)[:, :, :3] / 255
    img_array = np.expand_dims(img_arr, 0)
    # img_array = img_to_array(image1)

    explainer = lime_image.LimeImageExplainer(random_state=42)

    X = img_array
    explanation = explainer.explain_instance(X[0], model1, hide_color=0, top_labels=5, num_samples=1000)

    fabric_label = dict({0: 'cotton', 1: 'denim', 2: 'knit', 3: 'leather'})
    cloth_info = []
    cloth_info.append(fabric_label.get(explanation.top_labels[0]))

    explainer = lime_image.LimeImageExplainer(random_state=42)

    X = img_array
    explanation = explainer.explain_instance(X[0], model2, hide_color=0, top_labels=5, num_samples=1000)
    color_label = dict({0: 'bright', 1: 'dark', 2: 'etc'})
    cloth_info.append(color_label.get(explanation.top_labels[0]))

    explainer = lime_image.LimeImageExplainer(random_state=42)

    X = img_array
    explanation = explainer.explain_instance(X[0], model3, hide_color=0, top_labels=5, num_samples=1000)
    length_label = dict({0: 'half sleeve_train', 1: 'long sleeve_train'})
    cloth_info.append(length_label.get(explanation.top_labels[0]))
    # 이거 경로 수정
    print('%s' % (cloth_info[0]))
    return cloth_info[0], cloth_info[1], cloth_info[2]

#    image = img_to_array(image)
#    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
#    image = preprocess_input(image)
#    yhat = model.predict(image)
#    label = decode_predictions(yhat)
#    label = label[0][0]