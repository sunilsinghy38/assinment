import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
w=0.4
plt.style.use('bmh')
download_url = ("https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv")
df = pd.read_csv(download_url)
x = df['Rank']
college_job = df['College_jobs']
non_college_job = df['Non_college_jobs']
bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]
plt.bar(bar1,college_job,w,label="college_job")
plt.bar(bar2,non_college_job,w,label="non_college_job")

plt.xlabel('College Rank')
plt.ylabel("Jobs")
plt.legend()
plt.xticks(bar1,x)
plt.show()
