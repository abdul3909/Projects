import datetime
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import pymysql
import viewBook


def bookRegister():
    bid = bookId.get()
    title = bookTitle.get()
    author = authorName.get()
    status = bookStatus.get()
    status = status.lower()
    user_name = userName.get()
    user_address = userAddress.get()
    member_type = memberType.get()
    member_desc = memberDesc.get()
    member_email = memberEmail.get()
    library_section = librarySection.get()
    book_category = bookCategory.get()
    book_language = bookLanguage.get()
    days_offered = offerDays.get()
    date_borrowed = dateBorrow.get()
    due_date = dueDate.get()
    actual_price = price.get()
    late_fine = lateFine.get()
    pub_name = pubName.get()
    pub_loc = pubLoc.get()
    mem_gender = gender.get()

    insertBooks = "insert into  books values ('" + bid + "','" + title + "','" + author + "','" + status + "')"
    insertUser = "INSERT INTO user VALUES ('" + bid + "','" + user_name + "', '" + user_address + "')"
    insertMember = "INSERT INTO member VALUES ('" + bid + "','" + member_type + "', '" + member_desc + "', '" + member_email + "')"
    insertSection = "INSERT INTO section VALUES ('" + bid + "','" + library_section + "', '" + book_category + "', '" + book_language + "')"
    insertDays = "INSERT INTO days VALUES ('" + bid + "','" + days_offered + "', '" + date_borrowed + "', '" + due_date + "')"
    insertPrice = "INSERT INTO price VALUES ('" + bid + "','" + actual_price + "', '" + late_fine + "')"
    insertPublisher = "INSERT INTO publisher VALUES ('" + bid + "','" + pub_name + "', '" + pub_loc + "')"
    insertGender = "INSERT INTO gender VALUES ('" + bid + "', '" + mem_gender + "')"
    insertBookType = "insert into  book_type values ('" + bid + "','" + book_language + "','" + book_category + "')"
    insertAvail = "INSERT INTO availability VALUES ('" + bid + "','" + title + "', '" + status + "')"
    insertUserInfo = "INSERT INTO user_info VALUES ('" + bid + "','" + member_desc + "', '" + member_email + "')"
    insertPubInfo = "INSERT INTO publisher_info VALUES ('" + bid + "','" + book_category + "', '" + member_email + "')"
    insertMemInfo = "INSERT INTO member_info VALUES ('" + bid + "','" + user_name + "', '" + mem_gender + "')"

    try:
        cur.execute(insertBooks)
        con.commit()
        cur.execute(insertUser)
        con.commit()
        cur.execute(insertMember)
        con.commit()
        cur.execute(insertSection)
        con.commit()
        cur.execute(insertDays)
        con.commit()
        cur.execute(insertPrice)
        con.commit()
        cur.execute(insertPublisher)
        con.commit()
        cur.execute(insertGender)
        con.commit()
        cur.execute(insertBookType)
        con.commit()
        cur.execute(insertAvail)
        con.commit()
        cur.execute(insertUserInfo)
        con.commit()
        cur.execute(insertPubInfo)
        con.commit()
        cur.execute(insertMemInfo)
        con.commit()


        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showerror("Error", "There was some error, Try Again!")

    print(bid)
    print(title)
    print(author)
    print(status)
    root.destroy()


def addBook():
    # For books
    global bookId, bookTitle, authorName, bookStatus, Canvas1, con, cur, bookTable, root
    # For user table
    global userId, userName, userAddress
    # For member table
    global memberType, memberDesc, memberEmail
    # For section table
    global librarySection, bookLanguage, bookCategory
    # For days table
    global offerDays, dateBorrow, dueDate
    # For price table
    global price, lateFine
    # For publisher table
    global pubName, pubLoc
    # For gender table
    global gender

    # Declaring variables to fetch data from user input
    var_bookID = StringVar()
    var_bTitle = StringVar()
    var_authName = StringVar()
    var_dateBor = StringVar()
    var_dueDate = StringVar()
    var_offerDays = StringVar()
    var_lateFine = StringVar()
    var_authNo = StringVar()
    var_actualPrice = StringVar()

    root = Tk()
    root.title("Library")
    root.minsize(width=900, height=650)
    root.geometry("900x600")

    con = pymysql.connect(host="localhost", user="root", password="7654321", database="librarydata")
    cur = con.cursor()

    # Title for application
    label_title = Label(root, text="LIBRARY MANAGEMENT SYSTEM", bg="navajo white", fg="DarkGoldenrod4", bd=16,
                        relief=GROOVE, font=("Times", "34", "bold"), padx=2, pady=6)
    label_title.pack(side=TOP, fill=X)

    # Setting parent frame
    frame = LabelFrame(root, bg="navajo white", bd=10, relief=GROOVE, padx=20)
    frame.place(x=0, y=90, width=1024, height=360)

    #                      ********Setting frame inside parent frame*********
    #                        ==================lEFT Frame===================
    frame_left = LabelFrame(frame, text="Membership Information", bg="navajo white", fg="DarkGoldenrod4", bd=6,
                            relief=SUNKEN,
                            font=("Times", "10", "bold"))
    frame_left.place(x=0, y=1, width=650, height=340)

    # Creating Labels and entries
    # --1
    label1 = Label(frame_left, bg="navajo white", text="Member Type:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label1.grid(row=0, column=0, sticky=W)
    # Creating dropdown
    memberType = ttk.Combobox(frame_left, font=("Times", "12", "bold"), state="readonly", width=18)
    memberType["value"] = ("Admin", "Student", "Lecturer")
    memberType.grid(row=0, column=1)

    # --2
    label2 = Label(frame_left, bg="navajo white", text="Book ID:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label2.grid(row=1, column=0, sticky=W)
    bookId = Entry(frame_left, font=("Times", "12", "bold"), textvariable=var_bookID, width=20)
    bookId.grid(row=1, column=1)

    # --3
    label3 = Label(frame_left, bg="navajo white", text="Title:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label3.grid(row=2, column=0, sticky=W)
    bookTitle = Entry(frame_left, font=("Times", "12", "bold"), textvariable=var_bTitle, width=20)
    bookTitle.grid(row=2, column=1)

    # --4
    bookInfo3 = Label(frame_left, bg="navajo white", text="Author Name:", font=("Times", "10", "bold"),
                      padx=10, pady=6)
    bookInfo3.grid(row=3, column=0, sticky=W)
    authorName = Entry(frame_left, font=("Times", "12", "bold"), textvariable=var_authName, width=20)
    authorName.grid(row=3, column=1)

    # --5
    label5 = Label(frame_left, bg="navajo white", text="Status:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label5.grid(row=4, column=0, sticky=W)
    bookStatus = ttk.Combobox(frame_left, font=("Times", "12", "bold"), state="readonly", width=18)
    bookStatus["value"] = ("avail", "issued")
    bookStatus.grid(row=4, column=1)

    # --7
    label7 = Label(frame_left, bg="navajo white", text="User Name:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label7.grid(row=5, column=0, sticky=W)
    userName = Entry(frame_left, font=("Times", "12", "bold"), width=20)
    userName.grid(row=5, column=1)

    # --8
    label8 = Label(frame_left, bg="navajo white", text="User Address:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label8.grid(row=6, column=0, sticky=W)
    userAddress = Entry(frame_left, font=("Times", "12", "bold"), width=20)
    userAddress.grid(row=6, column=1)

    # # --9
    label9 = Label(frame_left, bg="navajo white", text="Member job description:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label9.grid(row=7, column=0, sticky=W)
    memberDesc = Entry(frame_left, font=("Times", "12", "bold"), width=20)
    memberDesc.grid(row=7, column=1)

    # --10
    label10 = Label(frame_left, bg="navajo white", text="Member Email:", font=("Times", "10", "bold"),
                    padx=10, pady=6)
    label10.grid(row=8, column=0, sticky=W)
    memberEmail = Entry(frame_left, font=("Times", "12", "bold"), width=20)
    memberEmail.grid(row=8, column=1)

    # --11
    label11 = Label(frame_left, bg="navajo white", text="Library Section:", font=("Times", "10", "bold"),
                    padx=10, pady=6)
    label11.grid(row=9, column=2, sticky=W)
    librarySection = Entry(frame_left, font=("Times", "12", "bold"), width=20)
    librarySection.grid(row=9, column=3)

    # --12
    label12 = Label(frame_left, bg="navajo white", text="Book Category:", font=("Times", "10", "bold"),
                    padx=10, pady=6)
    label12.grid(row=0, column=2, sticky=W)
    bookCategory = Entry(frame_left, font=("Times", "12", "bold"), width=20)
    bookCategory.grid(row=0, column=3)

    # --13
    label2 = Label(frame_left, bg="navajo white", text="Book Language:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label2.grid(row=1, column=2, sticky=W)
    bookLanguage = Entry(frame_left, font=("Times", "12", "bold"), width=20)
    bookLanguage.grid(row=1, column=3)

    # --14
    label2 = Label(frame_left, bg="navajo white", text="Offered Days:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label2.grid(row=2, column=2, sticky=W)
    offerDays = Entry(frame_left, font=("Times", "12", "bold"), textvariable=var_offerDays, width=20)
    offerDays.grid(row=2, column=3)

    # --15
    label2 = Label(frame_left, bg="navajo white", text="Date Borrowed:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label2.grid(row=3, column=2, sticky=W)
    dateBorrow = Entry(frame_left, font=("Times", "12", "bold"), textvariable=var_dateBor, width=20)
    dateBorrow.grid(row=3, column=3)

    # --16
    label2 = Label(frame_left, bg="navajo white", text="Due Date:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label2.grid(row=4, column=2, sticky=W)
    dueDate = Entry(frame_left, font=("Times", "12", "bold"), textvariable=var_dueDate, width=20)
    dueDate.grid(row=4, column=3)

    # --18
    label2 = Label(frame_left, bg="navajo white", text="Actual Price:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label2.grid(row=5, column=2, sticky=W)
    price = Entry(frame_left, font=("Times", "12", "bold"), textvariable=var_actualPrice, width=20)
    price.grid(row=5, column=3)

    # --17
    label3 = Label(frame_left, bg="navajo white", text="Late Fine:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label3.grid(row=6, column=2, sticky=W)
    lateFine = Entry(frame_left, font=("Times", "12", "bold"), textvariable=var_lateFine, width=20)
    lateFine.grid(row=6, column=3)

    label3 = Label(frame_left, bg="navajo white", text="Publisher Name:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label3.grid(row=7, column=2, sticky=W)
    pubName = Entry(frame_left, font=("Times", "12", "bold"), width=20)
    pubName.grid(row=7, column=3)

    label3 = Label(frame_left, bg="navajo white", text="Publisher Location:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label3.grid(row=8, column=2, sticky=W)
    pubLoc = Entry(frame_left, font=("Times", "12", "bold"), width=20)
    pubLoc.grid(row=8, column=3)

    label4 = Label(frame_left, bg="navajo white", text="Gender:", font=("Times", "10", "bold"),
                   padx=10, pady=6)
    label4.grid(row=9, column=0, sticky=W)
    # Creating dropdown
    gender = ttk.Combobox(frame_left, font=("Times", "12", "bold"), state="readonly", width=18)
    gender["value"] = ("Male", "Female", "Other")
    gender.grid(row=9, column=1)


    # Submit Button
    bottom_Frame = LabelFrame(root, bg="navajo white", bd=10, relief=GROOVE, padx=20)
    bottom_Frame.place(x=0, y=450, height=200, width=900)

    SubmitBtn = Button(bottom_Frame, text="SUBMIT", bg='antique white', fg='black', command=bookRegister, width=25,
                       height=3)
    SubmitBtn.grid(row=0, column=0, padx=100)

    quitBtn = Button(bottom_Frame, text="Quit", bg='antique white', fg='black', command=root.destroy, width=25,
                     height=3)
    quitBtn.grid(row=0, column=1, padx=20)

    root.mainloop()
