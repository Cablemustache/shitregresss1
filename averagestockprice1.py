from pandas_datareader import data
EFX = data.DataReader('EFX', 'yahoo',start = '2016/01/01', end = '2019/11/27')
print(EFX.head())
means = EFX.mean()
# [] acsess data set (colum)
print(means["Close"])