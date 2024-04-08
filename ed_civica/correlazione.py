import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

mesi_n = []
temp = []
voti = []
data_file = open("./dati.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader:
    mesi_n.append(int(row[1]))
    temp.append(float(row[2]))
    voti.append(float(row[3]))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle("Titolo")

ax1.plot(mesi_n, voti, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('')

ax2.plot(mesi_n, temp, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('')

plt.show()