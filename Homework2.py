# Nnanna Nwoke(1462586)
# CIS 2348
# Homework 2

def find(month_in_date):
    month_to_num = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
                  "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    try:
        year = month_in_date.split(",")[-1].strip() # Splits dictionary by comma and gets last item
        month = month_in_date.split(",")[0].split()[0] # Splits dictionary by comma and by blank space
        day = month_in_date.split(",")[0].split()[-1] # Splits dictionary by comma and gets last item
        convert_month = month_to_num[month]
        int(year)
        int(day)
        return str(convert_month) + "/" + day + "/" + year
    except:
        return ""




with open("inputDates.txt") as file: # Read file
   for x in file.readlines():  # loop line by line
        if x.strip() != "-1": # Check if -1 is entered
             result = find(x.strip()) # print result
             if result != "": # checks if result is valid
                with open("parsedDate.txt","a+") as w:
                    w.write(result+"\n") # Writes to file
