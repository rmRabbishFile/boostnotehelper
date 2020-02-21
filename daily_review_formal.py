# Daily review use fetcher class get the cson data
#              use Tabletailor get the table data with parsor '|' and '<br>'

import os
import datetime
import pdb

import fetcher
import tablemd


weekfile = "../notes/dcdec832-2203-44ec-b8b4-28ef78b1c207.cson"
#dailyfile = "../notes/c39b9947-b545-4a13-b05f-7b43e54568f8.cson"

## Read in the content
dailyreview =  fetcher.Fetcher()
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
week_day = datetime.datetime.today().weekday()
pdb.set_trace()
planIndex = 1
index_today = planIndex + dailytable.firstNrow(week_day + 1)
dailytable.printElement(index_today)


writefile = "test.cson"
print "please specify what is done"
buffer = getTableEntry()
data_table[index_today+2] = buffer.decode('utf-8')

print "Unfinished and emerging today?"
buffer = getTableEntry()
data_table[index_today+3] = buffer.decode('utf-8')

print "please specify the plan tomorrow"
buffer = ""
buffer = getTableEntry()
data_table[index_today+6] = buffer.decode('utf-8')

print("writing to the summary...")



check = ff.write_file(" ")

breakpoint()

#print fetchweek.read_file()


