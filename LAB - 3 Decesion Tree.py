import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Dataset
data = {
    "Outlook": ["Sunny", "Sunny", "Rain", "Overcast"],
    "Temp": ["Hot", "Hot", "Cool", "Mild"],
    "Play": ["No", "No", "Yes", "Yes"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical data
le_outlook = LabelEncoder()
le_temp = LabelEncoder()
le_play = LabelEncoder()

df["Outlook"] = le_outlook.fit_transform(df["Outlook"])
df["Temp"] = le_temp.fit_transform(df["Temp"])
df["Play"] = le_play.fit_transform(df["Play"])

# Features and Target
X = df[["Outlook", "Temp"]]
y = df["Play"]

# Train ID3 Decision Tree
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

# New Sample
new_sample = pd.DataFrame({
    "Outlook": [le_outlook.transform(["Sunny"])[0]],
    "Temp": [le_temp.transform(["Hot"])[0]]
})

# Prediction
prediction = model.predict(new_sample)

if prediction[0] == 1:
    print("Prediction: Yes")
else:
    print("Prediction: No")
