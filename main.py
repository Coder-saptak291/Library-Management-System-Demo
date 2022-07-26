import datetime
wel_msg = ["Wings of Fire", "My experiments with truth",
           "Learn python", "Coding for absolute beginners"]


def wel():
    for i in wel_msg:
        print("     ", i)


def ask():
    print("=====Welcome to the library=====")
    opt = ["1.List of books", "2.Request a book",
           "3.Return your book", "4.exit the library"]
    for j in opt:
        print("        ", j)
    ch = int(input("Enter what you want to do="))
    if ch == 1:
        wel()
        ask()
    if ch == 2:
        name = input("Enter your name = ")
        chb = input("Enter your choice=")
        f = open("borrow.txt","a")
        f.write(f"Name: {name}")
        f.write("\n")
        f.write(f"Book Borrowed: {chb}")
        f.write("\n")
        f.close()
        print("Thank you for using us. You will have to return this within 200 days")
        ask()
    if ch == 3:

        rb = str(input("Enter the name of the book="))
        for i in range(4):
            if rb == wel_msg[i]:
                print("Thank you for returning the book")
                exit()

    if ch == 4:
        print("Thank you for using us")
        exit()


ask()
