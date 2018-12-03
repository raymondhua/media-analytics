import mysql.connector
import csv
from datetime import datetime
import re
import sys

find = re.compile("^(.*)\..*")
fn = sys.argv[1]
m = re.match(find, fn)
year = m.group(1)

def insertCSVFile(file_obj):
    mydb = mysql.connector.connect(
        host="10.25.100.30",
        user="root",
        passwd="HelloRay12",
        database="mediaanalytics")
    reader = csv.DictReader(file_obj, delimiter=',')
    count = 0
    countSkip = 0
    print ('Inserting CSV file into database...')
    query = "INSERT INTO mediaanalytics_article (title, text, author, date, url, section) VALUES (%s,%s,%s,%s,%s,%s);"
    mycursor = mydb.cursor()
    for line in reader:
        text = line["article"].replace(".,", ". <p></p>")
        author = line["author"].lower().title()
        date = line["dop"].lower().title()
        title = line["title"].lower().title()
        url = line["url"]
        section = line["section"]
        if(("Jan." in date) or ("Feb." in date) or ("Aug." in date) or ("Sept." in date) or ("Oct." in date) or ("Nov." in date) or ("Dec." in date)):
            if "Jan." in date: 
                date = date.replace("Jan.","January")
            if "Feb." in date: 
                date = date.replace("Feb.","February")
            if "Aug." in date: 
                date = date.replace("Aug.","August")
            if "Sept." in date: 
                date = date.replace("Sept.","September")
            if "Oct." in date: 
                date = date.replace("Oct.","October")
            if "Nov." in date: 
                date = date.replace("Nov.","November")
            if "Dec." in date: 
                date = date.replace("Dec.","December")
        if(' 1, ' in date):
            date = date.replace(" 1, "," 01, ")
        if(' 2, ' in date):
            date = date.replace(" 2, "," 02, ")
        if(' 3, ' in date):
            date = date.replace(" 3, "," 03, ")
        if(' 4, ' in date):
            date = date.replace(" 4, "," 04, ")
        if(' 5, ' in date):
            date = date.replace(" 5, "," 05, ")
        if(' 6, ' in date):
            date = date.replace(" 6, "," 06, ")
        if(' 7, ' in date):
            date = date.replace(" 7, "," 07, ")
        if(' 8, ' in date):
            date = date.replace(" 8, "," 08, ")
        if(' 9, ' in date):
            date = date.replace(" 9, "," 09, ")
        #If no rows have blank coloums the query is inserted into the database
        if((text!='') and (date!="") and (author!='') and (title!="") and (url!='') and (section!="") and (year in date)):
            date = datetime.strptime(date, '%B %d, %Y').date()
            val = (title, text, author, date, url, section)
            mycursor.execute(query, val)
            mydb.commit()
            print (title + " inserted")
            count = count + 1
        else:
            countSkip = countSkip + 1
    print("%s articles added" % (count))
    print("%s articles skipped" % (countSkip))
    
if __name__ == "__main__":
    fileName = sys.argv[1]
    with open(fileName, encoding="utf8") as f_obj:
        insertCSVFile(f_obj)