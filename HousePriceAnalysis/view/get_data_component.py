from tkinter import messagebox
import tkinter as tk
from logic import storage


def get_data_component(master, app_size, data):
    app_width, app_height = app_size
    data_amount = len(data)

    canvas = tk.Canvas(master=master,
                       width=app_width, height=app_height,
                       scrollregion=(0, 0, 0, app_height + data_amount*28))
    canvas.place(x=0, y=0)

    frame_height = app_height + data_amount*28
    frame = tk.Frame(canvas, bg='snow', width=app_width, height=frame_height)

    i, j = 10, 0
    while i <= 40*data_amount:
        tk.Label(master=frame, text='Area: ', fg='teal', bg='ghostwhite', font=('Times', 16, 'bold')).place(
            relx=0, y=i, width=70, height=30)
        tk.Label(master=frame, text=data[j]['area'], fg='red', bg='ghostwhite', font=(
            'Times', 16)).place(relx=0.11, y=i, width=80, height=30)

        tk.Label(master=frame, text='Price: ', fg='teal', bg='ghostwhite', font=(
            'Times', 16, 'bold')).place(relx=0.25, y=i, width=70, height=30)
        tk.Label(master=frame, text=data[j]['price'], fg='red', bg='ghostwhite', font=(
            'Times', 16)).place(relx=0.36, y=i, width=125, height=30)

        tk.Button(master=frame, text='More info', cursor='hand2',
                  command=lambda temp=j: messagebox.showinfo(
                      title='More info', message=f'Link:  {data[temp]["link"]}'),
                  bg='black', fg='white', font=('Times', 16, 'bold')).place(relx=0.6, y=i, width=100, height=30)
        tk.Button(master=frame, text='Save', cursor='hand2',
                  command=lambda temp=j: storage.create_data(data[temp]),
                  bg='black', fg='white', font=('Times', 16, 'bold')).place(relx=0.8, y=i, width=75, height=30)

        i += 40
        j += 1

    tk.Label(master=frame, text='一'*40, fg='black', bg='snow', font=('Times', 14, 'bold')).place(
        relx=0, y=i+10, relwidth=1, height=10)
    tk.Label(master=frame, text=f'A total of {data_amount} data', fg='teal', bg='ghostwhite', font=('Times', 14, 'bold')).place(
        relx=0, y=i+35, relwidth=1, height=30)

    frame.place()

    vbar = tk.Scrollbar(canvas, orient=tk.VERTICAL)
    # The height of the navigation bar is `relheight=0.15`, so...`
    vbar.place(relx=0.97, y=0, relwidth=0.025, height=app_height*0.85)
    vbar.configure(command=canvas.yview)

    canvas.config(yscrollcommand=vbar.set)
    canvas.create_window((app_width / 2, frame_height / 2), window=frame)
