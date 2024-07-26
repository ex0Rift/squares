from tkinter import *
from PIL import ImageTk, Image
import random , time
global health , hscore , sp


set = Tk()


def main():
   global health , num , score , sp
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
   num=0
   score=''
   sp=speed.get()
   s = pscale.get()





   def SCORE():
       global num,score , sp

       multi=(550*(sp/100))
       multi=int(multi)
       lives.delete(score)
       score = lives.create_text(165, 25, text=num, font=('Helvetica 30 '),fill='gray100')
       num=num+1
       root.after(multi,SCORE)


   def DEL():
       items = canvas.find_all()
       items=list(items)
       for i in range(2):
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
               set.deiconify()
               a=1
               restart()
       if a == 0:
           root.after(1, COL)



   def OBJ():
       sp=speed.get()
       rx = random.randint(0, w)
       ry = random.randint(0, h)
       rs = random.randint(20, 250)
       canvas.create_rectangle(rx, ry, rx + rs, ry + rs, fill='orange')
       root.after(sp, OBJ)




   def Exit():
       root.destroy()
       set.deiconify()
       restart()




   def motion(event):
       p = canvas.coords(box)
       x, y = event.x, event.y
       # print(x,y)
       canvas.moveto(box, x, y)


       root.after(10)



   canvas = Canvas(root, width=w, height=h, bg='gray40')
   canvas.pack()
   box = canvas.create_rectangle(x, y, x + s, y + s, fill='green')


   lives = Canvas(root, width=200, height=50, bg='deepskyblue3')
   lives.place(x=(10), y=(h - 65))


   line=lives.create_line(130,0,130,55,fill='gray100',width=2)
   H1 = lives.create_rectangle(10, 10, 40, 40, fill='red')
   H2 = lives.create_rectangle(50, 10, 80, 40, fill='red')
   H3 = lives.create_rectangle(90, 10, 120, 40, fill='red')
   SCORE()
   root.bind('<Motion>', motion)
   root.bind('<space>', lambda x: Exit())


   OBJ()
   COL()
   DEL()


   root.mainloop()




#startup


def START():
   set.withdraw()
   main()


def QUIT():
   set.destroy()


def HIGH():
   file=open('data.txt','r')
   hscore = file.readline().strip()
   file.close()
   return hscore


def restart():
   global num ,hscore
   print('restart')
   if num>int(hscore):
       file = open('data.txt', 'w')
       num = str(num)
       file.write(num)
       file.close()
       hscore=num
   score_dsip.config(text=f'score {num}\nhighscore {hscore}')


wh=500
ww=250
h = set.winfo_screenwidth()
w = set.winfo_screenheight()
x=(h-wh)//2
y=(w-ww)//2
hscore=HIGH()




set.config(bg='gray40')
set.overrideredirect(True)
set.geometry(f'{wh}x{ww}+{x}+{y}')


start=Button(set,text='Start',command=START,bg='gray60',width=10)
quit=Button(set,text='Quit',command=QUIT,bg='gray60',width=10)
score_dsip=Label(set,text=(f'highscore {hscore}'),bg='gray40',font=('Helvetica 10 bold'))
speed=Scale(set,from_=100,to=800,orient=HORIZONTAL,length=250,resolution=10,label='spawn speed',bg='gray40',troughcolor='gray40',highlightbackground='gray45')
pscale=Scale(set,from_=40,to=150,orient=HORIZONTAL,length=250,resolution=10,label='player size',bg='gray40',troughcolor='gray40',highlightbackground='gray45')

start.place(x=20,y=190)
quit.place(x=400,y=190)
score_dsip.place(x=215,y=210)
speed.place(x=125,y=140)
pscale.place(x=125,y=80)
speed.set(200)
pscale.set(50)




set.mainloop()


'''
file name is data.txt
'''



