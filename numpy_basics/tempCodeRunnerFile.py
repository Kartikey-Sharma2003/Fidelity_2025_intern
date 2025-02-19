df=pd.read_csv('tips.csv')
df['smoker'] = df['smoker'].apply(lambda x: 1 if x.lower() == 'yes' else 0)
print(df[['smoker']])