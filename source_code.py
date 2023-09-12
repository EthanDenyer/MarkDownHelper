#Creation by Ethan Denyer,                 
#SOURCECODE:
# 1.02

import time



print("Please answer all questions directly, unless indicated otherwise by: (Y/N) ")
# time.sleep(5)

TITLE = input(str("[1] What would you like the Heading of your markdown file to be called?   "))
TITLE_SIZE = input(str("[2] What size (level 1-6) would you like your Heading to be?   "))    # STRING INPUT  

#TITLESIZE EDITS:
if TITLE_SIZE == "1":
    TITLE_SIZE_1 = TITLE.replace(TITLE, "# "+TITLE)
    print(TITLE_SIZE_1)
if TITLE_SIZE == "2":
    TITLE_SIZE_2 = TITLE.replace(TITLE, "## "+TITLE)
    print(TITLE_SIZE_2)
if TITLE_SIZE == "3":
    TITLE_SIZE_3 = TITLE.replace(TITLE, "### "+TITLE)
    print(TITLE_SIZE_3)
if TITLE_SIZE == "4":
    TITLE_SIZE_4 = TITLE.replace(TITLE, "#### "+TITLE)
    print(TITLE_SIZE_4)
if TITLE_SIZE == "5":
    TITLE_SIZE_5 = TITLE.replace(TITLE, "##### "+TITLE)
    print(TITLE_SIZE_5)
if TITLE_SIZE == "6":
    TITLE_SIZE_6 = TITLE.replace(TITLE, "###### "+TITLE)
    print(TITLE_SIZE_6)
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
    SUB_HEADERS = input(str("[5] How many subheaders are required within the document?")) # STRING INPUT 

#END OF DESCRIPTION EDITS

#ADDITIONAL HEADERS:
# if SUB_HEADERS == 
#END OF DESCRIPTION EDITS



