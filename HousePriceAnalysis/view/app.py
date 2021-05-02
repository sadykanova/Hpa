import tkinter as tk

from logic import handle_response, storage

if __name__ == '__main__':
    from storage_component import storage_component
    from get_data_component import get_data_component
else:
    from .storage_component import storage_component
    from .get_data_component import get_data_component


root = tk.Tk()


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.resizable(False, False)
        self.master.title('Hourse Price Anaylysis')
        # layout center screen
        self.app_width, self.app_height, = int(
            self.master.winfo_screenwidth() * 0.4), int(root.winfo_screenheight() * 0.5)
        self.master.geometry(
            f'{self.app_width}x{self.app_height}+{int(root.winfo_screenwidth() * 0.5 - root.winfo_screenwidth() * 0.4 / 2)}+{int(root.winfo_screenheight() * 0.5 - root.winfo_screenheight() * 0.5 / 2)}')

        self.place(x=0, y=0)
        self.build()

    def build(self):
        self.header = tk.Frame(self.master, bg='aliceblue')
        self.header.place(x=0, y=0, relwidth=1, relheight=0.15)
        self.main = tk.Frame(self.master, bg='lavender')
        self.main.place(x=0, rely=0.15, relwidth=1, relheight=0.85)

        self.header__logo = tk.Label(master=self.header, text='HPA', bg='aliceblue', fg='navy', font=('Times', 20, 'bold')).place(
            x=0, y=0, relwidth=0.15, relheight=1
        )
        self.header__btns = tk.Frame(master=self.header, bg='aliceblue')
        self.header__btns.place(relx=0.15, y=0, relwidth=0.85, relheight=1)
        self.header__btns__view_btn = tk.Button(
            master=self.header__btns, text='Storage', command=lambda: self.change_content('storage'), cursor='hand2', bg='black', fg='white', font=('Times', 18, 'bold')).place(
                relx=0.535, rely=0.4 / 2, relwidth=0.2, relheight=0.6
        )
        self.header__btns__get_btn = tk.Button(
            master=self.header__btns, text='Get Data', command=lambda: self.change_content('get_data'), cursor='hand2', bg='black', fg='white', font=('Times', 18, 'bold')).place(
                relx=0.765, rely=0.4 / 2, relwidth=0.2, relheight=0.6
        )

        # self.change_content('storage')
        self.change_content('get_data')

    def change_content(self, target_content):
        if target_content == 'storage':
            hourse_data_in_db = storage.read_data()
            return storage_component(self.main, app_size=(self.app_width, self.app_height), data=hourse_data_in_db)
        if target_content == 'get_data':
            hourse_data = handle_response.hourse_data()
            return get_data_component(self.main, app_size=(self.app_width, self.app_height), data=hourse_data)


if __name__ == '__main__':
    app = App(master=root)
    app.mainloop()
