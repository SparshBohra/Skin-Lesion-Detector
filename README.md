# Skin-Lesion-Detector
A web application built using Python (Django) that classifies 7 different types of Skin Cancers:
  - Actinic Keratoses and Intraepithelial Carcinoma / Bowen's Disease (akiec)
  - Basal Cell Carcinoma (bcc)
  -  Benign Keratosis-like Lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl)
  -  Dermatofibroma (df)
  -  Melanocytic Nevi (nv)
  -  Vascular Lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc)
  -  Melanoma (mel)
  
The data used is from the Skin Cancer MNIST: HAM10000 28_28_RGB dataset from kaggle. [https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000] The model is built in Keras, a popular python framework and uses a Convolutional Neural Network. This web application is only the first version with scope for further improvement, in both, the model and the UI.

**User Interface for v1.0:**
![skin-lesion-detector UI](https://user-images.githubusercontent.com/53478586/105143621-18526200-5b22-11eb-8039-88a76a690151.png)
