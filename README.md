# Consuming-NASA-API

This is a simple python integration to the following two Open NASA API:
- APOD – Astronomy Picture of the Day
- Asteroids – Neows (Near Earth Object Web Service)


## Motivation

The main aim of this integration is to 
- make API call to Open NASA API.
- capture remote IP address
- store the json received from the API call in excel file

## How to?

To get the following project running, follow the steps below.

1. Open up your terminal and clone this repository:
```
git clone https://github.com/bhagyalaxmi2108/Consuming-NASA-API.git
```

2. Set up and activate the virtual environment:
##### For Linux
```
$ pip3 install pipenv
$ virtualenv venv
$ source venv/bin/activate
```
##### For Windows
```
$ pip install virtualenv
$ python -m venv myenv
$ .\myenv\Scripts\activate
```

3. Make sure you're in inside the directory. Install the required libraries:
```
$ pip3 install -r requirements.txt
```
4. Before running the application, we need an API key. This can be obtained from [NASA Open APIs](https://api.nasa.gov/)

5. In the cloned repository, create an `.env` file and store API key and urls in it

6. Now that our environment is ready, call the Open NASA API
   - For APOD api call: 
     - Type the following in the terminal.
     ```
     $ python3 apod.py
     ```
     - This will make an API call followed by storing the json returned in an excel file named `apod_data.xlsx`

   - For Asteroids - NeoWs, user can search for Asteroids based on their closest approach date to Earth, lookup a specific Asteroid with its NASA JPL small body id, and browse the overall data-set. `asteroid.py` defines three fuctions for each one of these to make three different API calls. 
     - Type the following in the terminal.
     ```
     $ python asteroid.py
     ```
     - This will similarly make API calls and store the json returned in an excel file named `asteroid_data.xlsx`
     - This file will have three worksheet, each one storing data received from the API calls made by the three functions.

