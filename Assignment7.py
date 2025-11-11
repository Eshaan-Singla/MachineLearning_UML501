#!/usr/bin/env python
# coding: utf-8

# In[4]:


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
kernels = ['linear', 'poly', 'rbf']
results = {}
for kernel in kernels:
    if kernel == 'poly':
        model = SVC(kernel=kernel, degree=3)
    else:
        model = SVC(kernel=kernel)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='macro')
    rec = recall_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')
    results[kernel] = {'Accuracy': acc, 'Precision': prec, 'Recall': rec, 'F1-Score': f1}
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(4,3))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'Confusion Matrix - {kernel.capitalize()} Kernel')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
results_df = pd.DataFrame(results).T
print("=== SVM Performance on Iris Dataset ===")
print(results_df)


# In[5]:


cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
svm_noscale = SVC(kernel='rbf', random_state=42)
svm_noscale.fit(X_train, y_train)
train_acc_noscale = svm_noscale.score(X_train, y_train)
test_acc_noscale = svm_noscale.score(X_test, y_test)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
svm_scaled = SVC(kernel='rbf', random_state=42)
svm_scaled.fit(X_train_scaled, y_train)
train_acc_scaled = svm_scaled.score(X_train_scaled, y_train)
test_acc_scaled = svm_scaled.score(X_test_scaled, y_test)
comparison = pd.DataFrame({
    'Model': ['Without Scaling', 'With Scaling'],
    'Training Accuracy': [train_acc_noscale, train_acc_scaled],
    'Testing Accuracy': [test_acc_noscale, test_acc_scaled]
})
print("=== SVM (RBF Kernel) - Feature Scaling Comparison ===")
print(comparison)

