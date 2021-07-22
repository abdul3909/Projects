from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="7654321", database="librarydata")
cur = conn.cursor()


def View():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="honeydew4")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="aquamarine4", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='honeydew3', fg='black', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='honeydew2')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    # Making scroll bars inside frame
    xscroll = ttk.Scrollbar(labelFrame, orient=HORIZONTAL)
    yscroll = ttk.Scrollbar(labelFrame, orient=VERTICAL)

    # Setting column names for the table
    library_table = ttk.Treeview(labelFrame, column=("book_Id", "book_Title", "author_Name", "book_Status", "user_Id",
                                                     "user_Name", "user_Address", "member_Type", "member_Desc", "member_Email",
                                                     "library_Section", "book_Category", "book_Language", "offer_Days",
                                                     "date_Borrowed", "due_Date", "actual_Price", "late_Fine",
                                                     "pub_Name", "pub_Loc", "Gender"),
                                 xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

    xscroll.pack(side=BOTTOM, fill=X)
    yscroll.pack(side=RIGHT, fill=Y)

    xscroll.config(command=library_table.xview)
    yscroll.config(command=library_table.yview)

    # Adding column names for the table
    library_table.heading("book_Id", text="Book Id")
    library_table.heading("book_Title", text="Title")
    library_table.heading("author_Name", text="Author")
    library_table.heading("book_Status", text="Status")
    library_table.heading("user_Id", text="User Id")
    library_table.heading("user_Name", text="User Name")
    library_table.heading("user_Address", text="User Address")
    library_table.heading("member_Type", text="Member Type")
    library_table.heading("member_Desc", text="Member Description")
    library_table.heading("member_Email", text="Member Email")
    library_table.heading("library_Section", text="Library Section")
    library_table.heading("book_Category", text="Book Category")
    library_table.heading("book_Language", text="Book Language")
    library_table.heading("offer_Days", text="Offered Days")
    library_table.heading("date_Borrowed", text="Date Borrowed")
    library_table.heading("due_Date", text="Due Date")
    library_table.heading("actual_Price", text="Price")
    library_table.heading("late_Fine", text="Late Fine")
    library_table.heading("pub_Name", text="Publisher Name")
    library_table.heading("pub_Loc", text="Publisher Location")
    library_table.heading("Gender", text="Gender")

    # Setting width of output columns
    library_table.column("book_Id", width=100)
    library_table.column("book_Title", width=100)
    library_table.column("author_Name", width=100)
    library_table.column("book_Status", width=100)
    library_table.column("user_Id", width=100)
    library_table.column("user_Name", width=100)
    library_table.column("user_Address", width=100)
    library_table.column("member_Type", width=100)
    library_table.column("member_Desc", width=100)
    library_table.column("member_Email", width=100)
    library_table.column("library_Section", width=100)
    library_table.column("book_Category", width=100)
    library_table.column("book_Language", width=100)
    library_table.column("offer_Days", width=100)
    library_table.column("date_Borrowed", width=100)
    library_table.column("due_Date", width=100)
    library_table.column("actual_Price", width=100)
    library_table.column("late_Fine", width=100)
    library_table.column("pub_Name", width=100)
    library_table.column("pub_Loc", width=100)
    library_table.column("Gender", width=100)

    # Showing column names in the table
    library_table["show"] = "headings"
    library_table.pack(fill=BOTH, expand=1)
    # getBooks = "select * from books"
    try:
        cur.execute("SELECT books.bid, books.title, books.author, books.status, user.userId, user.user_name, user.user_address, member.member_type, member.member_desc, member.member_email, section.library_Section, section.book_Category, section.book_Language, days.offered_days, days.date_borrowed, days.due_date, price.Price, price.late_fine, publisher.publisher_name, publisher.publisher_location, gender.Gender FROM books, user, member, section, days, price, publisher, gender")
        rows = cur.fetchall()

        for row in rows:
            library_table.insert("", END, values=row)

    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='antique white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()



