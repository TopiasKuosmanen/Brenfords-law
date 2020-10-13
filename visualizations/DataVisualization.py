import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv('data/asiakaspaikat.csv', encoding='latin-1', usecols = ['ASIAKASPAIKAT'], sep=';')

#pd.read_csv('artwork_data.csv', encoding='latin-1', usecols = ['id'])


# New column with first char of id
Data['firstOfId'] = Data['ASIAKASPAIKAT'].astype(str).str[0]


print(Data.head())

Data1 = Data['firstOfId'].where((Data['firstOfId'] == '1'))
Result1 = Data1.dropna()
Data2 = Data['firstOfId'].where((Data['firstOfId'] == '2'))
Result2 = Data2.dropna()
Data3 = Data['firstOfId'].where((Data['firstOfId'] == '3'))
Result3 = Data3.dropna()
Data4 = Data['firstOfId'].where((Data['firstOfId'] == '4'))
Result4 = Data4.dropna()
Data5 = Data['firstOfId'].where((Data['firstOfId'] == '5'))
Result5 = Data5.dropna()
Data6 = Data['firstOfId'].where((Data['firstOfId'] == '6'))
Result6 = Data6.dropna()
Data7 = Data['firstOfId'].where((Data['firstOfId'] == '7'))
Result7 = Data7.dropna()
Data8 = Data['firstOfId'].where((Data['firstOfId'] == '8'))
Result8 = Data8.dropna()
Data9 = Data['firstOfId'].where((Data['firstOfId'] == '9'))
Result9 = Data9.dropna()


x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
x_index = np.arange(len(x))


palkit=[len(Result1.index), len(Result2.index), len(Result3.index), 
        len(Result4.index), len(Result5.index), len(Result6.index)
        , len(Result7.index), len(Result8.index), len(Result9.index)]
plt.bar(x, palkit, color=("Grey"), align="center")
plt.xlabel("")
plt.ylabel("")
plt.title("Brenfordin kaava anniskeluosastojen asiakaspaikkojen määrissä Suomessa")
plt.xticks(x_index, x, rotation=10)


