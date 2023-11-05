import tkinter as tk

root = tk.Tk()

b1 = tk.Text(root, text='b1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1\nb1')
b2 = tk.Text(root, text='b2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2\nb2')
b1.pack(side=tk.LEFT)      # pack starts packing widgets on the left 
b2.pack(side=tk.LEFT)      # and keeps packing them to the next place available on the left
root.mainloop()
