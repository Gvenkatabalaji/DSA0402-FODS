import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

dataset = pd.read_csv("C:/Users/vijay/OneDrive/Documents/medical_data.csv")

selected_features = ['age', 'gender', 'blood_pressure', 'cholesterol']
target = 'outcome'

X = dataset[selected_features]
y = dataset[target]

X = pd.get_dummies(X, columns=['gender'], drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Good')
recall = recall_score(y_test, y_pred, pos_label='Good')
f1 = f1_score(y_test, y_pred, pos_label='Good')

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")

conf_matrix = confusion_matrix(y_test, y_pred, labels=['Good', 'Bad'])
print("Confusion Matrix:")
print(conf_matrix)


predicted_labels = ['Good' if pred == 2 else 'Bad' for pred in y_pred]

for i, prediction in enumerate(predicted_labels):
    print(f"Prediction {i+1}: {prediction}")
