### THIS IS HOW YOU MANIPULATE A STRING USING .SPLIT() and .REPLACE()
# SPLIT IS USED TYO CUT STRINGS SO THEY CAN BE CALCULATED (USE SPACE - CUT WITH SPLIT - COUNT
# Start by removing special charecters (loop through and replace)
# Then break up the sentence into words
# Return the sum of the len() for each word (item) in the list words

sentence1 = "This is the first test sentence.  I think you look like a busy guy."
sentence2 = "This is an example of another sentence I hop.....I dont screw up"



def count_avg_length_word(sentence):

    # method for removing unwanted chars
    for i in "!?,';.":
        sentence = sentence.replace(i, ' ')
    # split the senteene into words
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words), 2) # this caluclates the average length of the strings in the list words (, 2) 
                                                                 # dictates how many digits


m = count_avg_length_word(sentence1)
print(m)