import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_palette("husl")


def plot_visuals():

    # READ DATA FROM .CSV GENERATED FROM SCRAPER.PY
    stock_data = pd.read_csv('apple_historical.csv', parse_dates=['DATE'], index_col=[0])
    stock_data['HIGH'] = stock_data['HIGH'].str.replace(',', '').str.replace('$', '').astype(float).round(2)
    stock_data['LOW'] = stock_data['LOW'].str.replace(',', '').str.replace('$', '').astype(float).round(2)
    stock_data['OPEN'] = stock_data['OPEN'].str.replace(',', '').str.replace('$', '').astype(float).round(2)
    stock_data['CLOSE'] = stock_data['CLOSE'].str.replace(',', '').str.replace('$', '').astype(float).round(2)
    stock_data['VOLUME'] = stock_data['VOLUME'].str.replace(',', '').astype(float).round(2)
    print(stock_data.head())
    print(stock_data.info())
    print(stock_data.dtypes)
    print(stock_data.index)

    # CREATE FIGURE AND PLOT SPACE FOR SCATTER PLOT
    fig, ax = plt.subplots(figsize=(15, 8))
    close = ax.scatter(stock_data.index, stock_data['CLOSE'], color='blue', label='Close', linewidth=0.5, alpha=0.5)
    high = ax.scatter(stock_data.index, stock_data['HIGH'], color='green', label='High', linewidth=0.5, alpha=0.3)
    low = ax.scatter(stock_data.index, stock_data['LOW'], color='red', label='Low', linewidth=0.5, alpha=0.3)
    plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1, loc='upper left', handles=[high, low, close],
               frameon=True, title='1-Year Stock History')
    ax.set(xlabel='Date', ylabel='Stock Value $', title='Apple Historical Price Data\n(Scatter-Plot)')

    # CHANGE THE DIRECTORY LOCATION BELOW TO WHERE YOU WANT TO SAVE THE PLOT
    plt.savefig('C:/Users/Paul/PycharmProjects/StockPrediction/scatter.png')
    plt.show()

    # CREATE FIGURE AND PLOT SPACE FOR BAR GRAPH
    fig2, ax2 = plt.subplots(figsize=(10, 7))
    ax2.bar(stock_data.index, stock_data['LOW'], color='green')  # Add x-axis and y-axis
    ax2.set(xlabel='Date', ylabel='Closing Price', title='Apple 1 Year Historical Price Data\nbar graph')
    plt.setp(ax2.get_xticklabels(), rotation=45)  # Rotate tick marks on x-axis

    # CHANGE THE DIRECTORY LOCATION BELOW TO WHERE YOU WANT TO SAVE THE PLOT
    plt.savefig('C:/Users/Paul/PycharmProjects/StockPrediction/bar.png')
    plt.show()

    # CREATE FIGURE AND PLOT SPACE FOR KDE PLOT
    sns.kdeplot(stock_data['HIGH'], label='high', shade=True)
    sns.kdeplot(stock_data['LOW'], label='low', shade=True)
    plt.title('Apple KDE Plot')
    plt.xlabel('Low and High Stock Price (year to date)')
    plt.ylabel('')

    # CHANGE THE DIRECTORY LOCATION BELOW TO WHERE YOU WANT TO SAVE THE PLOT
    plt.savefig('C:/Users/Paul/PycharmProjects/StockPrediction/KDE.png')
    plt.show()

    # CREATE FIGURE AND PLOT SPACE FOR STOCK PRICE AND TRADING VOLUME GRAPH
    top = plt.subplot2grid((4, 4), (0, 0), rowspan=2, colspan=4)
    top.plot(stock_data.index, stock_data["CLOSE"], color='blue')
    plt.title('Apple 1 Year Stock Price')
    bottom = plt.subplot2grid((4, 4), (3, 0), rowspan=4, colspan=4)
    bottom.bar(stock_data.index, stock_data["VOLUME"], color='black')
    plt.title('Apple Trading Volume', loc="center")
    plt.gcf().set_size_inches(15, 8)

    # CHANGE THE DIRECTORY LOCATION BELOW TO WHERE YOU WANT TO SAVE THE PLOT
    plt.savefig('C:/Users/Paul/PycharmProjects/StockPrediction/priceandvolume.png')
    plt.show()

    return


# Function Call
plot_visuals()