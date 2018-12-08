import pandas as pd
import lxml
import numpy as np
import matplotlib.pyplot as plt
username = input()
tables = pd.read_html("https://codeforces.com/contests/with/"+username)
Y = []
for i in tables[5]['Rating change']:
  Y.append(i)
Y = Y[::-1]
print(Y)
plt.plot(Y,color='black',linewidth=0.5)
X = np.arange(len(Y))
X = X + 1
plt.xticks(X)
plt.tick_params(axis='both', which='major', labelsize=7)
plt.grid()
plt.ylabel("changes")
for idx,i in enumerate(Y):
    plt.scatter(idx,i,marker=r"$ {} $".format(i),s=150)
plt.show()
