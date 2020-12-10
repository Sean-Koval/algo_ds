###
# The idea is to count the number of words in a file
# We first check the instance the file can't be opened
# This creates a dict() that will be used to store count
# Then we iterate through and use split to break up lines into words
# Iterate through the words and check if in the dict (count)
# If not then we add key: and increase the val by 1
# If it is in the dict then we increase the count by 1
###


def word__Count(fname):
     try:
          fhand=open(fname, 'r')
     except:
          print('File can not be opened')
          exit()

     count = dict()
     for line in fhand:
          words = line.split()
          for words in words:
               if word not in count:
                    count[word] = 1
               else:
                    count[word] += 1
     return(count)



count=wordcount('alice.txt') 


filtered={key:value for key, value in count.items() if value <20 and value>18 }

print(filtered)