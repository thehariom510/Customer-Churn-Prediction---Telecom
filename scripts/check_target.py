import pandas as pd
df = pd.read_csv('../data/Telecom_Customer_Churn.csv')
df.columns = [c.strip() for c in df.columns]
target = 'Churn Category'
print('Target column:', target)
print('Value counts:')
print(df[target].value_counts(dropna=False))
if df[target].nunique() < 2:
    raise SystemExit('Target has less than 2 classes. Provide a dataset with both classes to proceed.')
