from pandas_datareader import data
EFX = data.DataReader('EFX', 'yahoo',start = '2016/01/01', end = '2019/27/11')
print(EFX.head())
