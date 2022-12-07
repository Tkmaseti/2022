import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("tableone.xlsx")

counter = [] #future column you want

for string in df.Comments.values: #for each string in your "Comments"
    counter.append(string.count(' ') + 1) #num of spaces + 1

df['num_words'] = counter #add the column
df = df[['num_words', 'Comments']] #change the order of columns

# plt.show()
