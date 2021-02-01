import requests
import socket
import ast
from xlsxwriter import Workbook
from write_to_excel import write_to_excel
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_apod(api_key: str, date: str, url_apod: str):

    params = {"api_key": api_key, "date": date, "hd": "True"}

    response = requests.get(url_apod, params=params).json()

    return response


def main():

    api_key = os.getenv('api_key')

    url_apod = os.getenv('url_apod')

    hostname = "apod.nasa.gov"
    ip_address = socket.gethostbyname(hostname)

    date = "2021-01-30"

    response= fetch_apod(api_key=api_key, date=date, url_apod=url_apod)

    workbook = Workbook('apod_data.xlsx')

    write_to_excel(workbook=workbook, response=response, ip_address=ip_address)

    workbook.close()

if __name__ == "__main__":

    main()
