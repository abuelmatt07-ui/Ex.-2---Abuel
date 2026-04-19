def Read():
    try:
        with open("Exercise_2/Notes.txt", "r") as Note:
            readNote = Note.read()
            print(f"\nNote:\n{readNote}")

    except FileNotFoundError:
        print("\n* Create note first!\n")

def Write():
    with open("Exercise_2/Notes.txt", "w") as Note:
        Note.write(f" - {input("- Input Note: ")}\n")

def Append():
    try:
        with open("Exercise_2/Notes.txt", "r") as Note:
            pass
          
        with open("Exercise_2/Notes.txt", "a") as Note:
            Note.write(f" - {input("- Input Note: ")}\n")

    except FileNotFoundError:
        print("\n* Create note first!\n")

choices = ["1", "2", "3", "4"]

while True:

    print(f"\n{' INotes ':-^18}")
    print("1. Write new note.\n2. Write on note.\n3. Read note.\n4. Exit")

    while True:
        try:
            userIn = input("\n- Choice: ")
            if userIn != "":

                if userIn in choices:
                    break
                else:
                    print("* Not valid choice! (1, 2, 3, 4)")
            
            else:
                print("* Please input choice! (1, 2, 3, 4)")
                    

        except:
            print("* Input Error!")

    match userIn:
        
        case "1":
            Write()
        
        case "2":
            Append()

        case "3":
            Read()

        case "4":

            print("- EXITING PROGRAM...")

            break

