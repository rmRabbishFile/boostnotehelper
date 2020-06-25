## Extract current weekly review and plan for the next week

## output: Extract and print weekly review
            # Extract and print monthly review
            # make the review for next week

import fetcher
import tablemd

class WeeklyReview:
    def __init__(self, weekfile):
        self.weekreview = fetcher.Fetcher(weekfile)
        self.weekreview.read_file()
        self.weektable = tablemd.tablemd(self.weekreview.content_data)

    def printReview(self):
        for i in range(1, 4): ## Print all the entire table
            self.weektable.printElement( i, 0)
            self.weektable.printElement( i, 1)
