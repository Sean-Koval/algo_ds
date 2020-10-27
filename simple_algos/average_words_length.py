### THIS IS HOW YOU MANIPULATE A STRING USING .SPLIT() and .REPLACE() ###
### SPLIT IS USED TYO CUT STRINGS SO THEY CAN BE CALCULATED (USE SPACE - CUT WITH SPLIT - COUNT ###

sentence1 = "This is the first test sentence.  I think you look like a busy guy."
sentence2 = "This is an example of another sentence I hop.....I dont screw up"



def count_avg_length_word(sentence):

    for i in "!?,';.":
        sentence = sentence.replace(i, ' ')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words), 2) # this caluclates the average length of the strings in the list words (, 2) 
                                                                 # dictates how many digits


m = count_avg_length_word(sentence1)
print(m)