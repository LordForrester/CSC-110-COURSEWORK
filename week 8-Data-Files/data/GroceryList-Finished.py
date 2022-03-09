def main():
    groceryList = []
    choice = -99
    while choice != 0:
        print("Grocery List Helper")
        print()
        print("1. Read list from file")
        print("2. Display list")
        print("3. Add item to list")
        print("4. Remove item from list")
        print("5. Sort list")
        print("6. Write list to file")
        print("0. Exit")
        print()
        choice = int(input("Enter choice: "))
        
        if choice >= 1 and choice <= 6:

            if choice == 1:
                groceryFile = open("GroceryList.txt", "r")
                for oneItem in groceryFile:
                    groceryList.append(oneItem.strip())
                groceryFile.close()
                
            elif choice == 2:
                for oneItem in groceryList:
                    print(oneItem)

            elif choice == 3:
                newItem = input("Enter new grocery item: ")
                groceryList.append(newItem)
                print("Item was added to the list")

            elif choice == 4:
                deleteItem = input("Enter the item to remove: ")
                if deleteItem in groceryList:
                    groceryList.remove(deleteItem)
                    print("Item was removed from the list")
                else:
                    print("Item was not found on the list")

            elif choice == 5:
                groceryList.sort()
                print("List was sorted")

            elif choice == 6:
                groceryFile = open("GroceryList.txt", "w")
                for oneItem in groceryList:
                    groceryFile.write(oneItem + "\n")
                groceryFile.close()
                print("List was saved to the file")
                
            input("\nPress <Enter> to continue")    

if __name__ == "__main__":
    main()
