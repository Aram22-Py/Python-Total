"""
Created on Mon Mar  2 13:17:15 2026

@author: aram22
"""
#This project will allow us to analyse 1 text that the user will input.
#The user will give us 3 letters and we will check the following

#Our goal is to apply all the previous knowledge to answer and to do this:
# - How many times does each letter appear?
#- How many words are in the entire text?
#- What are the first and last words in the text?
# - If the word 'Python' appears in the text
#- Words in reverse order


#so first we will ask the user to input a text; a phrase, a paragraph or an entire article can work
print("""Hello, user!
      Please input a text so it can be analysed """)
text_1=input("Enter the text here: ")
#We show the user the text he input
print("This is the text you just input: \n" + text_1)

#now we are asking additional information, 3 words to begin the analysis
print("Now please provide 3 different letters so we can start the analysis: ")
letter1=input("Input letter 1:")
letter2=input("Input letter 2:")
letter3=input("Input letter 3:")
print("The letters you entered are: \n" +letter1 +"\n"+ letter2 +"\n" + letter3)

#so we will start with the first thing in the analsis:
    #- How many words are in the entire text?
    #we will split the text, save it as a list with each word as an element of it
    #we will storage it in a new variable
split_list1 = text_1.split() #we are leaving it with no argument in the method so it can take any
#blank space as a separator
#now we will count how many words it has
length_of_text1 = len(split_list1)


#now we will answer this : # - How many times does each letter appear?
#for the first letter
letter1_appearences = text_1.upper().count(letter1.upper())
letter2_appearences = text_1.upper().count(letter2.upper())
letter3_appearences = text_1.upper().count(letter3.upper())

    
    
#Final explaination of the analysis.
print("Using your text and the words given, this is the analysis we have for you:")
    #- How many words are in the entire text?
    #answering this question:
print(f"The text contains {length_of_text1} words.")
print(f"The first letter you provided ('{letter1}') appears {letter1_appearences} times.")
print(f"The second letter you provided ('{letter2}') appears {letter2_appearences} times.")
print(f"The third letter you provided ('{letter3}') appears {letter3_appearences} times.")

#now for the 3rd question #- What are the first and last words in the text?
print(f"The first letter used in the text is ('{text_1[0]}') and the last one is ('{text_1[-2]}')")
#Now, for the last one. Does the word 'Python' appears in the text, True or False
print ("Does the word Python appears in the text?: ")
print('Python' in text_1)


