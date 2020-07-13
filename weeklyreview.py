## Extract current weekly review and plan for the next week

## output: Extract and print weekly review
            # Extract and print monthly review
            # make the review for next week

import fetcher
import tablemd


class WeeklyReview:
    def __init__(self, weekfile, weeknumber):
        self.weekreview = fetcher.Fetcher(weekfile, end_ind="tag")
        self.weekreview.read_file()
        self.weektable = tablemd.tablemd(self.weekreview.content_data)
        weektitle = [self.weektable.readcell(0,2*i+1).encode('ascii','ignore') 
                                for i in range(3)]
        weeknumbers = [int(filter(str.isdigit,strt)) 
                                for strt in weektitle]
        self.week_index = 1 + weeknumbers.index(weeknumber) * 2
        #print self.weektable.table

    def printReview(self):
        for i in range(2, self.weektable.nrow+1): ## Print 
            # the entire table
            self.weektable.printElement( i, 0)
            self.weektable.printElement( i, self.week_index)

    def reviewByCat(self):
        for i in range(2, self.weektable.nrow+1): ## Print 
            # the entire table
            self.weektable.printElement( i, 0)
            self.weektable.printElement( i, self.week_index)
            self.weektable.getTableEntry(i, self.week_index + 1)
        self.weekreview.write_file(self.weektable.table_head, self.weektable.table)
    def planByCat(self):
        print("Please plan for next week:")
        for i in range(2, self.weektable.nrow+1): ## Print 
            # the entire table
            self.weektable.printElement( i, 0)
            self.weektable.printElement( i, self.week_index)
            self.weektable.getTableEntry(i, self.week_index + 2)
        self.weekreview.write_file(self.weektable.table_head, self.weektable.table)
