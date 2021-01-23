from tkinter import *
from core.result import *

app = Tk()

part_text = StringVar()


app.title('Rock, Paper & Scissors')
app.iconbitmap('./assets/icon.ico')
app.geometry('300x200')
app.resizable(0, 0)
app.configure(bg='#f5dd29')

# Button function
def programRun():
    move = rps.get()
    if result(move)['status'] != 200:
        v.set(result(move)['reason'])
    else:
        v.set(result(move)['result'].capitalize())
    if result(move)['status'] != 200:
        score.set(result(move)['reason'])
    else:
        score.set(f"Yours: {result(move)['user_score']}\nMine: {result(move)['client_score']}")
    rps.delete(0, END)
    rps.insert(0, "")


def close_window():
    app.destroy()
    

rps_text = Label(app, text='Enter your move:',
                 bg='#f5dd29', font=('Helvetica 12 bold'))
rps_text.grid(row=0, column=2)
rps = Entry(app, width=15, borderwidth=2, justify='center')
rps.grid(row=0, column=3, columnspan=1, padx=50, pady=10)

run = Button(app, text="Go", command=programRun)
run.grid(row=2, column=0, columnspan=3, padx=50, pady=10)

exit = Button(app, text='Exit', command=close_window)
exit.grid(row=2, column=2, columnspan=3, padx=20, pady=10)

# Result 
rps_result = Label(app, text='Result:', bg='#f5dd29', font=('Helvetica 10 bold'))
rps_result.place(relx=0.099, rely=0.5, anchor='center')

v = StringVar()
result_text = Label(app, textvariable=v, bg='#f5dd29',
                    font=('Monospace 8 bold'))

result_text.place(relx=0.45, rely=0.5, anchor='center')

# Score
rps_score = Label(app, text='Score:', bg='#f5dd29', font=('Helvetica 10 bold'))
rps_score.place(relx=0.099, rely=0.65, anchor='center')

score = StringVar()
score_text = Label(app, textvariable=score, bg='#f5dd29', font=('Monospace 8 bold'))
score_text.place(relx=0.45, rely=0.65, anchor='center')




app.mainloop()
