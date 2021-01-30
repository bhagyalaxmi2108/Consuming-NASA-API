import requests
import socket
import xlsxwriter
import ast

file = open('api_key.txt', 'r')
api_file = ast.literal_eval(file.read())

api_key = api_file.get("api_key")

URL_APOD = "https://api.nasa.gov/planetary/apod"

date = '2021-01-30'
params = {
    'api_key': api_key,
    'date': date,
    'hd': 'True'
}

response = requests.get(URL_APOD, params=params).json()

hostname = "apod.nasa.gov"
ip_address = socket.gethostbyname(hostname)

workbook = xlsxwriter.Workbook('apod_data.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

col = 0

for key, values in response.items():

    worksheet.set_column(0, col, 15)
    worksheet.set_column(1, col, 15)
    worksheet.write(0, col, key, bold)
    worksheet.write(1, col, values)
    col += 1

worksheet.set_column(0, col, 25)
worksheet.set_column(1, col, 25)
worksheet.write(0, col, "ip_address", bold)
worksheet.write(1, col, ip_address)

workbook.close()
