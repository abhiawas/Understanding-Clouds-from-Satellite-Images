import os
cwd = os.getcwd()
os.chdir(r"D:\understanding_cloud_organization")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import seaborn as sns

import plotly.graph_objs as go

traincsv = pd.read_csv("train.csv")

traincsv.head()

Emptyp = (traincsv.EncodedPixels.isna().sum())
allp = traincsv.EncodedPixels.count()



plt.style.use('ggplot')

x = ['Empty', 'NonEmpty']
y = [Emptyp , allp]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, y, color='cyan')
plt.xlabel("Encoded Pixels")
plt.ylabel("Count")

plt.xticks(x_pos, x)

for i, v in enumerate(y):
    plt.text(x_pos[i] - 0.1, v + 0.5, str(v))


plt.show()


###
traincsv['Image'] = traincsv['Image_Label'].apply(lambda x: x.split('_')[0])
traincsv['Classlable'] = traincsv['Image_Label'].apply(lambda x: x.split('_')[1])


pp = traincsvnonan['Encoded_Pixels = nan'].value_counts()


traincsvnonan = traincsv.dropna()

traincsvnonan.head()
Classlables = ['Fish', 'Flower', 'Gravel', 'Sugar']
nb_Classlabels = []
for item in Classlables:
    nb_class = traincsvnonan['Classlable'].str.count(item)
    nb_Classlabels.append(nb_class[nb_class == 1].count())

pp = traincsvnonan['Classlable'].value_counts()

patterns = fpg.find_frequent_patterns(labelcount['labels'], 2)
patternsdf = pd.DataFrame({'Label Association': list(patterns.keys()), 'Occurrences': list(patterns.values())})

#####################################################################################################################
Classcounts = ['1', '2', '3', '4']
nb_Classcounts = []
for item in Classcounts:
    nb_classc = traincsvnonan['Classlable'].str.count(item)
    nb_Classlabels.append(nb_class[nb_class == 1].count())


import matplotlib.pyplot as plt
# Pie chart
labels = ['Fish', 'Flower', 'Gravel', 'Sugar']
sizes = nb_Classlabels
#colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90)
#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.show()


plt.style.use('ggplot')

x_pos = [i for i, _ in enumerate(labels)]

plt.bar(x_pos, sizes, color = colors)
#plt.xlabel("Cloud Class Lables")
#plt.ylabel("Count")
#plt.title("Class Distribution")

plt.xticks(x_pos, labels)

for i, v in enumerate(sizes):
    plt.text(x_pos[i] - 0.19, v + 0.5, str(v))
plt.show()


class_counts = traincsvnonan.dropna(subset=['EncodedPixels']).groupby('Image')['Classlable'].nunique()
pc = class_counts.value_counts()

Classc = [ '2', '3','1', '4']
plt.style.use('ggplot')
x_pos = [i for i, _ in enumerate(Classc)]
plt.bar(x_pos, pc, color = '#66b3ff')
plt.xlabel("No.of masks (Classes)")
plt.ylabel("No.of Iamges")
#plt.title("Class Distribution")

plt.xticks(x_pos, Classc)

for i, v in enumerate(pc):
    plt.text(x_pos[i] - 0.19, v + 0.5, str(v))

plt.show()