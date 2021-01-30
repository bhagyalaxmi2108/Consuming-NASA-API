import requests
import socket
import xlsxwriter
import ast

file = open('api_key.txt', 'r')
api_file = ast.literal_eval(file.read())

api_key = api_file.get("api_key")

hostname = "api.nasa.gov"
ip_address = socket.gethostbyname(hostname)

def fetchAsteroidNeowsFeed():
    URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        'api_key':api_key,
        'start_date':'2021-01-30',
        'end_date':'2021-01-30'
    }

    response = requests.get(URL_NeoFeed,params=params).json()

    hostname = "api.nasa.gov"
    ip_address = socket.gethostbyname(hostname)
    
    return response


def fetchAsteroidNeowsLookup():
    asteroid_id = '3542519'
    URL_NeoLookup = "https://api.nasa.gov/neo/rest/v1/neo/"+ asteroid_id
    params = {
        'api_key':api_key
    }
    response = requests.get(URL_NeoLookup,params=params).json()
    return response

def fetchAsteroidNeowsBrowse():
    URL_NeoBrowse = "https://api.nasa.gov/neo/rest/v1/neo/browse/"
    params = {
        'api_key':api_key
    }
    response = requests.get(URL_NeoBrowse,params=params).json()
    return response

response1  = fetchAsteroidNeowsFeed()
response2  = fetchAsteroidNeowsLookup()
response3  = fetchAsteroidNeowsBrowse()

workbook = xlsxwriter.Workbook('asteroid_data.xlsx')
worksheet1 = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet()
worksheet3 = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

def write_to_excel(worksheet, response):

    col=0
        
    for key, values in response.items():

        worksheet.set_column(0, col, 25)
        worksheet.set_column(1, col, 25)
        worksheet.write(0, col, key, bold)
        worksheet.write(1, col, str(values))
        col+=1

    worksheet.set_column(0, col, 25)
    worksheet.set_column(1, col, 25)
    worksheet.write(0, col, "ip_address", bold)
    worksheet.write(1, col, ip_address)


write_to_excel(worksheet1, response1)
write_to_excel(worksheet2, response2)
write_to_excel(worksheet3, response3)


workbook.close()