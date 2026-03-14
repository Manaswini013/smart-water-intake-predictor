import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data/smart_water_intake_dataset.csv")

# Input features
X = data[['Weight_kg','Age','Temperature_C','Activity_Level']]

# Output
y = data['Water_Intake_Liters']

# Train model
model = LinearRegression()
model.fit(X,y)

print("Model trained successfully!")

# Take user input
weight = float(input("Enter your weight (kg): "))
age = int(input("Enter your age: "))
temp = float(input("Enter temperature (C): "))

print("Activity Level: 1-Low  2-Medium  3-High")
activity = int(input("Enter activity level: "))

# Prediction
prediction = model.predict([[weight,age,temp,activity]])

print("\nRecommended Daily Water Intake:")
print(round(prediction[0],2),"Liters")


