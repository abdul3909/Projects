from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

con = pymysql.connect(host="localhost", user="root", password="7654321", database="librarydata")
cur = con.cursor()


def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="DarkSeaGreen4")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="SpringGreen4", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='DarkSeaGreen3', fg='black', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='DarkSeaGreen1')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='DarkSeaGreen1', fg='black')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='antique white', fg='black', command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='antique white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def deleteBook():
    bid = bookInfo1.get()

    # f_keyCheck1 = "SET FOREIGN_KEY_CHECKS=0"
    # f_keyCheck2 = "SET FOREIGN_KEY_CHECKS=1"
    deleteSql = "delete from books where bid = '" + bid + "'"
    # deleteMember = "delete from member where member_id = '" + bid + "'"
    # deleteUser = "delete from user where userId = '" + bid + "'"
    deleteIssue = "delete from books_issued where bid = '" + bid + "'"

    try:
        #cur.execute(deleteMember)
        #con.commit()
        #cur.execute(deleteUser)
        #con.commit()
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()

        messagebox.showinfo('Success', "Book Record Deleted Successfully")

    except:
        messagebox.showerror("Error", "Check Book Id")

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()
