from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt


cotacao = web.DataReader("TAEE11.SA", data_source="yahoo", start="03-27-2019", end="09-15-2022")

print(cotacao)

"""cotacao["Close"].plot()
plt.show()"""