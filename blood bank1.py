# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of Tkinter Frame
win = Tk()
# Set the geometry of Tkinter Frame
win.geometry("700x450")

# Open the Image File
bg = ImageTk.PhotoImage(file="bank.png")

# Create a Canvas
canvas = Canvas(win, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("bank.png")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height))

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
win.bind("<Configure>", resize_image)

def donor():
    def reg():
        T = Toplevel()
        l1 = Label(T, text="NAME")
        l1.pack()
        t1 = Entry(T)
        t1.pack()
        l2 = Label(T,text="GENDER")
        l2.pack()
        t2 = Entry(T)
        t2.pack()
        l3 = Label(T, text="AGE")
        l3.pack()
        t3 = Entry(T)
        t3.pack()
        l4 = Label(T, text="MOBILENO")
        l4.pack()
        t4 = Entry(T)
        t4.pack()
        l5 = Label(T, text="BLOOD GROUP")
        l5.pack()
        t5=Entry(T)
        t5.pack()
        l6=Label(T,text="CITY")
        l6.pack()
        t6=Entry(T)
        t6.pack()
        def submit():
            import pymysql
            db=pymysql.connect(host='localhost',user='root',password='Swati@0209',database='bloodbank')
            a=t1.get()
            b=t2.get()
            c=int(t3.get())
            d=int(t4.get())
            e=t5.get()
            f=t6.get()
            sql="insert into donor values(%s,%s,%s,%s,%s,%s)"
            val=(a,b,c,d,e,f)
            cur=db.cursor()
            cur.execute(sql,val)
            db.commit()
            print(a,b,c,d,e,f)
        b1=Button(T,text="SUBMIT",command=submit)
        b1.pack()

    T=Toplevel()
    b1=Button(T,text="REGISTRATION",command=reg)
    b1.pack()

def recipient():
    def reg1():
        T=Toplevel()
        l1=Label(T,text="NAME")
        l1.pack()
        t1 = Entry(T)
        t1.pack()
        l2=Label(T, text="GENDER")
        l2.pack()
        t2 = Entry(T)
        t2.pack()
        l3=Label(T,text="AGE")
        l3.pack()
        t3 = Entry(T)
        t3.pack()
        l4=Label(T,text="MOBILE NO")
        l4.pack()
        t4 = Entry(T)
        t4.pack()
        l5=Label(T, text="CITY")
        l5.pack()
        t5 = Entry(T)
        t5.pack()
        l6=Label(T,text="REQUIRED DATE")
        l6.pack()
        t6=Entry(T)
        t6.pack()

        def submit1():
            import pymysql
            db = pymysql.connect(host='localhost', user='root', password='Swati@0209', database='bloodbank')
            a = t1.get()
            b = t2.get()
            c = int(t3.get())
            d = int(t4.get())
            e = t5.get()
            f = t6.get()
            sql = "insert into recipient values(%s,%s,%s,%s,%s,%s)"
            val = (a, b, c, d, e, f)
            cur = db.cursor()
            cur.execute(sql, val)
            db.commit()
            print(a, b, c, d, e, f)
        b2 = Button(T, text="SUBMIT", command=submit1)
        b2.pack()

    T= Toplevel()
    b3= Button(T, text="REGISTRATION", command= reg1)
    b3.pack()

def admin():
    T= Toplevel()
    l1= Label(T,text="NAME")
    l1.pack()
    t1=Entry(T)
    t1.pack()
    l2=Label(T,text="PASSWORD")
    l2.pack()
    t2=Entry(T)
    t2.pack()
    def login():
        import pymysql
        db = pymysql.connect(host='localhost', user='root', password='Swati@0209', database='bloodbank')
        c=0
        a= t1.get()
        b= t2.get()
        sql= "select * from admin"
        cur= db.cursor()
        cur.execute(sql)
        for row in cur.fetchall():
            if row[0] == a and row[1] == b:
                c = c+1
        print(c)
        if c == 0:
            print("invalid")
        else:
            print("valid")
            T=Toplevel()
            import pymysql

            db = pymysql.connect(host='localhost', user='root', password='Swati@0209', database='bloodbank')
            def delt():
                a= t11.get()
                b= t21.get()
                print(a,b)
                sql= "delete from donor where name=%s and age=%s"
                value=(a,b)
                cur= db.cursor()
                cur.execute(sql,value)
                db.commit()
                print("save")

            l1=Label(T, text="name")
            l1.pack()
            t11=Entry(T)
            t11.pack()
            l2 = Label(T, text="age")
            l2.pack()
            t21 = Entry(T)
            t21.pack()

            b1=Button(T,text="delete donor",command=delt)
            b1.pack()
    b6= Button(T, text="login", command=login)
    b6.pack()



b1=Button(text="DONOR",command=donor)
b1.place(x=400,y=150,width=80,height=30)
b2=Button(text="RECIPIENT",command=recipient)
b2.place(x=600,y=150,width=80,height=30)
b3=Button(text="ADMIN", command=admin)
b3.place(x=800,y=150,width=80,height=30)

win.mainloop()