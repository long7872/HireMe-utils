import pandas as pd

# Load one of your datasets
df = pd.read_csv("data/processed/essay_set1.csv")

# Look at score distributions
print("Score distributions:")
print(df[['Content', 'Organization', 'Word Choice', 
          'Sentence Fluency', 'Conventions']].describe())

# Look at essay lengths
df['word_count'] = df['essay'].str.split().str.len()
print("\nEssay length statistics:")
print(df['word_count'].describe())

# Check for missing data
print("\nMissing values:")
print(df.isnull().sum())