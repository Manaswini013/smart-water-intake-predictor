# ==============================
# 1. IMPORTS
# ==============================
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, accuracy_score

# ==============================
# 2. LOAD DATASET
# ==============================
df = pd.read_csv("advanced_water_dataset.csv")

# ------------------------------
# Remove unwanted columns
# ------------------------------
df = df.drop(["urine_color", "caffeine_intake"], axis=1)

# ==============================
# 3. ENCODING CATEGORICAL FEATURES
# ==============================
categorical_cols = [
    "gender","weather_condition","activity_level",
    "sweating_level","diet_type","health_condition"
]

label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Encode target (hydration_status)
status_encoder = LabelEncoder()
df["hydration_status"] = status_encoder.fit_transform(df["hydration_status"])

# ==============================
# 4. SPLIT DATA
# ==============================
X = df.drop(["water_intake", "hydration_status"], axis=1)
y_reg = df["water_intake"]
y_clf = df["hydration_status"]

X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)
_, _, y_train_clf, y_test_clf = train_test_split(X, y_clf, test_size=0.2, random_state=42)

# ==============================
# 5. TRAIN MODELS
# ==============================
reg_model = RandomForestRegressor(n_estimators=100, random_state=42)
clf_model = RandomForestClassifier(n_estimators=100, random_state=42)

reg_model.fit(X_train, y_train_reg)
clf_model.fit(X_train, y_train_clf)

# ==============================
# 6. EVALUATION
# ==============================
print("\nModel Performance:")
print("MAE (Regression):", round(mean_absolute_error(y_test_reg, reg_model.predict(X_test)), 2))
print("Accuracy (Classifier):", round(accuracy_score(y_test_clf, clf_model.predict(X_test)) * 100, 2), "%")

# ==============================
# 7. FEATURE IMPORTANCE
# ==============================
importances = reg_model.feature_importances_
features = X.columns

plt.figure(figsize=(10,6))
plt.barh(features, importances)
plt.xlabel("Importance")
plt.title("Feature Importance for Water Intake")
plt.show()

# ==============================
# 8. SAVE MODELS & ENCODERS
# ==============================
joblib.dump(reg_model, "water_model.pkl")
joblib.dump(clf_model, "status_model.pkl")
joblib.dump(label_encoders, "encoders.pkl")
joblib.dump(status_encoder, "status_encoder.pkl")
joblib.dump(X.columns.tolist(), "columns.pkl")

print("\n✅ Models saved successfully!")