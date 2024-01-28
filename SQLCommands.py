import mysql.connector
import csv
import random

def rand(x, z, k):
    if z <= 0:
        return k
    else:
        index = random.choice(range(len(x)))
        k.append(x[index])
        return rand(x, z-1, k)
    

# Importing module 

# Creating connection object
mydb = mysql.connector.connect(

)
countrylst = []
country = open('countries.csv', 'r')
for i in country:
    i = i[:-1]
    countrylst.append(i)
typelst = ["breakfast", "lunch", "dinner", "sweet", "drinks"]
foodtype = []
foodtype = rand(typelst, len(countrylst), foodtype)
    
print(countrylst)
print(foodtype)
print(len(foodtype))
cursor = mydb.cursor()
for i in range(0, len(countrylst)):
    cursor.execute("INSERT INTO country_food(Country,Type) VALUES('" + countrylst[i] + "', '" + foodtype[i] + "');")
    mydb.commit();

cursor.execute("SELECT * FROM country_food")

for x in cursor:
    print(x)