
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/Users/vijay/OneDrive/Documents/student_data.csv")

study_time = data['study_time']
exam_scores = data['exam_scores']

plt.figure(figsize=(8, 6))
plt.scatter(study_time, exam_scores, color='blue', alpha=0.7)
plt.title("Study Time vs Exam Scores")
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Scores")
plt.show()

correlation_coefficient = np.corrcoef(study_time, exam_scores)[0, 1]
print(f"Correlation Coefficient: {correlation_coefficient:.2f}")

plt.figure(figsize=(8, 6))
sns.regplot(x=study_time, y=exam_scores, scatter_kws={'alpha': 0.7})
plt.title("Study Time vs Exam Scores with Regression Line")
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Scores")
plt.show()

sns.jointplot(x=study_time, y=exam_scores,
              kind='reg', scatter_kws={'alpha': 0.7})
plt.show()

sns.displot(data, x='study_time', y='exam_scores', kind='kde')
plt.show()
