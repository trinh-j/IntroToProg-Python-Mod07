#----------------------------------------------------------------
# Title: Assignment07.py
# Dev : Jessica Trinh
# Description: Creating a .py script to demonstrate how to pickle,
#              and use error/exception-handling. Script requires user to make a list of
#              basketball players and their numbers.
# Change log (who, when what):
#   JTrinh, 5/28/20, created script
#   JTrinh, 5/28/20, added pickling/binary file section
#   JTrinh, 5/30/20, created class for read and write functions-tested with code in Main Body
#   JTrinh, 5/31/20, wrote exception handles and refined main body
#   JTrinh, 6/01/20, added comments
#----------------------------------------------------------------
import pickle # imports module that allows for processing of objects to binary code
import sys #import module for exception handling

#-----Data-------------------------------------------------------
strFileName = 'TextFile.dat' #binary file (.dat)
lstTable = []

#-----Processing-------------------------------------------------
class FileAccess():
    '''
    Desc: Contains functions for writing and reading binary data from a text file
    '''

    @staticmethod
    def write_data_to_file(file_name, list_of_data):
        '''
        Desc: Saves data to file
        :param file_name:
        :param list_of_data:
        :return:
        '''
        with open(file_name, "wb") as binfile: #file-object handle "saved" as binfile (name of binary file); edit mode "write bytes"
            pickle.dump(list_of_data, binfile) #dumping list of user inputs into "binfile"
            binfile.close()

    @staticmethod
    def read_data_from_file(file_name):
        '''
        Desc: Reads data from binary file
        :param file_name
        :return:
        '''
        with open(file_name, "rb") as binfile: # edit mode "read bytes"; file-object handle saved to binfile
            list_of_data = pickle.load(binfile) #unpickles data in binary file
            binfile.close()
            return list_of_data
#-----Presentation-----------------------------------------------

def user_input():
    intID = int(input("Player Number: ")) #asks user for input; converts to integer
    strName = input("Player Name: ").upper() #converts user input to uppercase
    lstTable = [intID, strName] #puts inputs into a list
    return(lstTable)

#-----Exception Handling ----------------------------------------
try:
    fileData = FileAccess.read_data_from_file(strFileName) #looks for binary file with strFileName(TextFile.dat)
except FileNotFoundError as e: #if name of file not found, print error message below)
    print('File not found. Please check the name of your file, or create a new file.')
    fileData = lstTable
except pickle.UnpicklingError as e: #problem unpickling data
    print('Your file is corrupt. Your data cannot be unpickled.')
    sys.exit(1)

try:
    fileData.append(user_input()) #adds user inputs to list
    FileAccess.write_data_to_file(strFileName, fileData) #writes user inputs to binary file
except ValueError as e: #general error
    print(e)

#-----Main Body--------------------------------------------------

counter = 0
print("Current List: ")
print('Player Number | Player Name ')
while counter < len(FileAccess.read_data_from_file(strFileName)): #lists all items in list
    print((FileAccess.read_data_from_file(strFileName))[counter])
    counter += 1
