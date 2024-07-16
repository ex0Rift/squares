from tkinter import *
import random
global health


set = Tk()


def main():
   global health
   root = Tk()
   root.focus_force()
   root.attributes('-fullscreen', True)
   root.attributes('-alpha', 0.6)
   root.configure(bg='gray40')
   root.config(cursor='none')


   health = 3
   h = root.winfo_screenheight()
   w = root.winfo_screenwidth()
   x = 10
   y = 10
   s = 50




   def DEL():
       items = canvas.find_all()
       items=list(items)
       r=random.randint(1,items[-1])
       if r!=1:
           canvas.itemconfig(r, state='hidden')


       root.after(600,DEL)


   def COL():
       global health
       a = 0
       p = canvas.coords(box)
       # print(p)
       coll = canvas.find_overlapping(p[0], p[1], p[2], p[3])
       coll = list(coll)
       #print(coll)
       if len(coll) != 1:
           if health == 3:
               print('first hit')
               health = 2
               lives.itemconfig(H3, state='hidden')
               a = 1
               root.after(1000, COL)
           elif health == 2:
               print('second hit')
               lives.itemconfig(H2, state='hidden')
               health = 1
               a = 1
               root.after(1000, COL)
           elif health == 1:
               print('third hit')
               lives.itemconfig(H1, state='hidden')
               health = 0
               a = 1
               root.after(1000, COL)
           elif health == 0:
               print('dead')
               root.destroy()
       if a == 0:
           root.after(1, COL)




   def OBJ():
       rx = random.randint(0, w)
       ry = random.randint(0, h)
       rs = random.randint(20, 250)
       canvas.create_rectangle(rx, ry, rx + rs, ry + rs, fill='orange')
       root.after(200, OBJ)




   def Exit():
       root.destroy()




   def motion(event):
       p = canvas.coords(box)
       x, y = event.x, event.y
       # print(x,y)
       canvas.moveto(box, x, y)


       root.after(10)




   canvas = Canvas(root, width=w, height=h, bg='gray40')
   canvas.pack()
   box = canvas.create_rectangle(x, y, x + s, y + s, fill='green')


   lives = Canvas(root, width=130, height=50, bg='deepskyblue3')
   lives.place(x=(10), y=(h - 65))


   H1 = lives.create_rectangle(10, 10, 40, 40, fill='red')
   H2 = lives.create_rectangle(50, 10, 80, 40, fill='red')
   H3 = lives.create_rectangle(90, 10, 120, 40, fill='red')


   root.bind('<Motion>', motion)
   root.bind('<space>', lambda x: Exit())


   OBJ()
   COL()
   DEL()


   root.mainloop()




#startup


def START():
   set.destroy()
   main()


def QUIT():
   set.destroy()


wh=500
ww=250
h = set.winfo_screenwidth()
w = set.winfo_screenheight()
x=(h-wh)//2
y=(w-ww)//2






set.config(bg='gray40')
set.overrideredirect(True)
set.geometry(f'{wh}x{ww}+{x}+{y}')


start=Button(set,text='Start',command=START,bg='gray60',width=10)
quit=Button(set,text='Quit',command=QUIT,bg='gray60',width=10)
start.place(x=20,y=190)
quit.place(x=400,y=190)




set.mainloop()
