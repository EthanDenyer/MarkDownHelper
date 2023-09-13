#Creation by Ethan Denyer,                 
#SOURCECODE:
# 1.02

import time
from time import sleep


print("Please answer all questions directly, unless indicated otherwise by: (Y/N) ")
# time.sleep(5)

TITLE = input(str("[1] What would you like the Heading of your markdown file to be called?   "))
TITLE_SIZE = input(str("[2] What size (level 1-6) would you like your Heading to be?   "))    # STRING INPUT  |  #Title Size is determined by hashtags before the title 
    #Add in a requirement that TITLE_SIZE must be numerical or else we will display an error message and make them repeat the question. 

#TITLESIZE EDITS:
if TITLE_SIZE == "1":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "# "+TITLE)
if TITLE_SIZE == "2":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "## "+TITLE)
if TITLE_SIZE == "3":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "### "+TITLE)
if TITLE_SIZE == "4":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "#### "+TITLE)
if TITLE_SIZE == "5":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "##### "+TITLE)
if TITLE_SIZE == "6":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "###### "+TITLE)

DESCRIPTION = input(str("[3] Please give a brief description on the contents of your file:   "))
DESCRIPTION_EDITS = input(str("[4] Is there any part of your description [3] that you would like to edit? E.g make a word bold (Y/N)   "))

#END OF TITLESIZE EDITS


#DESCRIPTION EDITS:
if DESCRIPTION_EDITS == "Y":
    DESCRIPTION_EDITS_CHANGES = input("[4.1] What word would you like to edit?   ")
    DESCRIPTION_EDITS_CHANGES_SPECIFIC = input("[4.2] How would you like to edit that word from these choices: (Bold/Hyperlink/Underlined/Italics)   ")
    if DESCRIPTION_EDITS_CHANGES_SPECIFIC == "Bold":   #Markdown uses asterixes for bold
        NEW_BOLD = DESCRIPTION_EDITS_CHANGES.replace(DESCRIPTION_EDITS_CHANGES,"**"+DESCRIPTION_EDITS_CHANGES+"**" )
        # print(NEW_BOLD)
    if DESCRIPTION_EDITS_CHANGES_SPECIFIC == "Hyperlink":  # Markdown uses [hyperlinkname](hyperlinkurl)
        INPUT_HYPERLINK = input("[4.3] Can you please paste the hyperlink URL that you would like to use:   ")
        NEW_HYPERLINK = DESCRIPTION_EDITS_CHANGES.replace(DESCRIPTION_EDITS_CHANGES,"["+DESCRIPTION_EDITS_CHANGES+"]")  #Edit original word to add hyperlink brackets
        # print(NEW_HYPERLINK)
        NEW_HYPERLINK_URL = NEW_HYPERLINK.replace(NEW_HYPERLINK,NEW_HYPERLINK+"("+INPUT_HYPERLINK+")")  #Edit original word to add hyperlink brackets
        # print(NEW_HYPERLINK_URL)
    if DESCRIPTION_EDITS_CHANGES_SPECIFIC == "Underlined":    #Markdown uses <ins> to format to Underlined
       NEW_UNDERLINED = DESCRIPTION_EDITS_CHANGES.replace(DESCRIPTION_EDITS_CHANGES,"<ins>"+DESCRIPTION_EDITS_CHANGES+"<ins>")
    #    print(NEW_UNDERLINED) 
    if DESCRIPTION_EDITS_CHANGES_SPECIFIC == "Italics":    #Markdown uses <ins> to format to Italics
        NEW_ITALICS = DESCRIPTION_EDITS_CHANGES.replace(DESCRIPTION_EDITS_CHANGES, "*"+DESCRIPTION_EDITS_CHANGES+"*")
        # print(NEW_ITALICS)
else:
    SUB_HEADERS = input(str("[5] How many subheaders are required within the document? (Maximum of ten)   ")) # STRING INPUT 

#END OF DESCRIPTION EDITS

# ADDITIONAL HEADERS:

if SUB_HEADERS == "0":
   sleep(0.5)
   print("Is this working")
if SUB_HEADERS == "1":
    N1_SUB_HEADERS = input("[6] Please list all the different subheaders that are required. Seperated by a space.   ")
if SUB_HEADERS > "1":
    N123_SUB_HEADERS = input("[6] Please list all the different subheaders that are required. Seperated by a space.   ") # Because we have more than one subheader we now need to seperate them each by 
    NEW_HEADER_list = N123_SUB_HEADERS.split() #Example HEADER list = ["Functions Progression Specifications Resources Limits Computing"]
    List_Value = len(NEW_HEADER_list)    #We want to assign the value of the elements in our list, this will then be used in our function 

if SUB_HEADERS < "0":
    print("Invalid Input")


HEAD_0 = NEW_HEADER_list[0]
HEAD_1 = NEW_HEADER_list[1]
HEAD_2 = NEW_HEADER_list[2]
HEAD_3 = NEW_HEADER_list[3]
HEAD_4 = NEW_HEADER_list[4]
HEAD_5 = NEW_HEADER_list[5]
HEAD_6 = NEW_HEADER_list[6]
HEAD_7 = NEW_HEADER_list[7]
HEAD_8 = NEW_HEADER_list[8]
HEAD_9 = NEW_HEADER_list[9]
 #NOTE TO MYSELF I WILL NEED TO CHANGE THE SUB HEADER LATER 
#END OF ADDITIONAL HEADERS

# OUTPUTTED RESULT:
print("------------------------------------")
print("---------GENERATED .MD CODE---------")
print(TITLE_SIZE_VARIABLE)
# END OUTPUTTED RESULT:

