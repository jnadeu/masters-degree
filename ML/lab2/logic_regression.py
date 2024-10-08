import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


#Load iris dataset and store as a dataframe
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

#rename target variable
iris_df['species'] = pd.Categorical.from_codes(iris.target,
iris.target_names)

# Display basic statistics of the dataframe
print(iris_df.describe())

# Pairplot to visualize relationships between features
sns.pairplot(iris_df, hue='species')
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
plt.show()

# Boxplot to visualize the distribution of each feature
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris_df)
plt.title('Boxplot of Iris Features')
plt.xticks(rotation=90)
plt.show()

# Violin plot to visualize the distribution and density of each feature for each species
plt.figure(figsize=(10, 6))
for feature in iris.feature_names:
    plt.figure()
    sns.violinplot(x='species', y=feature, data=iris_df)
    plt.title(f'Violin Plot of {feature}')
    plt.show()

# Scatter plot matrix with KDE (Kernel Density Estimate)
sns.pairplot(iris_df, hue='species', kind='kde', diag_kind='kde',
markers=['o', 's', 'D'])
plt.suptitle('Scatter Plot Matrix with KDE of Iris Dataset', y=1.02)
plt.show()

"""-----------------------------------------"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Split the data into training and testing sets
X = iris_df.drop('species', axis=1)
y = iris_df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')



# Print confusion matrix
print('Confusion Matrix:')
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Visualize the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()