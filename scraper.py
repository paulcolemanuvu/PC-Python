import pandas as pd
import time
from selenium import webdriver


def scrape():

    # CREATE A PANDAS DATA-FRAME TO STORE THE SCRAPED DATA
    df = pd.DataFrame(index=range(20),
                      columns=['DATE', 'CLOSE', 'VOLUME',
                               'OPEN', 'HIGH', 'LOW'])

    # SETTING BROWSER PROPERTIES AND LAUNCHING THE CHROME BROWSER
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe', options=chrome_options)
    browser.maximize_window()
    browser.execute_script("document.body.style.zoom='80%'")
    url_form = "https://www.nasdaq.com/"
    browser.get(url_form)
    time.sleep(3)

    symbols = ["AAPL"]  # Enter a company index value here

    # NAVIGATE TO 'SYMBOL' INPUT SEARCH BOX; CLICK IT AND TYPE IN SYMBOL
    for company in range(len(symbols)):
        browser.find_element_by_xpath('//*[@id="find-symbol-input"]').send_keys(symbols[company])
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[2]/div/main/div/div[2]/section[1]/div/div[1]/div['
                                      '1]/form/div/div/button[2] ').click()  # Click search box submit button
        time.sleep(1)
        browser.find_element_by_xpath('// *[ @ id = "_evidon-decline-button"]').click()  # Accept Cookies. Closes popup
        browser.find_element_by_link_text('Historical Quotes').click()  # Navigate to Historical Quotes
        time.sleep(2)
        browser.find_element_by_css_selector("button[aria-label='Click to show data for 1 year']").click()
        next_page_button = browser.find_element_by_class_name("pagination__next")
        num_of_rows = 0
        time.sleep(1)
        browser.find_element_by_css_selector("div[hs-name='Close Button']").click()
        time.sleep(1)

        # LOOP AND STORE STOCK INDEX DATA FROM 1 YEAR AGO TO TODAY FROM ALL TABLE ROWS
        while next_page_button.is_enabled():

            date = []
            close_price = []
            volume = []
            open_price = []
            high_price = []
            low_price = []

            historical_data = browser.find_elements_by_class_name("historical-data__row")

            # FILL THE PANDAS DATAFRAME WITH THE SCRAPED DATA
            for row in historical_data:
                temp = row.text
                date.append(temp.split(" ")[0])
                close_price.append(temp.split(" ")[1])
                volume.append(temp.split(" ")[2])
                open_price.append(temp.split(" ")[3])
                high_price.append(temp.split(" ")[4])
                low_price.append(temp.split(" ")[5])

            for i in range(1, len(date)):
                df.loc[num_of_rows, 'DATE'] = date[i]
                df.loc[num_of_rows, 'CLOSE'] = close_price[i]
                df.loc[num_of_rows, 'VOLUME'] = volume[i]
                df.loc[num_of_rows, 'OPEN'] = open_price[i]
                df.loc[num_of_rows, 'HIGH'] = high_price[i]
                df.loc[num_of_rows, 'LOW'] = low_price[i]
                num_of_rows = num_of_rows + 1

            # NAVIGATE TO THE NEXT PAGE IN HISTORICAL DATA UNTIL END
            browser.find_element_by_css_selector("button[aria-label='click to go to the next page']").click()
            time.sleep(2)

        browser.quit()

    # CREATE AND SAVE A CSV FILE OF THE SCRAPED DATA TO THE WORKING DIRECTORY
    df.to_csv("apple_historical.csv", index=False)
    return


# FUNCTION CALL
scrape()