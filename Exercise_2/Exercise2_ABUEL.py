def Read():
    try:
        with open("Exercise_2/Notes.txt", "r") as Note:
            readNote = Note.read()
            print(f"\nNote:\n{readNote}")

    except FileNotFoundError:
        print("\n* Note does not exist!\n")




with open("Exercise_2/Notes.txt", "w") as Note:
    Note.write(f" - {input("- Input Note: ")}\n")


Read()


try:
    with open("Exercise_2/Notes.txt", "a") as Note:
        Note.write(f" - {input("- Input Note: ")}\n")

except FileNotFoundError:
    print("\n* Note does not exist!\n")


Read()



