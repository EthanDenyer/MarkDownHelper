
# TITLE = input(str("[1] What would you like the Heading of your markdown file to be called?   "))
# TITLE_SIZE = input(str("[2] What size (level 1-6) would you like your Heading to be?   "))    # STRING INPUT  |  #Title Size is determined by hashtags before the title 
#     #Add in a requirement that TITLE_SIZE must be numerical or else we will display an error message and make them repeat the question. 

# #TITLESIZE EDITS:
# if TITLE_SIZE == "1":
#     TITLE_SIZE_1 = TITLE.replace(TITLE, "# "+TITLE)
# if TITLE_SIZE == "2":
#     TITLE_SIZE_2 = TITLE.replace(TITLE, "## "+TITLE)
# if TITLE_SIZE == "3":
#     TITLE_SIZE_3 = TITLE.replace(TITLE, "### "+TITLE)
# if TITLE_SIZE == "4":
#     TITLE_SIZE_4 = TITLE.replace(TITLE, "#### "+TITLE)
# if TITLE_SIZE == "5":
#     TITLE_SIZE_5 = TITLE.replace(TITLE, "##### "+TITLE)
# if TITLE_SIZE == "6":
#     TITLE_SIZE_6 = TITLE.replace(TITLE, "###### "+TITLE)

# if TITLE_SIZE_1 > "0":
#     TT_FORWARD = TITLE_SIZE_1
# if TITLE_SIZE_2 > "0":
#     TT_FORWARD = TITLE_SIZE_2
# if TITLE_SIZE_3 > "0":
#     TT_FORWARD = TITLE_SIZE_3
# if TITLE_SIZE_4 > "0":
#     TT_FORWARD = TITLE_SIZE_4
# if TITLE_SIZE_5 > "0":
#     TT_FORWARD = TITLE_SIZE_5
# if TITLE_SIZE_6 > "0":
#     TT_FORWARD = TITLE_SIZE_6
# print(TT_FORWARD)

# input_ 
# def 
#I want to pass the title size to the function and have that function assign it to an overall variable which print's one of them .

# new_input = input("Give me a number")

# def user_input(input):
#     if input == "0":
#         print("hello")
#     else:
#         print("goodbye")

# user_input(new_input)     
SUB_HEADERS = input("[5] How many subheaders are required within the document? (Maximum of ten)   ") #String input
SUB_HEADER_INT = int(SUB_HEADERS)
N123_SUB_HEADERS = input("[6] Please list all the different subheaders that are required. Seperated by a space.   ") # Because we have more than one subheader we now need to seperate them each by 
NEW_HEADER_list = N123_SUB_HEADERS.split() #We take the input and we give each individual word a set of brackets
List_Value = len(NEW_HEADER_list) #Number of strings in the list (INTEGER)



print(NEW_HEADER_list) # IF WE PAY ATTENTION WE SEE THAT THE [ ] DESIGNATED THAT THIS IS ALREADY IN ARRAY FORM. 
print(SUB_HEADERS)
print(type(SUB_HEADERS))
#13/9/23: FUNC ATTEMPT 1 - I WANT TO CREATE A WORKING INPUT WHICH ALLOWS US TO ASSIGN A VARIABLE NAME ITERATION ON NUMBER OF CHANGES

def array_var():
    for x in range(SUB_HEADER_INT):     # We are now cycling through the number of values 
        

array_var()

# def assignindex(input):
#     input = List_Value #This has appended six values 
#     print(List_Value)  
#     for i in range(List_Value)      #This will now print the amount of values in the range
#     #I need a function that allows us to create the number of variables which are in List_Value

# #int isn't iterable, so we need a way

# print
# assignindex(N123_SUB_HEADERS)
# HEAD_0 = NEW_HEADER_list[0]
# HEAD_1 = NEW_HEADER_list[1]
# HEAD_2 = NEW_HEADER_list[2]
# HEAD_3 = NEW_HEADER_list[3]
# HEAD_4 = NEW_HEADER_list[4]
# HEAD_5 = NEW_HEADER_list[5]
# HEAD_6 = NEW_HEADER_list[6]
# HEAD_7 = NEW_HEADER_list[7]
# HEAD_8 = NEW_HEADER_list[8]
# HEAD_9 = NEW_HEADER_list[9]




# dog = 5

# print(type(dog))

