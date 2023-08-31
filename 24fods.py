import numpy as np
from sklearn.neighbors import KNeighborsClassifier
def predict_condition(symptoms, k):
  data1 =open("fever.txt","r")
  data=data1.read()
  features = data[:, :-1]
  labels = data[:, -1]
  classifier = KNeighborsClassifier(n_neighbors=k)
  classifier.fit(features, labels)
  prediction = classifier.predict([symptoms])[0]
  return prediction

symptoms = input("Enter the symptoms: ").split(",")

k = int(input("Enter the value of k: "))

prediction = predict_condition(symptoms, k)

if prediction:
  print("The patient has the condition.")
else:
  print("The patient does not have the condition.")

