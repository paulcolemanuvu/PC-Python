import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams
import pandas as pd


# CHANGE THE DIRECTORY BELOW TO THE LOCATION OF WHERE YOU HAVE SAVED THE convert.exe AND ffmpeg.exe
rcParams['animation.convert_path'] = r'C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\convert.exe'
rcParams['animation.ffmpeg_path'] = r'C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\ffmpeg.exe'

stock_data = pd.read_csv('apple_historical.csv', parse_dates=['DATE'], index_col=[0])
stock_data['HIGH'] = stock_data['HIGH'].str.replace(',', '').str.replace('$', '').astype(float).round(2)
stock_data['LOW'] = stock_data['LOW'].str.replace(',', '').str.replace('$', '').astype(float).round(2)
stock_data['OPEN'] = stock_data['OPEN'].str.replace(',', '').str.replace('$', '').astype(float).round(2)
stock_data['CLOSE'] = stock_data['CLOSE'].str.replace(',', '').str.replace('$', '').astype(float).round(2)

stock_data.mean(axis=0)
avg = []  # Create empty array
simulation = 1000  # Set the number of simulations to run

for i in range(2, simulation):
    a = (stock_data['LOW'], stock_data['HIGH'], i)
    avg.append(np.average(a))
current = avg[1:10]


# FUNCTION THAT WILL PLOT THE CURRENT HISTOGRAM
def clt(current):

    plt.cla()
    if current == 1000:
        current.event_source.stop()
    plt.hist(avg[0:current])
    plt.gca().set_title('Expected Price of Stock Index AAPL From 10 Random Samples')
    plt.gca().set_xlabel('Average 1 Year Price of Index AAPL')
    plt.gca().set_ylabel('Frequency/Sampling')
    plt.annotate('Sample Pick = {}'.format(current), [3, 10000])


# CREATE ANIMATION AND SAVE TO SELECTED FILE PATH
fig = plt.figure()
a = animation.FuncAnimation(fig, clt, interval=1)

# CHANGE THE SAVE DIRECTORY BELOW TO THE LOCATION YOU WANT THE GIF
a.save('C:/Users/Paul/PycharmProjects/StockPrediction/CLT.gif', writer='imagemagick', fps=10)
