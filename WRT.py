from tkinter import Label,Button,Tk
from random import randint

root = Tk()
root.title('Random Winner')
win_label = Label(root)

def pick():
    global win_label
    win_label.destroy()
    entries = ['John','Jack','Tom','Jerry']
    entries_set = set(entries)
    unique_entries = list(entries_set)
    random_num = randint(0,len(unique_entries)-1)

    winner = unique_entries[random_num]
    win_label = Label(root, text=f'Winner is: {winner}!', font=('Helvetica', 18))
    win_label.pack(pady=10)

win_button = Button(root, text='PICK OUR WINNER!!',command=pick,font=('Helvetica',24))
win_button.pack(pady=10)

root.mainloop()