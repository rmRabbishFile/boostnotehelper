# This class contains functions regarding basic table 
# manipulation in markdown format

# This class only took the raw markdown notes content 
# as input and change the table within

class tablemd:
    def __init__(self, mdcontent):
        self.data_raw = mdcontent
        key1 = "--|\n"
        key2 = "--:|\n"
        if mdcontent.find(key1) != -1:
            self.table_head = mdcontent.find(key1) + \
                len(key1)
        elif mdcontent.find(key2) != -1:
            self.table_head = mdcontent.find(key2) + \
                len(key2)
        else:
            print("Load table fails: no table in the file")
        # TODO: Call tableReformat for uniform table on mdcontent[self.table_head:]
        #       from tablestart to tableend
        tablecontent = mdcontent[self.table_head:]
        self.table = tablecontent[1:].split(u'|')
        self.colcnt = self.table.index('\n')
        self.first =  self.colcnt + 1
        self.table_end = "Search for the table end later"
        ## TODO: Create a dictionary for title
        ##       Get the # of rows of the table
        
    def firstNrow(self, n):
        return n * self.first
    
    def tableReformat(self, strTable):
        start_anker = "search for ||\n"
        end_anker = "search for \n||"
        end = strTable.replace('\n','|\n')
        end = end.replace('||\n','|\n')
        end = end.replace('|\n','|\n|')
        end = end.replace('\n||','\n|')
        return end
# testing with tableReformat("|\n 123 |\n|123|\n 123 \n")
# index is the column of the selected row
    def getTableEntry(self,row, col):
        index = col + self.firstNrow(row)
        escape = True
        buffer = ""
        while(escape):
            temp = raw_input("only one at a time: (exit with e)")
            if temp.strip() == "e":
                break
            buffer = buffer + temp + "<br>"
        self.table[index] = buffer.decode('utf-8')
        return buffer

    def printElement(self, row, col):
        indx = self.firstNrow(row) + col 
        data_plan = self.table[indx].split(u'<br>')

        for i in range(len(data_plan)):
            print(i,data_plan[i]) 

    def table2output(self, head):
        data_output =  data_raw[0:self.table] + seperator.join(data_table)
        newmdcontent = data_output.encode('ascii','ignore')
        return newmdcontent


def tableElement():
    buffer = ""
    while(escape):
        temp = raw_input("only one at a time:")
        if temp == "e":
            escape = False 
        buffer = buffer + temp + "<br>"
    return buffer




