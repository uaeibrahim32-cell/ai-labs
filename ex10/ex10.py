# AI Based College Canteen Food Waste Predictor
# Using Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression

# Previous canteen data
# Students, Meals Prepared, Food Waste (kg)

X = np.array([
    [100, 120],
    [150, 170],
    [200, 220],
    [250, 270],
    [300, 320],
    [350, 370],
    [400, 420]
])

y = np.array([5, 7, 9, 11, 13, 15, 17])

# Create and train the AI model
model = LinearRegression()
model.fit(X, y)

# Get input from user
students = int(input("Enter number of students: "))
meals = int(input("Enter number of meals prepared: "))

# Predict food waste
prediction = model.predict([[students, meals]])

print("\n--- Food Waste Prediction ---")
print("Number of Students :", students)
print("Meals Prepared     :", meals)
print("Predicted Food Waste :", round(prediction[0], 2), "kg")

# Suggestion
if prediction[0] > 12:
    print("Suggestion: Reduce the quantity of food prepared.")
elif prediction[0] > 8:
    print("Suggestion: Prepare food carefully to minimize waste.")
else:
    print("Suggestion: Food preparation quantity is acceptable.")