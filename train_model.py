import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("Student_Performance.csv")

# Encode categorical
df['Extracurricular Activities'] = df['Extracurricular Activities'].map({'Yes':1, 'No':0})

# Features and target
X = df.drop("Performance Index", axis=1)
y = df["Performance Index"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
