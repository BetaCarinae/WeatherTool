import requests
import json
import pyperclip
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
        f = open('log.txt')
        f.write(API_DATA)
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
        f = open('log.txt')
        f.write(API_DATA)
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
        pyperclip.copy(API_DATA)
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
        pyperclip.copy(API_DATA)
        print("Copied")
        print("Hit CTRL-C to exit program (if run in terminal)")
    else:
        print("Ok!, Hit CTRL-C to exit program (if run in terminal)")

print("Enter Data to pull:")
print("Current Forecast, CF")
print("Forecast, F")
print("Alerts, A")
print("Astronomy, AS")
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
else:
    print("What the hell?!, how in the holy hell did you pick something that doesnt exist?!?!")

if ModuleNotFoundError:
    print("Required modules were not found!, Please install the following python packages")
    print("Pyperclip")
    print("Terminal_menu")
    print("To install simply type 'pip install {module name}'")
