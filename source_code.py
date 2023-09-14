#Creation by Ethan Denyer,                 
#SOURCECODE:
# V.1.03 

#Requirement file allows you to import package into venv without having to pip install everything manually (and slowly!)

import time
from time import sleep


print("[SYSTEM] Please answer all questions directly, unless indicated otherwise by: (Y/N) ")
# time.sleep(5)

TITLE = input(str("[1] What would you like the Heading of your markdown file to be called?   "))
TITLE_SIZE = input(str("[2] What size would you like your Heading to be? (1 - 6 / Large - small)   "))    # STRING INPUT  |  #Title Size is determined by hashtags before the title 
    #Add in a requirement that TITLE_SIZE must be numerical or else we will display an error message and make them repeat the question. 

#TITLESIZE EDITS:   #useelif
if TITLE_SIZE == "1":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "# "+TITLE)
elif TITLE_SIZE == "2":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "## "+TITLE)
elif TITLE_SIZE == "3":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "### "+TITLE)
elif TITLE_SIZE == "4":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "#### "+TITLE)
elif TITLE_SIZE == "5":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "##### "+TITLE)
elif TITLE_SIZE == "6":
    TITLE_SIZE_VARIABLE = TITLE.replace(TITLE, "###### "+TITLE)

DESCRIPTION = input(str("[3] Please give a brief description on the contents of your file:   "))
DESCRIPTION_EDITS = input(str("[4] Is there any part of your description [3] that you would like to edit? E.g make a word bold (Y/N)   "))

#END OF TITLESIZE EDITS


#DESCRIPTION EDITS: #Similar to title size variable we are creating our variable for edit changes (NEW_DESC_EDIT)
if DESCRIPTION_EDITS == "Y":
    DESCRIPTION_EDITS_CHANGES = input("[4.1] What word would you like to edit?   ")
    DESCRIPTION_EDITS_CHANGES_SPECIFIC = input("[4.2] How would you like to edit that word from these choices: (Bold/Hyperlink/Underlined/Italics)   ")
    if DESCRIPTION_EDITS_CHANGES_SPECIFIC == "Bold":   #Markdown uses asterixes for bold
        NEW_DESC_EDIT = DESCRIPTION_EDITS_CHANGES.replace(DESCRIPTION_EDITS_CHANGES,"**"+DESCRIPTION_EDITS_CHANGES+"**" )
        # print(NEW_BOLD)
    if DESCRIPTION_EDITS_CHANGES_SPECIFIC == "Hyperlink":  # Markdown uses [hyperlinkname](hyperlinkurl)
        INPUT_HYPERLINK = input("[4.3] Can you please paste the hyperlink URL that you would like to use:   ")
        NEW_HYPERLINK = DESCRIPTION_EDITS_CHANGES.replace(DESCRIPTION_EDITS_CHANGES,"["+DESCRIPTION_EDITS_CHANGES+"]")  #Edit original word to add hyperlink brackets
        # print(NEW_HYPERLINK)
        NEW_DESC_EDIT = NEW_HYPERLINK.replace(NEW_HYPERLINK,NEW_HYPERLINK+"("+INPUT_HYPERLINK+")")  #Edit original word to add hyperlink brackets
        # print(NEW_HYPERLINK_URL)
    if DESCRIPTION_EDITS_CHANGES_SPECIFIC == "Underlined":    #Markdown uses <ins> to format to Underlined
       NEW_DESC_EDIT = DESCRIPTION_EDITS_CHANGES.replace(DESCRIPTION_EDITS_CHANGES,"<ins>"+DESCRIPTION_EDITS_CHANGES+"<ins>")
    #    print(NEW_UNDERLINED) 
    if DESCRIPTION_EDITS_CHANGES_SPECIFIC == "Italics":    #Markdown uses <ins> to format to Italics
        NEW_DESC_EDIT = DESCRIPTION_EDITS_CHANGES.replace(DESCRIPTION_EDITS_CHANGES, "*"+DESCRIPTION_EDITS_CHANGES+"*")
        # print(NEW_ITALICS)
else:
    NEW_DESC_EDIT = DESCRIPTION #If user input = "N"/"other input" there will be no amendemnts to current Description and simply print,
    print("[SYSTEM] No additional edits will be added to the current description    ")

#END OF DESCRIPTION EDITS

# ADDITIONAL HEADERS: This system is designed to create additional headers known as "subheaders / smaller titles"
SUB_HEADERS = input(str("[5] How many subheaders are required within the document? (Maximum of ten)   ")) #String input

if SUB_HEADERS == "0":
   sleep(0.5)
   print("[SYSTEM] No subheadings will be added.   ")
if SUB_HEADERS == "1":
    N1_SUB_HEADERS = input("[6] Please list the subheading that is required.   ")
if SUB_HEADERS > "1":
    N123_SUB_HEADERS = input("[6] Please list all the different subheaders that are required they need to be seperated by a space.   ") # Because we have more than one subheader we now need to seperate them each by a space to allow for our split function 
    NEW_HEADER_list = N123_SUB_HEADERS.split() #Example HEADER list = ["Functions Progression Specifications Resources Limits Computing"]
    List_Value = len(NEW_HEADER_list)    #We want to assign the value of the elements in our list to the variable List_Value, this will then be used in our function 

if SUB_HEADERS < "0": 
    print("[SYSTEM] Invalid Input. ")

#WE HAVE THE VALUE OF LIST_VALLUE WHICH IS THE ELEMENTS IN OUR LIST 
# NOW WE WANT TO ASSIGN EVERY ELEMENT IN THE LIST VALUE TO A HEADING VARIABLE- 
#  VALUE SO THAT WE CAN ADD THE VALUES 

#Input value is going to be STORED IN N123_SUB_HEADERS IN STRING FORMAT
for VAL in N123_SUB_HEADERS:
    

#INDEX VALUES FOR HEADERS
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
print(NEW_DESC_EDIT)   #Assumed edits but not necessarily if we return original desc value
# END OUTPUTTED RESULT:

