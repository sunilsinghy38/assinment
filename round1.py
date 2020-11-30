import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

download_url = ("https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv")

df = pd.read_csv(download_url)

print(df.head())

rcParams["figure.figsize"]= 10,10

df.plot(x="Rank", y=["Full_time", "Part_time", "Unemployment_rate"], kind="line")

plt.grid(True, color="k", linestyle=":")

plt.show()

