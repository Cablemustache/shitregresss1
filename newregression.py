from pandas_datareader import data
R = data.DataReader('AAPL', 'yahoo', start='2012/01/01', end='2018/01/01')
print(R.head())
print(f"Number of rows: {R.size}")

L = data.DataReader('EFX', 'yahoo', start='2012/01/01', end='2018/01/01')
print(L.head())

R = R.resample('M').last().pct_change()
print(R.head())


L = L.resample('M').last().pct_change()
print(L.head())
 
Rf = data.DataReader('CHART', 'fred' ,)