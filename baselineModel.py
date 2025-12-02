import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

# Load data
df = pd.read_csv("data/processed/essay_set1.csv")

# Prepare data
X = df['essay']
y = df['Content']  # Start with just ONE attribute

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text to numbers (TF-IDF)
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_vec, y_train)

# Predict
y_pred = model.predict(X_test_vec)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Mean Absolute Error: {mae:.3f}")
print(f"Root Mean Squared Error: {rmse:.3f}")
print(f"\nInterpretation:")
print(f"On average, predictions are off by {mae:.2f} points")
print(f"(On a 1-6 scale, this means if true score is 4, we predict {4-mae:.1f} to {4+mae:.1f})")

# Add this to your baselineModel.py file

# Let's look at what the model considers "important"
feature_names = vectorizer.get_feature_names_out()
feature_importance = model.feature_importances_

# Get top 20 most important words
top_indices = np.argsort(feature_importance)[-20:]
top_features = [feature_names[i] for i in top_indices]
top_importance = [feature_importance[i] for i in top_indices]

print("\n" + "="*50)
print("Top 20 most important words for predicting Content score:")
print("="*50)
for word, importance in zip(top_features, top_importance):
    print(f"{word:20s} {importance:.4f}")