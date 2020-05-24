# Daily review use fetcher class get the cson data
#              use Tabletailor get the table data with parsor '|' and '<br>'

import os
import datetime
import pdb

import fetcher
import tablemd


weekfile = "../notes/dcdec832-2203-44ec-b8b4-28ef78b1c207.cson"
dailyfile = "../notes/c39b9947-b545-4a13-b05f-7b43e54568f8.cson"

## Read in the content
dailyreview =  fetcher.Fetcher(dailyfile)
#testing and prototyping
dailyreview.read_file()
weekreview = fetcher.Fetcher(weekfile)
weekreview.read_file()
## Read in tables
dailytable = tablemd.tablemd(dailyreview.content_data)
weektable = tablemd.tablemd(weekreview.content_data)


print "This is weekly plan"

for i in range(1, 4):
    weektable.printElement(weektable.firstNrow(i) + 0)
    weektable.printElement(weektable.firstNrow(i) + 1)

print "Today plan is"
# First day is sunday
week_day = (datetime.datetime.today().weekday() + 1 ) % 7 


planIndex = 1
index_today = planIndex + dailytable.firstNrow(week_day%6)

dailytable.printElement(index_today)

writefile = "test.cson"
print "please specify what is done"
buffer = dailytable.getTableEntry(index_today+1)
#data_table[index_today+2] = buffer.decode('utf-8')

print "Unfinished and emerging today?"
buffer = dailytable.getTableEntry(index_today+2)
#data_table[index_today+3] = buffer.decode('utf-8')

print "please specify the plan tomorrow"
buffer = ""
buffer = dailytable.getTableEntry(index_today+5)
#data_table[index_today+6] = buffer.decode('utf-8')


dailyreview.write_file(dailytable.table_head, dailytable.table)

print("writing to the summary...")



#breakpoint()



