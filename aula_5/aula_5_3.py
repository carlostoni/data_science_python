import tkinter as tk


j = tk.Tk()

btn1 = tk.Button(j,text = 'Plot Bar')
btn1.pack(pady=5)

display_sta = tk.Label(j, text='', bg ='black' ,fg= 'white')

btn2 = tk.Button(j,text = 'Plot Scatter')
btn2.pack(pady=5)

btn3 = tk.Button(j,text = 'Plot Plot')
btn3.pack(pady=5)

btn4 = tk.Button(j,text = 'Plot pie')
btn4.pack(pady=5)

btn5 = tk.Button(j,text = 'Estatistica')
btn5.pack(pady=5)

j.mainloop()