from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from addBook import *
from deleteBook import *
from viewBook import *
from issueBook import *
from returnBook import *


# Connecting to database
conn = pymysql.connect(host="localhost", user="root", password="7654321", database="librarydata")
c = conn.cursor()

# Making a window
root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("800x550")

same = True
n = 1.25

# Adding background image
background_image = Image.open("image1.jfif")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)


# Adding heading
headingFrame1 = Frame(root, bg="dim gray", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Library Management System", bg='NavajoWhite3', fg='black', font=("Helvetica",
                                                                                                           17, "bold"))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# Adding Buttons
btn1 = Button(root, text="Add Book Details", bg='NavajoWhite3', font=("Helvetica", 13), fg='black', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='NavajoWhite3', font=("Helvetica", 13), fg='black', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Books", bg='NavajoWhite3', font=("Helvetica", 13), fg='black', command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book", bg='NavajoWhite3', font=("Helvetica", 13), fg='black', command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='NavajoWhite3', font=("Helvetica", 13), fg='black', command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
root.mainloop()

root.mainloop()
