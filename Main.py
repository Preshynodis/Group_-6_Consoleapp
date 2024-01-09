# I defined the number Api

from urllib.request import urlopen
from datetime import datetime
import json

#function for numbers api
def numbersapi_url():
    BASE_URL_1 = "http://numbersapi.com/"
    print("""
        Welcome to the Numbers App
        Input the day and month you want to know about.
        """)
    month = int(input("Enter a month(1-12): "))

    day = int(input("Enter a day(1-31): "))
    url = BASE_URL_1 + str(month) + "/" + str(day) + "/date"  # Corrected URL

    with urlopen(url) as response:
        data = response.read().decode()  # Decoding the response to a string

    # If the API returns JSON, parse it with json.loads. If it's plain text, adjust accordingly.
    try:
        data = json.loads(data)
    except json.JSONDecodeError:
        # Handle plain text or other formats here
        pass

    print(data)

    #functin to get the data of from the covid API
def get_data(date=None, iso=None):
    url = BASE_URL_2 + "reports/total?date=" + date
    if iso:
        url += "&iso=" + iso
    print("Fetching data...")
    with urlopen(url) as response:
        data = response.read()
    data = eval(data)
    data = data["data"]
    if not data:
        print("No data found for the given date and country code")
        return
    print("Total Confirmed Cases: ", data["confirmed"])
    print("Total Active Cases: ", data["active"])
    print("Total Deaths: ", data["deaths"])
    print("New Cases: ", data["confirmed_diff"])
    print("New Deaths: ", data["deaths_diff"])
    print("Total Recovered: ", data["recovered"])
    
    BASE_URL_2 = "https://covid-api.com/api/"
 
#main function for covid API using the get_data function
def covid19():
    print(
        """Welcome to the COVID-19 Tracker App
        Please select from the following options:
        1. Global Data
        2. Country Data
        3. See the list of countries
        4. Exit
        """
    )
    choice = input("Enter your choice: ")
    if choice == "4":
        exit()
    elif choice == "3":