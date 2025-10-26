import pandas as pd

# Create a sample dataset
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [50, 60, 70, 80, 90]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Find correlation between Height and Weight
correlation = df['Height'].corr(df['Weight'])

print("Correlation between Height and Weight:", correlation)
