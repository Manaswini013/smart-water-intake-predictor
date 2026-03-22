import pandas as pd
import random

data = []

def calculate_bmi(weight, height):
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)

for _ in range(10000):
    age = random.randint(18, 65)
    weight = random.randint(45, 110)
    height = random.randint(150, 195)
    gender = random.choice(["Male", "Female"])
    
    bmi = calculate_bmi(weight, height)

    temp = random.randint(20, 42)
    humidity = random.randint(30, 90)
    weather = random.choice(["sunny", "cloudy", "rainy"])
    altitude = random.randint(0, 3000)

    activity = random.choice(["low", "medium", "high"])
    duration = random.randint(10, 120)
    sweat = random.choice(["low", "medium", "high"])
    steps = random.randint(2000, 15000)

    diet = random.choice(["normal", "high-protein"])
    caffeine = random.randint(0, 5)
    alcohol = random.randint(0, 10)
    health = random.choice(["none", "diabetes", "kidney"])

    urine = random.randint(1, 8)
    prev_water = round(random.uniform(1.5, 4.5), 2)
    sleep = random.randint(4, 9)

    # 💧 Advanced water calculation logic
    water = weight * 0.035

    # activity impact
    if activity == "high":
        water += 0.8
    elif activity == "medium":
        water += 0.4

    # temperature
    if temp > 30:
        water += 0.6

    # humidity
    if humidity > 70:
        water += 0.3

    # sweating
    if sweat == "high":
        water += 0.5

    # altitude
    if altitude > 1500:
        water += 0.4

    # diet
    if diet == "high-protein":
        water += 0.3

    # caffeine & alcohol
    water += caffeine * 0.05
    water += alcohol * 0.03

    # urine indicator
    if urine > 5:
        water += 0.5

    # sleep effect
    if sleep < 6:
        water += 0.2

    # health condition adjustment
    if health == "kidney":
        water -= 0.3

    water = round(water, 2)

    # hydration status
    if water >= 3.5:
        status = "Good"
    elif water >= 2.5:
        status = "Moderate"
    else:
        status = "Dehydrated"

    data.append([
        age, weight, height, gender, bmi,
        temp, humidity, weather, altitude,
        activity, duration, sweat, steps,
        diet, caffeine, alcohol, health,
        urine, prev_water, sleep,
        water, status
    ])

df = pd.DataFrame(data, columns=[
    "age","weight","height","gender","BMI",
    "temperature","humidity","weather_condition","altitude",
    "activity_level","activity_duration","sweating_level","steps_per_day",
    "diet_type","caffeine_intake","alcohol_intake","health_condition",
    "urine_color","previous_day_water_intake","sleep_hours",
    "water_intake","hydration_status"
])

df.to_csv("advanced_water_dataset.csv", index=False)

print("Advanced dataset created successfully!")