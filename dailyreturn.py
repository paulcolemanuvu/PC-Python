import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def calculate_daily_return():
    
    # Read dataframe object
    cdr = pd.read_csv('apple_historical.csv')

    # Convert str to float and round to 2 decimals
    cdr['CLOSE'] = cdr['CLOSE'].str.replace(',', '').str.replace('$', '').astype(float).round(2)

    # Correct the format of DATE
    cdr['DATE'] = pd.to_datetime(cdr.DATE)

    # Set DATE column as row index
    cdr = cdr.set_index('DATE')

    # Calculate the daily returns
    daily_return = cdr['CLOSE'].pct_change()

    # Create new column and assign daily return values to it
    cdr['daily_return'] = daily_return

    # Label names for x and y axis
    plt.ylabel('Percentage Change\n(Risk)')
    plt.xlabel('')

    cdr['daily_return'].plot(legend=True, figsize=(15, 7), label='Daily Return')
    plt.title("Daily Return")

    # Change the directory location below to where you want to save the plot
    plt.savefig('C:/Users/Paul/PycharmProjects/StockPrediction/dailyreturn.png')
    plt.show()
    return


# Changes plot default color palette from matplotlib to seaborn
sns.set_palette('husl')
calculate_daily_return()
