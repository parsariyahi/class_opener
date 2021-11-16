import csv
import datetime as dt
import webbrowser as wb

"""
the path of chrome.exe
in path use {  /  } instead of {  \  }
"""
CHROME_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"


#list of classes informations
all_classes = []

#list of today classes
today_classes = []

#number of weekdays --- o => monday _ 6 => sunday
today = dt.date.today().weekday()

#current time
current_hour = dt.datetime.now().hour


"""
open the CSV file
append classes into a list to use 
"""
with open('classes.csv', newline='') as file :
    classes = csv.reader(file)
    for clas in classes :
        all_classes.append(clas)

#get today classes
for clas in all_classes :
    if int(clas[2]) == today :
        today_classes.append(clas)

start = dt.time.fromisoformat(today_classes[0][3]).hour - 1 #start time
end = dt.time.fromisoformat(today_classes[0][4]).hour + 1 #end time

#if you have class now it will open it in chrome
if start <= current_hour <= end:
    url = today_classes[0][0]
    wb.get(CHROME_PATH).open_new_tab(url)
else :
    print('you dont have any class right now')
    
