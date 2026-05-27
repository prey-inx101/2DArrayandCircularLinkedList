
#user input based sample program for 2d array and circular linked list 

array2D = []  #set as global for 2D array, to be accessed and modified in multiple fxns like insert, delete, and search

def menu(): #main menu

    while True: #loops until user input is valid
        print("\nMENU")
        print(" 1) 2D Array")
        print(" 2) Circular Linked List")
        print(" 0) Exit\n")

        user_choice = input("Enter choice: ").strip() #ask and store user input chocie

        if user_choice == "":
            print("Input cannot be empty. Please try again.") #error handling for incorrect user input.
            continue

        try:
            u_input = int(user_choice)
            if u_input == 0:
                print("Exiting ... ")
                break

            #2D ARRAY MENU
            if u_input == 1:
                print("\nYou chose 2D Array.")

                try:
                    rows = int(input("Enter number of rows: ")) #set the # of rows in 2D arrays
                    cols = int(input("Enter number of columns: ")) #set the # of columns per row
                    #rows and cols are stored in local var in menu()

                    for r in range(rows):
                        while True:
                            row = input(f"Enter {cols} numbers for Row {r+1}, separated by spaces: ").split()
                            
                            if len(row) != cols:
                                print(f"Error! You must enter exactly {cols} numbers.")
                                continue  #Ask again

                            try:
                                int_row = [int(x) for x in row]  #Convert input to integers
                                array2D.append(int_row)
                                break  #Exit the loop if input is valid
                            except ValueError:
                                print("Invalid input! Enter whole numbers only.") #error handling for incorrect user input.

                    print("\n2D array:")#prints 2d array
                    for row in array2D:
                        print(row)

                except ValueError:
                    print("Invalid Input. Enter whole numbers only. Please try again.") #error handling for incorrect user input.


                #2D ARRAY SUBMENU
                while True:#loops until user input is valid
                    print("\nOptions for 2D Array\n")
                    print(" 1) Insert")
                    print(" 2) Delete")
                    print(" 3) Search")
                    print(" 0) Back to Main Menu\n")

                    u_arr = input("Enter choice: ").strip()
                    if u_arr == "":
                        print("Input cannot be empty. Please try again.")
                        continue

                    try:
                        u_arr_input = int(u_arr)
                        if u_arr_input == 0:
                            break  #back to the main menu

                        elif u_arr_input == 1:
                            insert_2DArr(cols)  #calls fxn for insertion

                        elif u_arr_input == 2:
                            delete_value_2D_array() #calls fxn for deletion

                        elif u_arr_input == 3:
                            search_2d(array2D) #calls fxn for search
                            
                        else:
                            print("Invalid choice. Please enter 0, 1, 2, or 3.")

                    except ValueError:
                        print("Please enter 0, 1, 2, or 3. Try again.")



            #CIRCULAR LINKED LIST MENU
            elif u_input == 2:
 
                my_list = CircularLinkedList() #creates instance of class named  CircularLinkedlist to access, store, modidy data

                while True:
                    print("\nOptions:")
                    print("1. Insert a node")
                    print("2. Delete a node")
                    print("3. Search for a node")
                    print("0. Exit")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        data = input("Enter data to insert: ")
                        try:
                            data = int(data)  #convert input from string to integer
                        except ValueError:
                            pass  
                        my_list.insert(data) #calls the insert method of instance named my_list as intialized above, which is an instance of the class named CircularLinkedList()
                    elif choice == '2':
                        data = input("Enter data to delete: ")
                        try:
                            data = int(data)  
                        except ValueError:
                            pass  
                        my_list.delete(data)#calls the delete method of instance named my_list as intialized above, which is an instance of the class named CircularLinkedList()
                    elif choice == '3':
                        data = input("Enter data to search: ")
                        try:
                            target = int(data)  
                        except ValueError:
                            target = data  
                        if my_list.search(target):#calls the search method of instance named my_list as intialized above, which is an instance of the class named CircularLinkedList()
                            print("Node found.")
                        else:
                            print("Node not found.")
                    elif choice == '0':
                        print("Exiting...")
                        break
                    else:#this will handle the cases where  user is not 1,2,3,or 0, displaying msg to try again
                        print("Invalid choice. Please try again.")

        except ValueError:
            print ("Please try again. Enter Valid Option: 0, 1, or 2.")


#2D ARRAY INSERT FUNCTION
def insert_2DArr(cols):#parameter cols is passed into this fxn to ensure that the new rows to be inserted have the correct # of columns (as set earlier)
    print("\nYou have chosen to Insert Value in 2D Array.")

    print("\nCurrent 2D Array:") 
    for i, row in enumerate(array2D): #loops through each row of the 2D list (array2D).
        print(f"Row {i}: {row}") #prints the row number (i) and the actual row values (row) so user can choose where to insert

    #Get row index from user, where user want to insert the new row
    while True:#loop until  row index input is valid
        try:
            #this ask for user input at the same it converts the input from string to interger and store it to user_index
            user_index = int(input("\nEnter the (row index) where you want to insert the values: ")) 
            if 0 <= user_index <= len(array2D): #checks the user input if it is within a valid range in array2D
                break
            else:
                print(f"Invalid index. Please enter a number between 0 and {len(array2D)}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    #Get new row from user
    while True: #loop until new row data is valid
        new_row = input(f"Enter {cols} values separated by spaces: ").split() #this stores the input values that will be inserted to 2D Array.
        if len(new_row) == cols: #this is the condition for loop
            try:
                new_row = [int(x) for x in new_row]  #Convert input to integers
                break
            except ValueError:
                print("Invalid input! Enter whole numbers only.") #error handling for incorrect user input.
        else:
            print(f"Error! You must enter exactly {cols} numbers.") #error handling for incorrect user input.
    #Insert row at the specified index
    array2D.insert(user_index, new_row) #new row is inserted directly to into array2D
    print("\nUpdated 2D Array:")
    for row in array2D:
        print(row)


#2D ARRAY DELETE FUNCTION
def delete_value_2D_array():
    global array2D  #Declare global variable to modify the original list

    print("\nCurrent 2D Array:")
    for i, row in enumerate(array2D): #loops through each row of the 2D list (array2D).
        print(f"Row {i}: {row}") #prints the row number and the actual row values so user can choose where to insert

    if not array2D:
        print("The 2D array is empty.")
        return
    
    while True:
        print("\nOptions for Deleting Value(s) in 2D Array")
        print("1) Delete values by row")
        print("2) Delete values by column")
        print("0) Return to the main menu")

        user = input("Enter choice: ").strip()

        if not user:
            print("Input cannot be empty. Please try again.") #error handling for incorrect user input.
            continue

        try:
            u_input = int(user)
            
            if u_input == 0:
                return  #will routed back to the main menu

            elif u_input == 1:
                print("\nYou have chosen to delete values by row.")
                
                while True:
                    try:
                        print(f"Please enter a row index between 0 and {len(array2D) - 1}.") #this provides the user the range of row, it provides the max valud row index
                        user_index = int(input("Enter the row index to delete: "))

                        if 0 <= user_index < len(array2D): #check if user input (user_index) is within a valid range 
                            del array2D[user_index]  #Delete row in place
                            print("Updated 2D Array:\n", array2D)
                            break
                        else:
                            print(f"Invalid index. Please enter a number between 0 and {len(array2D) - 1}.") #error handling for incorrect user input.
                    except ValueError:
                        print("Invalid input. Please enter a whole number.") #error handling for incorrect user input.

            elif u_input == 2:
                print("\nYou have chosen to delete values by column.")

                while True:
                    try:
                        if not array2D or not array2D[0]:  #Check if the matrix is empty
                            print("The 2D array is empty. No columns to delete.")
                            return  

                        col_index = int(input("Enter the column index to delete: ")) #store the user input and convert to an integer (from string)

                        if 0 <= col_index < len(array2D[0]):  #this checks user input is within the range
                            for row in array2D:
                                del row[col_index]  # Delete column in place
                            print("Updated 2D Array:\n", array2D)
                            break  
                        else:
                            print(f"Invalid column index. Please enter a number between 0 and {len(array2D[0]) - 1}.") #error handling for incorrect user input.
                   
                    except ValueError:
                        print("Invalid input. Please enter a whole number.") #error handling for incorrect user input.
            else:
                print("Enter a valid choice (0, 1, or 2).") #error handling for incorrect user input.
        except ValueError:
            print("Invalid input. Please enter a valid number.") #error handling for incorrect user input.


#2D Array Search
def search_2d(array2D): #parameter is passed to this fxn to allow search within the 2D array
    
    print("\nCurrent 2D Array:")
    for i, row in enumerate(array2D): #iterate ove array2D while keeping track of the row index and value
        print(f"Row {i}: {row}")#display each row of 2D array with its row #

    while True:#lopps until valid input is entered
        try:
            user = input("Enter value to search: ")
            search_val = int(user) #converts user input to int and stored it in search_val
            break  #Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    found = False  #to track if the value is found

    for r in range(len(array2D)):#loops through rows of 2D array by index to check if the value searching exist in the 2D array
        for c in range(len(array2D[r])): #iterating through the columns of the current row that first loop is currently processing
            if array2D[r][c] == search_val: #accesses the element located at row "r" and column "c"
                print(f"Value found at index: [{r}, {c}]")
                found = True  #Set found to True when value is found
                break 
        if found:  #If value is found, break from outer loop
            break
    if not found:  #Check if value was never found
        print("Value not found.")

                        
#Circular Linked List 
class Node:
    def __init__(self, data): #accepts data as argument and assigns it to self.data
        self.data = data #stores the value of node
        self.next = None #set to none as it will be user input based sample program, so node is not yet created and linked to any other node

class CircularLinkedList:

    def __init__(self):
        self.head = None #this creates a list with no nodes yet


    def insert(self, data):
        
        new_node = Node(data) #create a new node that will hold the newly input data
        if not self.head: #condition if list is empty 
            self.head = new_node #then, the head is set to the new node (making it the 1st node)
            new_node.next = self.head  #point to itself
           
        else: #if is not empty then this will execute
            current = self.head 
            while current.next != self.head: #this traverse the list until current.next points back to head (last node)
                current = current.next #updates the last node's next pointer to link it to new node
            current.next = new_node
            new_node.next = self.head #point back to head to remain the list circular
        self.display()


    def delete(self, data):
        if not self.head: #checks if the list is empty
            print("List is empty.")
            return  
        # initialize first to set that current value is the 1st node and previous as none and it will be updated as it will traverse the list
        current = self.head 
        previous = None #be updated each step

        while True:
            if current.data == data: #if the node's data macthes the value input to delete, deletion will be executed
                if previous is None:  #but it will check if the input to be deleted it the head node, if prev is none means it is at the 1st node
                    if current.next == self.head:  #Only one node case
                        self.head = None #remove the only node
                    else: #handles multiple nodes and del of head node
                        last_node = self.head #set last node as the head node
                        while last_node.next != self.head: #loops until last node points back to head node
                            last_node = last_node.next #updating last node to the next node 
                        last_node.next = self.head.next #update the last node's next to the second node
                        self.head = self.head.next # set the second node to the new head
                else:
                    previous.next = current.next  #handling del of non-head nodes

                print(f"Node '{data}' deleted.")
                self.display()#prints the updated list
                return  

            previous = current #updates the prev pointer to the current node
            current = current.next #update the current pointer to the next node

            if current == self.head:  #Back to start, means not found
                print(f"Node '{data}' not found.")
                return  


    def search(self, target):
        self.display() #calls the function to display the list
        if not self.head: #checks if the list is empty
            return False 

        current = self.head #set current as the head of the list
        while True: #loops until a returnn statement is encountered
            if current.data == target:  #checks if the current data is equal to the value searching for 
                return True #returns True if the value searching found in the list
            current = current.next #if the target was not found, moves the current pointer to the next node
            if current == self.head:  #checks if the current node looped to the head 
                return False #if it already looped back and target was not found, this returns false


    def display(self):
        if not self.head: # This checks if the list is empty. self.head would be a pointer to the first node.
            print("List is empty.")
            return

        current = self.head #This initializes a variable current to point to the first node of the list (the head).  current will be used to traverse the list.
        print("Circular Linked List:", end=" ")
        while True:
            print(current.data, end=" -> ")
            current = current.next #This moves current to the next node in the list.
            if current == self.head: #It checks if current has looped back to the head of the list. 
                print(self.head.data)  #Always print the head again
                break


#Main Function to Start the Program**
def main():
    menu()

#Start the program**
main()
