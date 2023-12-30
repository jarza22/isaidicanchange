"""
Python Project 1 - Data Processing
This Project is worth 100 points.
For this project, you are given a set of step-by-step instructions.
Write your code at the bottom of this file.
"""

"""
When gathering data from a Web service, it is common for that data to be collected
into a JSON (JavaScript Object Notation) file and then dumped inceremoniously into
a list. Developers must then consult the service API and write code that processes
into something their application can use.

In this project, you will learn how to map a 2-dimensional list into a more usable
format - in this case, a list of dictionaries. You will then iterate over the new
list to generate and display a report.

The list you will process contains the following data.
    data[x][0]: Account Number
    data[x][1]: First Name
    data[x][2]: Last Name
    data[x][3]: Type (Checking, Savings, or CD)
    data[x][4]: Balance
"""

#Here is your data.
data = [
    ["1928661700", "Jason", "Brody", "Checking", 600],
    ["1928661701", "Maria", "Tilly", "Savings", 15000],
    ["1928661702", "Ashley", "Doiley", "CD", 56200],
    ["1928661703", "Satoshi", "Tachibana", "Checking", 2200],
    ["1928661704", "Katya", "Szymanski", "Checking", 1800],
    ["1928661705", "Jayant", "Mathew", "CD", 2900],
    ["1928661706", "Liu", "Xiaotong", "Saving", 6000],
    ["1928661707", "Sinh", "Nguyen", "Checking", 7350],
    ["1928661708", "Dontrel", "Jackson", "Savings", 21500],
    ["1928661709", "Cristobal", "Garcia", "CD", 100000],
    ]

"""
Follow these steps.
1. Create an empty list called accountsList.
2. Create a loop that will iterate over each account in data. For each account...
    a. Create an empty dictionary called accountInfo.
    b. Assign accountInfo the following key-value pairs with the appropriate data.
        1. accounts["accountnumber"]
        2. accounts["name"] (DO NOT assign first and last name separately.)
        3. accounts["type"] (Change this to all caps.)
        4. accounts["balance"] (Remember to stringify this!)
    c. Append the completed dictionary to accountsList.
3. Create an empty string called accountsInfo.
4. Create a second loop to iterate over accountsList. For each entry...
    a. Create a string called entryInfo. It should contain a newline character.
    b. Create a third loop to iterate over the key-value pairs of entry. For each key...
        1. Create a string called item, which should contain "[key]: [value]" and end with a newline character.
        2. Append item to entryInfo.
    c. Append entryInfo to accountsInfo.
5. Print accountsInfo.
6. Take a screenshot of your terminal showing the code executed successfully.
7. Compress your completed project file and screenshot into a ZIP folder named FirstLast_CS230_Project1. Replace FirstLast with your name.
8. Submit the ZIP folder on Canvas.
"""

accountsList = []

for accounts in data:
    accountInfo = {}

    accountInfo["Account Number:"] = accounts[0]
    accountInfo["Full Name:"] = f"{accounts[1]} {accounts[2]}"
    accountInfo["Type:"] = accounts[3].upper()
    accountInfo["Balance:"] = str(accounts[4])

    accountsList.append(accountInfo)

accountsInfo = ""    

for entry in accountsList:
    entryInfo = "\n"
    for key, value in entry.items():
        item = f"{key} {value}\n"
        entryInfo += item

    accountsInfo += entryInfo

print(accountsInfo)    
