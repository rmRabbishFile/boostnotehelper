## Test scripts for weeklyreview
import weeklyreview
import datetime
 
passed = 1
weekfile = "/home/c7031195/Dropbox/Boostnote//notes/dcdec832-2203-44ec-b8b4-28ef78b1c207.cson"
## Initialization
weekfile = "test_weekly.cson"

weeknumber = datetime.date.today().isocalendar()[1]
print("This is week ", weeknumber)
if passed == 1:
    weekdata = weeklyreview.WeeklyReview(weekfile,weeknumber)
    passed = 3

## Print weekly 
if passed == 3:
#    weekdata.printReview()
    passed = 4

## Display sections one by one
if passed == 4:
    weekdata.reviewByCat()
    passed = 5
## Add content to Done

if passed == 5:
    weekdata.planByCat()
    
## Copy content of daily review to old review database
if passed == 6:
    pass

##