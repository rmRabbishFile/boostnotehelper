import os
import datetime
import cson
from helper import checkIndex
from helper import csonToTable
from helper import printPlan
from helper import getTableEntry



week_day = datetime.datetime.today().weekday()

# Read plan from the table

#with open("../notes/c39b9947-b545-4a13-b05f-7b43e54568f8.cson",'r+') as weekfile:
#with open("test.cson",'r') as weekfile:
with open("../notes/c39b9947-b545-4a13-b05f-7b43e54568f8.cson",'r') as weekfile:
    file_data = cson.load(weekfile)
    weekfile.seek(0) # ??? why set 0 used else where?
    write_data = weekfile.read()

data_table = csonToTable(file_data)


with open("../notes/dcdec832-2203-44ec-b8b4-28ef78b1c207.cson",'r') as weekfile:
    week_data = cson.load(weekfile)
#print(type(write_data))
#print(write_data[204:])

week_table =  csonToTable(week_data)

print "This is weekly plan"
printPlan(week_table, 6)

print "Today plan is"
data_raw = file_data[unicode("content", "utf-8")]
index_today = 6 + 5 * week_day
printPlan(data_table, index_today+1)


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
seperator = u'|' 
# XXX: hard-coded data head -> do keyword searching instead
data_output =  data_raw[0:323] + seperator.join(data_table) 
output_data = write_data[0:204] + data_output.encode('ascii','ignore') + "\n'''\nlinesHighlighted: []\nisStarred: false\nisTrashed: false"
output_data = output_data.decode('utf-8')
with open("../notes/c39b9947-b545-4a13-b05f-7b43e54568f8.cson",'w') as weekfile:
#with open("test.cson",'w') as weekfile:
    weekfile.write(output_data)



#print(file_data[u"content"])
print(output_data)

#print([list((i, data_table[i])) for i in range(0,len(data_table))])



#For weekly

#with open("../notes/dcdec832-2203-44ec-b8b4-28ef78b1c207.cson",'r+') as weekfile:
#    file_data = cson.load(weekfile)
#print(data_table[311:1000])