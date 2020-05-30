# ------------------------------------------------- #
# Title: Assignment 07
# Description: A simple example of storing data in a binary file with handling errors
# ChangeLog: (Who, When, What)
# Kate Golenkova, 05/28/2020, Created Script
# Kate Golenkova, 05/30/2020, Modified Script
# ------------------------------------------------- #

import pickle

# Data -------------------------------------------- #
strFileName = 'C:\_PythonClass\Assignment07\AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
# Function to save data
def save_data_to_file(file_name, list_of_data):
        # pass  # TODO: Add code here
        # open file, convert data to binary, save data and close the file
        file = open(file_name, "wb")
        # Save data to binary file
        pickle.dump(list_of_data, file)
        file.close()
        return list_of_data
# Function to read data from file
def read_data_from_file(file_name):
        # pass  # TODO: Add code here
        data = []
        file = open(file_name, "rb")
        # Using try-except to catch EOFError if our file is empty
        try:
            # Get data from binary file
            data = pickle.load(file)
        except EOFError as e:
            print("There is no data in this file yet. Please use Option 2 to add some data.")
        file.close()
        return data

# Presentation ------------------------------------ #
# Function to get user input new data
def get_user_input():
    # Using while loop and try-except block to get ValueError if ID is not a digit
    while True:
        user_id = input("Please enter your ID: ")
        try:
            user_id = int(user_id)
            break
        except ValueError as e:
            print("Error. Please use numbers only for ID.")
    user_name = input("Please enter your Name: ")
    # Store new data in a list
    list_of_data = [user_id, user_name]
    return list_of_data

# TODO: Get ID and NAME From user, then store it in a list object
# TODO: store the list object into a binary file
# TODO: Read the data from the file into a new list object and display the contents

# Main Script ------------------------------------- #
print("Welcome to Assignment 07.")
print("Please use this program to add you ID and Name into file.")
# While loop to display Menu with options
while(True):
    # Menu options
    print('''
        Choose an Option:
            1. Show Current Data in a File
            2. Add New Data
            3. Save New Data to a File
            4. Exit
            
    ''')
    choice = input("Please enter an Option: ")
    # Read and display data from File
    if choice == '1':
        print("Current Data in a File is: ")
        print(read_data_from_file(strFileName))
    # Add new data
    elif choice == '2':
        lstCustomer = get_user_input()
        print("You entered: " + str(lstCustomer))
    # Save data to a file
    elif choice == '3':
        print("Your Data has been saved.")
        save_data_to_file(strFileName, lstCustomer)
    # Exit the program
    elif choice == '4':
        break
    else:
        print("Please enter Option 1, 2 or 3: ")


