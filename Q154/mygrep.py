#importing sys library for accessing command line arguments
import sys

def main():
    #checking if there are three arguments or not
    #here first argument is name of python file itself
    if len(sys.argv) !=3:
        print("Arguments Format not Correct")
        return
    search_text = sys.argv[1]
    filename = sys.argv[2]
    
    #adding a try except block to catch file not found error
    try:
        #opening file in read only mode
        with open(filename,'r') as fl:
            
            #function to read all lines as a python list
            lines = fl.readlines()
            #looping through each line one by one
            for line in lines:
                #searching if search text exists in current line and printing
                if search_text in line:
                    print(line)
    except FileNotFoundError:
        print("File Does not exist")

#this line is used so that main is only called when it is directly executed and not imported
if __name__ == '__main__':
    main()