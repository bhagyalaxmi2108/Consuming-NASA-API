import requests
import socket
from xlsxwriter import Workbook
from dotenv import load_dotenv
import os
from write_to_excel import write_to_excel

# loads api_key and urls in .env file
load_dotenv()


def fetch_apod(api_key, url_apod):
    """
    Consumes the Astronomy Picture Of the Day (APOD) API response
    Args:
        api_key (int)
        url_apod (str)
        date (str)
    Returns:
        response (json)
    """

    date = input("Input the date for APOD(yyyy-mm-dd): ")
    params = {
        "api_key": api_key,
        "date": date,
        "hd": "True"
    }

    response = requests.get(url_apod, params=params).json()
    return response


def fetch_asteroid_neows_feed(api_key, url_neo_feed):
    """
    Consumes the list of Asteroids based on their closest approach date to Earth
    Args:
        api_key (int)
        url_neo_feed (str)
        start_date (str)
        end_date (str)
    Returns:
        response (json)
    """

    start_date = input("Input the start date for APOD(yyyy-mm-dd): ")
    end_date = input("Input the end date for APOD(yyyy-mm-dd): ")
    params = {
        "api_key": api_key,
        "start_date": start_date,
        "end_date": end_date
    }

    response = requests.get(url_neo_feed, params=params).json()
    return response


def fetch_asteroid_neows_lookup(api_key, url_neo_lookup):
    """
    Consumes details of a Asteroids based on their unique NASA-JPL small body id
    Args:
        api_key (int)
        url_neo_lookup (str) 
        asteroid_id (int)
    Returns:
        response (json)
    """

    asteroid_id = input("Input valid asteriod id(e.g. 3542519): ")
    url = url_neo_lookup + asteroid_id
    params = {
        "api_key": api_key
    }

    response = requests.get(url, params=params).json()
    return response


def fetch_asteroid_neows_browse(api_key, url_neo_browse):
    """
    Consumes overall Asteroid data-set
    Args:
        api_key (int)
        url_neo_browse (str)
    Returns:
        response (json)
    """

    params = {
        "api_key": api_key
    }

    response = requests.get(url_neo_browse, params=params).json()
    return response


def main():

    print("-"*60)
    print(" "*10, "Welcome to NASA Open API")
    print("-"*60)

    api_key = os.getenv('api_key')

    url_neo_feed = os.getenv('url_neo_feed')
    url_neo_lookup = os.getenv('url_neo_lookup')
    url_neo_browse = os.getenv('url_neo_browse')
    url_apod = os.getenv('url_apod')

    hostname = "api.nasa.gov"
    ip_address = socket.gethostbyname(hostname)

    # for each api calls, a workbook is created to store response data
    workbook = Workbook('NASA_Open_API.xlsx')
    file = os.path.abspath('NASA_Open_API.xlsx')

    while True:

        print("1. Consume Asteroid Pic Of the Day(APOD) API")
        print("2. Search for asteroids based on their closest approach date to Earth")
        print("3. Lookup for a specific Asteroid with its NASA-JPL small body id")
        print("4. Browse the overall data-set of asteroid.")
        print("5. To exit")
        ch = int(input("Enter your choice: "))

        if(ch == 1):
            response = fetch_apod(
                api_key=api_key,
                url_apod=url_apod
            )
            hostname = "apod.nasa.gov"
            ip_address = socket.gethostbyname(hostname)
            write_to_excel(
                workbook=workbook,
                response=response,
                ip_address=ip_address
            )

        elif (ch == 2):
            response_neo_feed = fetch_asteroid_neows_feed(
                api_key=api_key,
                url_neo_feed=url_neo_feed
            )
            write_to_excel(
                workbook=workbook,
                response=response_neo_feed,
                ip_address=ip_address
            )

        elif (ch == 3):
            response_neo_lookup = fetch_asteroid_neows_lookup(
                api_key=api_key,
                url_neo_lookup=url_neo_lookup
            )
            write_to_excel(
                workbook=workbook,
                response=response_neo_lookup,
                ip_address=ip_address
            )

        elif (ch == 4):
            response_neo_browse = fetch_asteroid_neows_browse(
                api_key=api_key,
                url_neo_browse=url_neo_browse
            )
            write_to_excel(
                workbook=workbook,
                response=response_neo_browse,
                ip_address=ip_address
            )

        elif (ch == 5):
            break

        else:
            print("Choice isn't valid.")
            continue

        print()
        print("Result has been stored in the following location: ")
        print(file)
        print("-"*60)
        print()

    workbook.close()


if __name__ == '__main__':

    main()
