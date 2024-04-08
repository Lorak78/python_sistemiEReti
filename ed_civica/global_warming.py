import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

anniPPM = []
anniTemp = []
anniPopulation = []
ppm_CO2 = []
temp_difference = []
population = []
data_filePPM = open("./co2ppm.csv")
data_readerPPM = csv.reader(data_filePPM, delimiter=',')
data_fileTemp = open("./temperature_anomaly.csv")
data_readerTemp = csv.reader(data_fileTemp, delimiter=',')
data_filePopulation = open("./world_population.csv")
data_readerPopulation = csv.reader(data_filePopulation, delimiter=',')

for row in data_readerPPM:
    anniPPM.append(int(row[0]))
    ppm_CO2.append(float(row[1]))

for row in data_readerTemp:
    anniTemp.append(int(row[0]))
    temp_difference.append(float(row[1]))

for row in data_readerPopulation:
    anniPopulation.append(int(row[0]))
    population.append(float(row[1]))

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.suptitle("Ricerca Dati e correlazioni/causalità: Global Warming")

ax1.plot(anniTemp, temp_difference,'-g')
ax1.set_xlabel('Anni')
ax1.set_ylabel('Anomalia temperatura (°C)')

ax2.plot(anniPPM, ppm_CO2, 'o-r')
ax2.set_xlabel('Anni')
ax2.set_ylabel('CO2 (ppm)')

ax3.plot(anniPopulation, population, 'o-b')
ax3.set_xlabel('Anni')
ax3.set_ylabel('Popolazione (miliardi)')
fig.tight_layout()

plt.show()