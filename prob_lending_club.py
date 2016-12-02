import matplotlib.pyplot as plt
import pandas as pd;

loans_data = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
print loans_data;
loans_data.dropna(inplace=True);
print loans_data;


loans_data.boxplot(column='Amount.Funded.By.Investors')
plt.show();
#how does this plt.show() command work? so the plt is stored in plt even when plt isn't explicity called?

loans_data.hist(column='Amount.Funded.By.Investors', bins = 100)
plt.show();

import scipy.stats as stats
plt.figure()
graph = stats.probplot(loans_data['Amount.Funded.By.Investors'], dist='norm', plot=plt)
plt.show()
#this is also confusing to me; what is the variable graph doing here? Why save this in a variable if it's not called?
