

with open("Exercise 2/Notes.txt", "w") as Note:
    Note.write(input("Input Note: "))


try:
    with open("Exercise 2/Notes.txt", "r") as Note:
        readNote = Note.read()
        print(f"\nNote:\n - {readNote}\n")

except FileNotFoundError:
    print("\n* Note does not Exist!\n")






