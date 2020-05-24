# findata is the data read by cson.load
# head_key is the first lable followed by meaning for data
# data_raw the data in the oringinal form
# data table the data in the tavle form convenient for processing
# Reader 
import cson
## Fetcher write and get string  for file and pass the table from cson format. 
## Parser put content into lists and pack back
## Changer Change the items from the request of UI
## Terminal UI

### TODO: Seperate the md writing file with cson.

class Fetcher:
  def __init__(self, file_name = "test.cson"):
    self.file_data = ""
    self.file_name = file_name
    #self.head_indr = head_key #Search can be used
    self.data_table = []

  def read_file(self):
    with open(self.file_name,'r') as weekfile:
        self.file_data = cson.load(weekfile)
        weekfile.seek(0) # ??? why set 0 used else where?
        self.write_data = weekfile.read()
        self.content_data = self.file_data[unicode("content", "utf-8")]
        return self.file_data
# Write content data to the cson files
# Input: 
#
  def write_file(self, startIdx, data_table):
    # head = self.write_data[0:204]
    self.keykey = "content: '''"
    self.endkey = "'''\nlinesHighlighted"
    self.head = self.write_data.find(self.keykey)+ len(self.keykey) + 1
    self.end = self.write_data.find(self.endkey)
    seperator = u'|' 
    data_output = self.content_data[0:startIdx] + '|' + seperator.join(data_table)
    self.output_data = self.write_data[0:self.head] + \
      data_output.encode('ascii','ignore') + '\n' + self.write_data[self.end:]
    #data_output.encode('ascii','ignore') + "\n'''\nlinesHighlighted: []\nisStarred: false\nisTrashed: false"
    self.output_data = self.output_data.decode('utf-8')
    try: 
      #with open("../notes/c39b9947-b545-4a13-b05f-7b43e54568f8.cson",'w') as weekfile:
      with open(self.file_name,'w') as weekfile:
        weekfile.write(self.output_data)
      return True
    except IOError as e:
      print("Couldn't open or write to file (%s)." % e)
      return False 
     

     
# and Writer