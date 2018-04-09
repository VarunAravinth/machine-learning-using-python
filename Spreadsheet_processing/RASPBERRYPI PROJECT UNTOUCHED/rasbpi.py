from Tkinter import *
from tkMessageBox import *
from tkFileDialog import askopenfilename as pickfile
from time import sleep,ctime
from time import *
from os import *
import shutil
import ttk
nm=[]
com=0
def passed():
        global nm
        d=0
        size=0
        ds=Tk()
        n=0
        ds.title('Destination USB')
        Label(ds,text="list of files in destination ",fg="red").pack(pady=20,padx=20)
        a=time()    
        Label(ds,text="Name     Size    Date modified",fg="blue").pack()
        if(com==1):
                for s in nm:
                        n=n+1
                        size=size+(path.getsize(s)/1000)
                        Label(ds,text=path.basename(s)+"        "+str(path.getsize(s)/1000)+" Kb       "+str(path.getatime(s)),fg="black").pack()
                        shutil.move(s,"d:")
                b=time()
                c=b-a
                c=int(c)
                if(c>0):
                        tr=size/(c*n)
                else:
                        tr=size/n
                while(c>=60):
                       d=d+1
                       c=c-60
                Label(ds,text="source path: "+str(path.dirname(s)),fg="red").pack()
                Label(ds,text="Destination path: E:",fg="Red").pack()
                Label(ds,text="Total size of data transferred: "+str(size)+" Kb",fg="red").pack()
                p=str(d)+" minutes "+str(c)+" seconds"
                Label(ds,text="Time taken for data transfer: "+str(p),fg="red").pack()
                Label(ds,text="Average transfer rate: "+str(tr)+" Kb/sec",fg="red").pack()
                Label(ds,text="Number of files Moved: "+str(n),fg="red").pack()
        if(com==2):
                for s in nm:
                        n=n+1
                        shutil.copy2(s,"d:")
                        size=size+(path.getsize(s)/1000)
                        Label(ds,text=path.basename(s)+"        "+str(path.getsize(s)/1000)+" Kb       "+str(path.getatime(s)),fg="black").pack()
                b=time()
                c=b-a
                c=int(c)
                if(c>=0):
                        tr=size/(c*n)
                else:
                        tr=c/n
                while(c>=60):
                       d=d+1
                       c=c-60
                Label(ds,text="source path: "+str(path.dirname(s)),fg="red").pack()
                Label(ds,text="Destination path: E:",fg="Red").pack()
                Label(ds,text="Total size of data transferred: "+str(size)+" Kb",fg="red").pack()
                p=str(d)+" minutes "+str(c)+" seconds"
                Label(ds,text="Time taken for data transfer: "+str(p),fg="red").pack()
                Label(ds,text="Average transfer rate: "+str(tr)+" Kb/sec",fg="red").pack()
                Label(ds,text="Number of files copied: "+str(n),fg="red").pack()
        ds.mainloop()
def destusb():
        f3=Tk()
        f3.title('Selection of Destination USB')
        u2=Button(f3,text='USB 2',command=passed)
	u2.pack(pady=50,padx=120)
	u3=Button(f3,text='USB 3',command=passed)
	u3.pack(pady=60,padx=120)
	u4=Button(f3,text='USB 4',command=passed)
	u4.pack(pady=70,padx=120)
	f3.mainloop()
def srcusb():
        global nm
        nm=pickfile(multiple=True)
        print nm
def pre():
        root.destroy()
        global com
	print 'after selecting files'
	f2=Tk()
	com=2
	f2.title('source file selection')
	Label(f2,text="Selected files",fg="black",bg="white").pack()
	u1=Button(f2,text='USB 1',command= srcusb)
	u1.pack(pady=50,padx=110)
	sa=Button(f2,text='paste',command= destusb)
	sa.pack(pady=40,padx=110)
	f2.mainloop()
def press():
        root.destroy()
        global com
        print 'after selecting files'
	m=Tk()
	com=1
	m.title('source file selection')
	Label(m,text="Selected files",fg="black",bg="white").pack()
	u1=Button(m,text='USB 1',command=srcusb)
	u1.pack(pady=50,padx=110)
	sa=Button(m,text='paste',command= destusb)
	sa.pack(pady=40,padx=110)
	m.mainloop()
def pressed1():
                global nm
                if(nm==[]):
                        showwarning('WARNING!','No files are selected..!')
                else:
                        if askyesno('verify','Really remove selected files?'):
                                                        showinfo('yes','deleting files')
                                                        for s in nm:
                                                                remove(s)
                        else:
                                 showinfo('no','deletion cancelled')
def remo():
        root.destroy()
        print 'after selecting files'
	f5=Tk()
	f5.title('source file selection')
	Label(f5,text="Selected files",fg="black",bg="white").pack()
	u1=Button(f5,text='USB 1',command=srcusb)
	u1.pack(pady=10,padx=10)
	u2=Button(f5,text='USB 2',command=srcusb).pack(pady=10,padx=10)
	u3=Button(f5,text='USB 3',command=srcusb).pack(pady=10,padx=10)
	u4=Button(f5,text='USB 4',command=srcusb).pack(pady=10,padx=10)
	d=Button(f5,text='next',command=pressed1).pack(pady=10,padx=10)
	f5.mainloop()
root=Tk()
root.title('selection window')
m=Button(root,text='move',command= press)
m.pack(pady=50,padx=70)
c=Button(root,text='copy',command= pre)
c.pack(pady=50,padx=80)
d=Button(root,text='delete',command= remo)
d.pack(pady=50,padx=90)
root.mainloop()

