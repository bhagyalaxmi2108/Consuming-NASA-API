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

6. Now that our environment is ready, we need to call the Open NASA API
   - Type the following in the terminal.
     ```
     $ python asteroid.py
     ```
   - The above command will run a interactive window. Depending on the choices, it'll make APOD or Asteroid NeoWs API calls. Every time on running this, `NASA_OPEN_API.xlsx` will be created which will have as many worksheets as per the no.of choices, each one storing data received from the API calls based on the choices. 
   - In case, the input data is wrong, the worksheet will record the error that it faced

