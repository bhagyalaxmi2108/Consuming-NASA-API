import requests
import socket
from xlsxwriter import Workbook
import ast
from write_to_excel import write_to_excel
from dotenv import load_dotenv
import os

load_dotenv()


def fetch_asteroid_neows_feed(api_key, url_neo_feed, start_date, end_date):

    params = {"api_key": api_key, "start_date": start_date, "end_date": end_date}
    response = requests.get(url_neo_feed, params=params).json()
    return response


def fetch_asteroid_neows_lookup(api_key, url_neo_lookup, asteroid_id):

    url = url_neo_lookup + asteroid_id

    params = {"api_key": api_key}
    response = requests.get(url, params=params).json()
    return response


def fetch_asteroid_neows_browse(api_key, url_neo_browse):

    params = {"api_key": api_key}
    response = requests.get(url_neo_browse, params=params).json()
    return response

def main():

    api_key = os.getenv('api_key')

    url_neo_feed = os.getenv('url_neo_feed')
    url_neo_lookup = os.getenv('url_neo_lookup')
    url_neo_browse = os.getenv('url_neo_browse')

    hostname = "api.nasa.gov"
    ip_address = socket.gethostbyname(hostname)

    start_date = "2021-01-30"
    end_date = "2021-01-30"

    asteroid_id = "3542519"

    response_neo_feed = fetch_asteroid_neows_feed(api_key=api_key, url_neo_feed=url_neo_feed, start_date=start_date, end_date=end_date)
    response_neo_lookup = fetch_asteroid_neows_lookup(api_key=api_key, url_neo_lookup=url_neo_lookup, asteroid_id=asteroid_id)
    response_neo_browse = fetch_asteroid_neows_browse(api_key=api_key, url_neo_browse=url_neo_browse)

    workbook = Workbook('asteroid_data.xlsx')

    write_to_excel(workbook=workbook, response=response_neo_feed, ip_address=ip_address)
    write_to_excel(workbook=workbook, response=response_neo_lookup, ip_address=ip_address)
    write_to_excel(workbook=workbook, response=response_neo_browse, ip_address=ip_address)

    workbook.close()

if __name__=='__main__':

    main() 