# Initialize an empty dictionary to store person details
import random as m
person_dict = {}

def add_person():
    print("\n1.Entry\n2.Delete")
    cho=input("Enter what you want choice(Entry/Delete): ")
    if cho in ["entry","
    f=int(input("Input Your Id: "))
    # Check if the name is in the dictionary
    if f in person_dict:         
        print("Details found:")
        for key, value in person_dict[f].items():
            print(key,":",value)
    else:
        print("Person not found.")

# Main program loop
while True:
    print("\n1. Edit\n2. Search Person\n3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_person()

    elif choice == '2':
        search_person()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        continue 
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print(person_dict)  
