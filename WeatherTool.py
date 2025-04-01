import requests
import json
import os
LogNum = 0
API_KEY = "23db7c3f79974942ab2234108252803"
def Forecastjson():
    User_pos_not = input("Enter Location: ")
    User_pos = User_pos_not.capitalize()
    aqichoice = input("Would you like air quality alerts? (yes/no): ")
    alertchoice = input("Would you like weather alerts? (yes/no): ")
    Dayamount = input("Number of days to forecast (1-14): ")
    URLNOARGS = "http://api.weatherapi.com/v1/"+UrlPrefix+"?key="+API_KEY+"&q="+User_pos+"&days="+Dayamount+"&aqi="+aqichoice+"&alerts="+alertchoice
    rescode = requests.get(URLNOARGS)
    print("Getting data from: ", URLNOARGS)
    print("Status Code: ",rescode)
    rescode.raise_for_status()

    API_DATA = rescode.json()
    print(API_DATA)
    copyA = input("Would you like to log the data? \n (y/n)?: ")
    copy = copyA.casefold()
    if copy == "y":
        API_DATA_STR = str(API_DATA)
        API_DATA_STR_DOUBLE_QOUTES = API_DATA_STR.replace("\'", '\"')
        API_DATA_PY = json.loads(API_DATA_STR_DOUBLE_QOUTES)
        API_DATA_PY_STR = str(API_DATA_PY)
        f = open('log.txt', "a")
        f.write(API_DATA_PY_STR)    
        f.close() 
        print("Copied")
        print("Hit CTRL-C to exit program (if run in terminal)")
    else:
        print("Ok!, Hit CTRL-C to exit program (if run in terminal)")



def currentjson():
    User_pos_not = input("Enter Location: ")
    User_pos = User_pos_not.capitalize()
    aqichoice = input("Would you like air quality alerts? (y/n): ")
    URLNOARGS = "http://api.weatherapi.com/v1/"+UrlPrefix+"?key="+API_KEY+"&q="+User_pos+"&aqi="+aqichoice
    rescode = requests.get(URLNOARGS)
    print("Getting data from: ", URLNOARGS)
    print("Status Code: ",rescode)
    rescode.raise_for_status()

    API_DATA = rescode.json()
    print(API_DATA)
    copyA = input("Would you like to copy the data? \n (y/n)?: ")
    copy = copyA.casefold()
    if copy == "y":
        API_DATA_STR = str(API_DATA)
        API_DATA_STR_DOUBLE_QOUTES = API_DATA_STR.replace("\'", '\"')
        API_DATA_PY = json.loads(API_DATA_STR_DOUBLE_QOUTES)
        API_DATA_PY_STR = str(API_DATA_PY)
        f = open('log.txt', "a")
        f.write(API_DATA_PY_STR)    
        f.close() 
        print("Copied")
        print("Hit CTRL-C to exit program (if run in terminal)")
    else:
        print("Ok!, Hit CTRL-C to exit program (if run in terminal)")

def alertsjson():
    User_pos_not = input("Enter Location: ")
    User_pos = User_pos_not.capitalize()
    URLNOARGS = "http://api.weatherapi.com/v1/"+UrlPrefix+"?key="+API_KEY+"&q="+User_pos
    rescode = requests.get(URLNOARGS)
    print("Getting data from: ", URLNOARGS)
    print("Status Code: ",rescode)
    rescode.raise_for_status()
    API_DATA = rescode.json()
    print(API_DATA)
    copyA = input("Would you like to copy the data? \n (y/n)?: ")
    copy = copyA.casefold()
    if copy == "y":
        API_DATA_STR = str(API_DATA)
        API_DATA_STR_DOUBLE_QOUTES = API_DATA_STR.replace("\'", '\"')
        API_DATA_PY = json.loads(API_DATA_STR_DOUBLE_QOUTES)
        API_DATA_PY_STR = str(API_DATA_PY)
        f = open('log.txt', "a")
        f.write(API_DATA_PY_STR)    
        f.close() 
        print("Copied")
        print("Hit CTRL-C to exit program (if run in terminal)")
    else:
        print("Ok!, Hit CTRL-C to exit program (if run in terminal)")

def astronomyjson():
    User_pos_not = input("Enter Location: ")
    User_pos = User_pos_not.capitalize()
    dt = input("Enter date (yyyy-MM-dd): ")
    URLNOARGS = "http://api.weatherapi.com/v1/"+UrlPrefix+"?key="+API_KEY+"&q="+User_pos+"&dt="+dt
    rescode = requests.get(URLNOARGS)
    print("Getting data from: ", URLNOARGS)
    print("Status Code: ",rescode)
    rescode.raise_for_status()

    API_DATA = rescode.json()
    print(API_DATA)
    copyA = input("Would you like to copy the data? \n (y/n)?: ")
    copy = copyA.casefold()
    if copy == "y":
        API_DATA_STR = str(API_DATA)
        API_DATA_STR_DOUBLE_QOUTES = API_DATA_STR.replace("\'", '\"')
        API_DATA_PY = json.loads(API_DATA_STR_DOUBLE_QOUTES)
        API_DATA_PY_STR = str(API_DATA_PY)
        f = open('log.txt', "a")
        f.write(API_DATA_PY_STR)    
        f.close() 
        print("Copied")
        print("Hit CTRL-C to exit program (if run in terminal)")
    else:
        print("Ok!, Hit CTRL-C to exit program (if run in terminal)")

print("Enter Data to pull:")
print("Current Forecast, CF")
print("Forecast, F")
print("Alerts, A")
print("Astronomy, AS")
print("Clear Log File, Clear")
user_choice = input("Enter Data to pull: ")
print(f"Pulling Data, '{user_choice}'.")
if user_choice == "CF":
    UrlPrefix = "current.json"
    currentjson()
elif user_choice == "F":
    UrlPrefix = "forecast.json"
    Forecastjson()
elif user_choice == "A":
    UrlPrefix = "alerts.json"
    alertsjson()
elif user_choice == "AS":
    UrlPrefix = "astronomy.json"
    astronomyjson()
elif user_choice == "Clear":
    LogNum = (LogNum+1)
    f = open('log.txt', "w")
    f.write("//")
    os.remove
else:
    print("What the hell?!, how in the holy hell did you pick something that doesnt exist?!?!")

if ModuleNotFoundError:
    print("Required modules were not found!, Please install the following python packages")
    print("requests")
    print("json")
    print("To install simply type 'pip install {module name}'")
    print("If you are seeing this after you selected to copy or not, Or if you selected 'Clear', Ignore this error message.")

