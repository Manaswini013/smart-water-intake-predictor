# ==============================
# SMART HYDRATION SYSTEM - DESKTOP VERSION
# ==============================
import pandas as pd
import joblib
import time
from plyer import notification

import matplotlib.pyplot as plt
import seaborn as sns
import random

# ==============================
# 1. LOAD MODELS & ENCODERS
# ==============================
reg_model = joblib.load(r"C:\Users\sarad\OneDrive\Desktop\PR project\water_model.pkl")
clf_model = joblib.load(r"C:\Users\sarad\OneDrive\Desktop\PR project\status_model.pkl")
label_encoders = joblib.load(r"C:\Users\sarad\OneDrive\Desktop\PR project\encoders.pkl")
status_encoder = joblib.load(r"C:\Users\sarad\OneDrive\Desktop\PR project\status_encoder.pkl")
columns = joblib.load(r"C:\Users\sarad\OneDrive\Desktop\PR project\columns.pkl")

print("✅ Models Loaded Successfully!\n")

# ==============================
# 2. USER INPUT
# ==============================
user = {}
print("Enter Your Details:")

# Numeric Inputs
user["age"] = int(input("Age: "))
user["weight"] = float(input("Weight (kg): "))
user["height"] = float(input("Height (cm): "))
user["BMI"] = round(user["weight"]/((user["height"]/100)**2),2)
user["temperature"] = float(input("Temperature (°C): "))
user["humidity"] = float(input("Humidity (%): "))
user["altitude"] = float(input("Altitude (meters): "))
user["activity_duration"] = int(input("Activity Duration (minutes): "))
user["steps_per_day"] = int(input("Steps per day: "))
user["alcohol_intake"] = int(input("Alcohol intake (units/week): "))
user["previous_day_water_intake"] = float(input("Yesterday water intake (liters): "))
user["sleep_hours"] = float(input("Sleep hours: "))

# Categorical Inputs
print("\nCategorical Inputs:")
user["gender"] = input("Gender (Male/Female): ")
user["weather_condition"] = input("Weather (sunny/cloudy/rainy): ")
user["activity_level"] = input("Activity Level (low/medium/high): ")
user["sweating_level"] = input("Sweating Level (low/medium/high): ")
user["diet_type"] = input("Diet Type (normal/high-protein): ")
user["health_condition"] = input("Health Condition (none/diabetes/kidney): ")

# ==============================
# 3. CONVERT TO DATAFRAME & ENCODE
# ==============================
input_df = pd.DataFrame([user])
categorical_cols = ["gender","weather_condition","activity_level",
                    "sweating_level","diet_type","health_condition"]

try:
    for col in categorical_cols:
        input_df[col] = label_encoders[col].transform(input_df[col])
except:
    print("❌ Invalid input! Please match exact values.")
    exit()

# Reorder columns
input_df = input_df[columns]

# ==============================
# 4. PREDICTIONS
# ==============================
water = reg_model.predict(input_df)[0]
status = clf_model.predict(input_df)[0]
status_label = status_encoder.inverse_transform([status])[0]

print(f"\n💧 Recommended Water Intake: {round(water,2)} L/day")
print(f"📊 Hydration Status: {status_label}")

# ==============================
# 5. SMART SUGGESTIONS
# ==============================
def hydration_alert(water_intake):
    if water_intake > 3.5:
        print("⚠️ High hydration needed due to activity/weather.")
    elif water_intake < 2.5:
        print("⚠️ You are likely dehydrated. Drink more water!")
    else:
        print("✅ Your hydration level is good.")

def hydration_tips():
    tips = [
        "🍉 Eat fruits like watermelon and cucumber to stay hydrated.",
        "🥛 Drink milk or coconut water for electrolytes.",
        "💦 Take small sips frequently rather than large amounts at once.",
        "🥗 Include hydrating vegetables like lettuce, tomato, and celery in your meals."
    ]
    print("\n💡 Hydration Tips:")
    for tip in random.sample(tips, 3):
        print("-", tip)

hydration_alert(water)
hydration_tips()

# ==============================
# 6. DESKTOP REMINDERS WITH SOUND
# ==============================
import winsound
from plyer import notification
import time

def water_reminder(hour, water_amount):
    # Desktop notification
    notification.notify(
        title=f"💧 Hydration Reminder - Hour {hour}",
        message=f"Time to drink ~{water_amount:.2f} L of water!",
        timeout=10
    )
    # Sound alert (requires WAV file)
    winsound.PlaySound("alert.wav", winsound.SND_FILENAME)
    print(f"⏰ Reminder {hour}: Drink ~{water_amount:.2f} L water")

# Example usage
total_water = 2.8
hourly_goal = total_water / 8
for i in range(1, 9):
    water_reminder(i, hourly_goal)
    time.sleep(5)  # for testing; use 3600 for 1 hour intervals

# ==============================
# 7. WEEKLY WATER INTAKE CHART (SIMULATION)
# ==============================
week_data = pd.DataFrame({
    "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    "Water Intake (L)": [round(random.uniform(2,4),2) for _ in range(7)],
    "Recommended Intake (L)": [round(water,2)]*7
})

plt.figure(figsize=(10,5))
sns.barplot(x="Day", y="Water Intake (L)", data=week_data, color="skyblue")
plt.plot(week_data["Day"], week_data["Recommended Intake (L)"], color="red", marker='o', label="Recommended")
plt.title("Weekly Water Intake vs Recommended Intake")
plt.ylabel("Water (Liters)")
plt.legend()
plt.show()

# ==============================
# 8. GAMIFICATION
# ==============================
def hydration_challenge(week_data, goal=2.5):
    success_days = sum(week_data["Water Intake (L)"] >= goal)
    print(f"\n🏆 Hydration Challenge Result: {success_days}/7 days achieved")
    if success_days == 7:
        print("🎉 Congratulations! You completed the weekly hydration challenge!")
    elif success_days >= 5:
        print("👍 Good job! Almost perfect week!")
    else:
        print("⚠️ Keep trying! Aim for at least 2.5 L/day.")

hydration_challenge(week_data)

print("\n✅ Smart Hydration System finished successfully!")