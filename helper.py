# TODO make a class that took all the file as the state

def checkIndex(data_table):
    print([list((i, data_table[i])) for i in range(0,len(data_table))])

def tableElement():
    buffer = ""
    while(escape):
        temp = raw_input("only one at a time:")
        if temp == "e":
            escape = False 
        buffer = buffer + temp + "<br>"
    return buffer

def csonToTable(file_data):
    data_raw = file_data[unicode("content", "utf-8")]
    # FIXME: data_raw is not a clean implementation
    data_table = data_raw[323:].split(u'|') 
    return data_table

def printPlan(data_table, indx):
    data_plan = data_table[indx].split(u'<br>')

    for i in range(len(data_plan)):
        print(i,data_plan[i])

def getTableEntry():
    escape = True
    buffer = ""
    while(escape):
        temp = raw_input("only one at a time:")
        if temp == "e":
            break
        buffer = buffer + temp + "<br>"
    return buffer