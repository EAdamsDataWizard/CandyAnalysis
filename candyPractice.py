import pandas as pd 

FileName = r'C:\Projects\Practice\Halloween+Candy+Rankings\candy-data.csv'
winners =  r'C:\Projects\Practice\Halloween+Candy+Rankings\candyWinners.csv'
cleaned =  r'C:\Projects\Practice\Halloween+Candy+Rankings\candyCleaned.csv'
df = pd.read_csv(FileName)

print(df.head(7))

nullAudit = df.isna().sum()
print(f"\nNull Audit Results: {nullAudit}.")
print(f"\nData Summary: ")
df.info()

boo_cols = ['chocolate', 'fruity', 'caramel','peanutyalmondy','nougat',\
   'crispedricewafer','hard','bar','pluribus']
per_cols = ['sugarpercent','pricepercent','winpercent']

df['competitorname'] = df['competitorname'].astype('category')

for col in boo_cols:
    df[col] = pd.to_numeric(df[col], downcast='integer')
for col in per_cols:
    df[col] = pd.to_numeric(df[col], downcast='float')

df['winpercent'] = df['winpercent']/100
df['winpercent'] = df['winpercent'].round(2)

print("\nUpdated info:")
df.info()

df.to_csv(cleaned, index=False)
high_win_candy = df[df['winpercent']>50]
final_df = high_win_candy.sort_values(by='winpercent', ascending=False)

final_df.to_csv(winners, index=False)
print("Data has been cleaned, saved and ready for visuals.")