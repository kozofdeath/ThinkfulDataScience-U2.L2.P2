import pandas as pd;
import matplotlib.pyplot as plt;

df = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

#this removes rows that have empty entries
df.dropna(inplace=True)

df.boxplot(column='Amount.Funded.By.Investors');
plt.show();

df.hist(column='Amount.Funded.By.Investors');
plt.show();

import scipy.stats as stats

plt.figure()
graph = stats.probplot(df['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()

print df;
