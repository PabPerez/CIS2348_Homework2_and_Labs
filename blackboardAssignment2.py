#Pablo Perez
#1770045
from datetime import date

months = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6",
          "july": "7", "august": "8", "september": "9", "october": "10", "november": "11", "december": "12"}

file1 = open('inputDates.txt', 'r')
file2 = open('parsedDates.txt', 'w')

today = date.today()
currentMonth = today.month
currentDay = today.day
currentYear = today.year
val_list = list(months.values())

for line in file1:
    if line != "." or line != "-" or line != "/" or line != "-1":
        dateList = line.split()
        if len(dateList) >= 3:
            month = dateList[0]
            day = dateList[1]
            year = dateList[2]

            if month.lower() in months:
                comma = day[-1]
                if comma == ',':
                    day = day[:len(day) - 1]
                    currentMonth = months[month.lower()]
                    testDate = currentMonth + "/" + day + "/" + year

    testList = testDate.split("/")
    testMonth = testList[0]
    testDay = testList[1]
    testYear = testList[2]

    if int(testYear) <= currentYear:
        if int(testYear) == currentYear:
            if val_list.index(testMonth) + 1 <= int(currentMonth):
                if val_list.index(testMonth) + 1 == int(currentMonth):
                    if int(testDay) <= currentDay:
                        file2.write(testDate + "\n")
        #if val_list.index(testMonth) + 1 <= int(currentMonth):
            #if int(testDay) < currentDay:
                #file2.write(testDate + "\n")

###FIGURE OUT WHY IT'S NOT OUTPUTTING ANY CODE !!!

file2.close()
file1.close()