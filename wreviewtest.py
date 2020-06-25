## Test scripts for weeklyreview
import weeklyreview

passed = 1
weekfile = "/home/c7031195/Dropbox/Boostnote//notes/dcdec832-2203-44ec-b8b4-28ef78b1c207.cson"
## Initialization

if passed == 1:
    weekdata = weeklyreview.WeeklyReview(weekfile)
    passed = 3

## Print weekly 
if passed == 3:
    weekdata.printReview()
## Display sections one by one
if passed == 4:
    pass
## Add content to Done

if passed == 5:
    pass
## Copy content to old review database


##