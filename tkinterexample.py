import tkinter as tk
root=tk.Tk()                                                                            #make a new window
root.title('This is the Tk class')                                                      #change the window's name
root.geometry('300x350')                                                                #change the window's size
t=tk.StringVar(value='This is an Entry')                                                #used for storing value in textbox
i=tk.IntVar(value=0)                                                                    #used for storing value of radiobutton
b=tk.BooleanVar(value=False)                                                            #used for storing value of checkbutton 1
b2=tk.BooleanVar(value=False)                                                           #used for storing value of checkbutton 2
canvas=tk.Canvas(root,bg='black',width=200,height=100)                                  #make a canvas
ctext=canvas.create_text(100,50,text='This is a Canvas',fill='white')                   #make text on the canvas
checkbutton=tk.Checkbutton(root,text='This is a Checkbutton',variable=b)                #make checkbutton 1
checkbutton2=tk.Checkbutton(root,text='This is also a Checkbutton',variable=b2)         #make checkbutton 2
radiobutton=tk.Radiobutton(root,text='This is a Radiobutton',value=1,variable=i)        #make radiobutton 1
radiobutton2=tk.Radiobutton(root,text='This is also a Radiobutton',value=2,variable=i)  #make radiobutton 2
entry=tk.Entry(root,textvariable=t)                                                     #make the textbox
label=tk.Label(root,text='This is a Label')                                             #make a label
scale=tk.Scale(root, from_=0, to=500, orient=tk.HORIZONTAL,label='This is a Scale')     #make a slider with minimum value 0 and maximum value 500
def submit():                                                                           #when the button is pressed, it will run this function
    canvas.itemconfig(ctext,text=t.get())                                               #change text on canvas
    print('Checkbutton 1 value: '+str(b.get()))                                         #print if the checkbutton 1 is pressed
    print('Checkbutton 2 value: '+str(b2.get()))                                        #print if the checkbutton 2 is pressed
    if i.get()==0:                                                                      #if none of the radiobuttons have been selected
        print('No Radiobutton was selected')
    else:                                                                               #if one of the options has been selected
        print('Radiobutton '+str(i.get())+' was selected')
    print(t.get())                                                                      #print whatever text is in the textbox
    print(scale.get())                                                                  #print whatever number is on the slider
    print('---------------')
button=tk.Button(root,text='This is a Button',command=submit)                           #make the button
button.pack()                                                                           #place the button on the window
canvas.pack()                                                                           #place the canvas on the window
checkbutton.pack()                                                                      #place checkbutton 1 on the window
checkbutton2.pack()                                                                     #place checkbutton 2 on the window
radiobutton.pack()                                                                      #place radiobutton 1 on the window
radiobutton2.pack()                                                                     #place radiobutton 2 on the window
entry.pack()                                                                            #place the textbox on the window
label.pack()                                                                            #place the label on the window
scale.pack()                                                                            #place the slider on the window
root.mainloop()                                                                         #display the window