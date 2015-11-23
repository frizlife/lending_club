import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)
#1. Boxplot
loansData.boxplot(column='Amount.Requested')
plt.savefig("boxplot.png")
#2. Histogram
loansData.hist(column='Amount.Requested')
plt.savefig("histogram.png")
#3 QQ
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("qq.png")