# Daily review use fetcher class get the cson data
#              use Tabletailor get the table data with parsor '|' and '<br>'

import os
import datetime
import pdb
import sys

import fetcher
import tablemd
import weeklyreview

## TODO: Seperate cson with writing and improve the UI by bash scripts
writefile = "test.cson"
weekfile = "/home/c7031195/Dropbox/Boostnote//notes/dcdec832-2203-44ec-b8b4-28ef78b1c207.cson"
dailyfile = "/home/c7031195/Dropbox/Boostnote//notes/c39b9947-b545-4a13-b05f-7b43e54568f8.cson"
weeknumber = datetime.date.today().isocalendar()[1]


## Read in the content
dailyreview =  fetcher.Fetcher(dailyfile)

#testing and prototyping
dailyreview.read_file()

## Read in tables
dailytable = tablemd.tablemd(dailyreview.content_data)
weekdata = weeklyreview.WeeklyReview(weekfile,weeknumber)

if datetime.datetime.today() == 5:
    print("Today is Saturday, Backing off...")
    sys.exit(0)

print "This is weekly plan"

weekdata.printReview()

print "Today plan is"
# First day is sunday: control loop of the day
week_day = (datetime.datetime.today().weekday() + 1 ) % 7 

# 6 Rows per week: control loop of the table
planIndex = 1
index_today = week_day % 6
index_tomorrow = (week_day + 1) % 6

dailytable.printElement(index_today, planIndex)


print "Try to be short, put `e` for next step."
print "please specify what is done:"
buffer = dailytable.getTableEntry(index_today, planIndex + 1)
#data_table[index_today+2] = buffer.decode('utf-8')

print "Unfinished and emerging today?"
buffer = dailytable.getTableEntry(index_today, planIndex + 2)
#data_table[index_today+3] = buffer.decode('utf-8')

print "please specify the plan tomorrow"
buffer = ""
buffer = dailytable.getTableEntry(index_tomorrow, planIndex)
#data_table[index_today+6] = buffer.decode('utf-8')


dailyreview.write_file(dailytable.table_head, dailytable.table)

print("writing to the summary...")



#breakpoint()



