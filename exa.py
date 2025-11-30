import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


import os
os.chdir("E:/ai")

# --------------------------------------
# 1. Load Dataset
# --------------------------------------
df = pd.read_csv("ait_315_final_exam_c_data.csv")

print("First 5 rows:")
print(df.head())

# --------------------------------------
# 2. Features & Target
# --------------------------------------
target = "RiskLevel"
X = df.drop(target, axis=1)
y = df[target]

# --------------------------------------
# 3. Train-Test Split
# --------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --------------------------------------
# 4. Train Model
# --------------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# --------------------------------------
# 5. Prediction
# --------------------------------------
y_pred = model.predict(X_test)

# ----------


# 6. Metrics (Multiclass)
# --------------------------------------
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='weighted')
rec = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
cm = confusion_matrix(y_test, y_pred)

# --------------------------------------
# 7. Output
# --------------------------------------
print("🔹 Accuracy:", acc)
print("🔹 Precision (weighted):", prec)
print("🔹 Recall (weighted):", rec)
print("🔹 F1 Score (weighted):", f1)

print("\n🔹 Confusion Matrix:")
print(cm)
