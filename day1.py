import sys,datetime
x = datetime.datetime.today().strftime("%d %B %Y")

bookInfo = sys.stdin.readline().split(" - ")


if len(bookInfo) != 2:
    print("Wrong input")
else:
    print("Book name: " + bookInfo[0] + "\nWriter: " + bookInfo[1] + "Added in: " + x)


