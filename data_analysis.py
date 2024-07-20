import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Cargar datos
data = pd.read_csv('calls_data.csv')

# Procesamiento de datos
data['fraud'] = data['fraud'].apply(lambda x: 1 if x == 'fraudulent' else 0)

# Variables independientes y dependientes
X = data[['duration', 'day_of_week']]
y = data['fraud']

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de Regresión Logística
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred_log = log_reg.predict(X_test)

# Resultados de Regresión Logística
print("Regresión Logística")
print(classification_report(y_test, y_pred_log))
print("Accuracy:", accuracy_score(y_test, y_pred_log))

# Modelo de Árbol de Decisión
tree_clf = DecisionTreeClassifier()
tree_clf.fit(X_train, y_train)
y_pred_tree = tree_clf.predict(X_test)

# Resultados de Árbol de Decisión
print("Árbol de Decisión")
print(classification_report(y_test, y_pred_tree))
print("Accuracy:", accuracy_score(y_test, y_pred_tree))
