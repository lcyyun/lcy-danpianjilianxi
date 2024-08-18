from tkinter import *
import serial
from tkinter import messagebox

ser=serial.Serial("com4",9600,timeout=0.6)

def getButton1():#当前温度
   sensord=ser.readline().decode().split(",")
   print(sensord)
   if len(sensord)>1:
      temp.set(sensord[0])#[]中数据取决于硬件端输出
   
   
   if int(sensord[0])>num1 or int(sensord[0])<num4:
      messagebox.showerror("错误","超出阈值")
def getButton2():#当前湿度
   sensord=ser.readline().decode().split(",")
   print(sensord)
   if len(sensord)>1:
      hum.set(sensord[1])
   if int(sensord[1])>num2 or int(sensord[1])<num5:
      messagebox.showerror("错误","超出阈值")
def getButton3():#当前光照
   sensord=ser.readline().decode().split(",")
   print(sensord)
   if len(sensord)>1:
      sun.set(sensord[2])
   if int(sensord[2])>num3:
      messagebox.showerror("错误","超出阈值")
   path = "D:\实验数据记录/shuju.txt"
   f = open(path,"a")
   ls=("温度：",sensord[0],"   ","湿度：",sensord[1],"  ","  光照：",sensord[2],"\n")
   f.writelines(ls)
   f.close

def A():#最高温度
   global num1
   num1=int (Entry1.get())
   print(num1)
def B(event):#最高湿度
   global num2
   num2=int (Entry2.get())
   print(num2)
def C(event):#光照
   global num3
   num3=int (Entry3.get())
   print(num3)
def D(event):#最低温度
   global num4
   num4=int (Entry4.get())
   print(num4)
def E(event):#最低湿度
   global num5
   num5=int (Entry5.get())
   print(num5)
"""def rgbR():#R
   global num6
   num6=str (Entry1.get())
   print(num1)"""
def setled():
        def setcolour():
            global r,g,b,rgbload
            
               
            r=str(ergbr.get())
            g=str(ergbg.get())
            b=str(ergbb.get())
            rgbload="G"+r+g+b
            print(rgbload)
            
            ser.write(str.encode(rgbload))

        
        sensord = ser.readline().decode()
        win=Tk()
        win.title("设置灯光颜色")
        win['width']=400;win['height']=110

        ergbr=Entry(win,width=20)
        ergbr.place(x=20,y=1)
        label1=Label(win,text = "(R)")
        label1.place(x=160,y=1)

        ergbg=Entry(win,width=20)
        ergbg.place(x=20,y=21)
        label2=Label(win,text = "(G)")
        label2.place(x=160,y=21)

        ergbb=Entry(win,width=20)
        ergbb.place(x=20,y=41)
        label3=Label(win,text = "(B)")
        label3.place(x=160,y=41)

        label2=Label(win,text = "必须000~255输入三位数，\n不足三位数在数前补零")
        label2.place(x=200,y=15)

        brgb=Button(win,text="设置颜色",width=50,command=setcolour).place(x=20,y=61)

        win.mainloop()


root = Tk()
root.title("程序设计基础实践")
root.geometry("700x250")
Label1=Label(root,text = "温湿度设置")
Label1.grid(row=0,column=0)

Button1=Button(root,text = "设置",command=A)#设置最高最低参数
Button1.grid(row=0,column=1)
Button1.bind("<Button-1>",B,add="+")
Button1.bind("<Button-1>",C,add="+")
Button1.bind("<Button-1>",D,add="+")
Button1.bind("<Button-1>",E,add="+")

Label2=Label(root,text = "最高温度：")
Label2.grid(row=1,column=0)
data1=StringVar()
Entry1=Entry(root,textvariable=data1)
Entry1.grid(row=1,column=1)

Label3=Label(root,text = "最高湿度：")
Label3.grid(row=2,column=0)
data2=StringVar()
Entry2=Entry(root,textvariable=data2)
Entry2.grid(row=2,column=1)

Label4=Label(root,text = "光照：")
Label4.grid(row=3,column=0)
data3=StringVar()
Entry3=Entry(root,textvariable=data3)
Entry3.grid(row=3,column=1)

Label5=Label(root,text = "℃")
Label5.grid(row=1,column=2,sticky=W)
Label6=Label(root,text = "%RH")
Label6.grid(row=2,column=2,sticky=W)
Label7=Label(root,text = "LUX")
Label7.grid(row=3,column=2,sticky=W)

Label8=Label(root,text = "最低温度：")
Label8.grid(row=1,column=3)
Label9=Label(root,text = "最低湿度：")
Label9.grid(row=2,column=3)

data4=StringVar()
Entry4=Entry(root,textvariable=data4)
Entry4.grid(row=1,column=4)
data5=StringVar()
Entry5=Entry(root,textvariable=data5)
Entry5.grid(row=2,column=4)

Label(root,text = "℃").grid(row=1,column=5)
Label(root,text = "%RH").grid(row=2,column=5)

Label(root,text = "传感器读取值:").grid(row=5,column=1)

temp=StringVar()
data1N=Label(root,textvariable=temp).grid(row=4,column=3,sticky=W)
Label(root,text = "温度：").grid(row=4,column=2,sticky=W)
Button2=Button(root,text = "read",command=getButton1)
Button2.grid(row=4,column=5,sticky=W)
Label(root,text = "℃").grid(row=4,column=4,sticky=W)

hum=StringVar()
data2N=Label(root,textvariable=hum).grid(row=5,column=3,sticky=W)
Label(root,text = "湿度：").grid(row=5,column=2,sticky=W)
Button3=Button(root,text = "read",command=getButton2)
Button3.grid(row=5,column=5,sticky=W)
Label(root,text = "%RH").grid(row=5,column=4,sticky=W)

sun=StringVar()
data3N=Label(root,textvariable=sun).place(x=260,y=160)
#data3N=Label(root,textvariable=sun).grid(row=6,column=3,sticky=W)
Label(root,text = "光照：").grid(row=6,column=2,sticky=W)
Button4=Button(root,text = "read",command=getButton3)
Button4.grid(row=6,column=5,sticky=W)
Label(root,text = "LUX").grid(row=6,column=4,sticky=W)

Label(root,text = "颜色设置（请输入0~255）").grid(row=7,column=1)
Button(root,text = "设置",command=setled).grid(row=7,column=2)



root.mainloop()
