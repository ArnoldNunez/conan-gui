import os

import tkinter as tk
from tkinter import ttk

from Theme import ThemeManager
from MainViewModel import MainViewModel

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Conan GUI')
        self.minsize(600, 600)
        self.geometry('800x600')
        self.configure(background='#222222')

        tm: ThemeManager = self.configure_theme()
        
        # Create view components
        self.settings_view: SettingsView = SettingsView(self, tm)
        self.main_view: MainView = MainView(self, tm)

        self.layout()

        def up(event): print('up')

        self.bind('<Up>', up)

        self.mainloop()

    def layout(self):
        '''
        Lays out the main window
        '''

        self.columnconfigure(0, weight=1, minsize=200)
        self.columnconfigure(1, weight=2, minsize=400)

        self.rowconfigure(0, weight=100)

        # sticky='NENNW'
        self.settings_view.grid(row=0, column=0, sticky=tk.NSEW)
        self.main_view.grid(row=0, column=1, sticky=tk.NSEW)

    def configure_theme(self) -> ThemeManager:
        '''
        Creates a theme manager instance that configures the app theme.

        return:
            ThemeManager instance for use by app
        '''

        tm = ThemeManager()
        tm.load_theme(os.path.join(os.curdir, 'res', 'themes', 'default_theme.json'))
        return tm


# View for the configured settings
class SettingsView(ttk.Frame):
    def __init__(self, parent, tm: ThemeManager) -> None:
        '''
        The main settings view. This view displays the currently configured settings

        params:
            parent - Parent widget this view will be attached to.
            tm - The theme manager instance.
        '''
        
        super().__init__(parent)

        self.theme_manager = tm

        self.create_widgets()

    def create_widgets(self):
        # configure layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0, minsize=2)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)


        title_lbl: ttk.Label = ttk.Label(self, background='red', text="0, 0", anchor='center')

        # Create widgets
        label1: ttk.Label = ttk.Label(self, background='red', text="0, 0", anchor='center')
        # label2: ttk.Label = ttk.Label(self, background='green', text="0, 1")
        label3: ttk.Label = ttk.Label(self, background='blue', text="0, 2")

        label4: ttk.Label = ttk.Label(self, background='blue', text="1, 0", anchor='center')
        # label5: ttk.Label = ttk.Label(self, background='red', text="1, 1")
        label6: ttk.Label = ttk.Label(self, background='green', text="1, 2")

        # Position elements
        label1.grid(row=0, column=0, sticky=tk.NSEW)
        # label2.grid(row=0, column=1, sticky=tk.NSEW)
        label3.grid(row=0, column=2, sticky=tk.NSEW)

        label4.grid(row=1, column=0, sticky=tk.NSEW, )
        # label5.grid(row=2, column=1, sticky=tk.NSEW)
        label6.grid(row=3, column=2, sticky=tk.NSEW)

        # Apply theming
        label1.configure(font=self.theme_manager.nf_paragraph_small)
        # label2.configure(font=self.theme_manager.nf_paragraph_normal)
        label3.configure(font=self.theme_manager.nf_paragraph_large)
        # ttk.Label(self, background='yellow').pack(expand=True, fill='x', side='left')
        # ttk.Label(self, background='violet').pack(expand=True, fill='x', side='left')
        # self.grid(row=0, column=0)
        # self.place(x=0, y=0, relwidth=0.3, relheight=1)

        # ttk.Label(self, text="hello", background='cyan').pack(expand=True, fill='x', side='left')
        pass

class MainView(ttk.Frame):
    def __init__(self, parent, tm: ThemeManager) -> None:
        '''
        The main content view. This view displays the main app content

        params:
            parent - Parent widget this view will be attached to
            tm - The theme manager instance
        '''
        super().__init__(parent)
        self.theme_manager = tm
        self.create_widgets()

        # Bind to viewmodel
        self.vm: MainViewModel = MainViewModel()
        self.set_context(self.vm)

    def create_widgets(self):
        self.label1 = ttk.Label(self, background='green')
        self.label1.pack(expand=True, fill='both')

        self.input_box = ttk.Entry(self)
        self.input_box.pack(expand=True, fill="both")
        
    def set_context(self, vm: MainViewModel):
        '''
        Bind to the passed in viewmodel
        '''
        self.label1.configure(textvariable=self.vm.varA)

        self.input_box.bind("<Key>", func=self._input_box_changed)

    def _input_box_changed(self, e):
        self.vm.varA.set(self.input_box.get() + e.char)


    # def labeler(self, e):
    #     print(f"LABELER")
    #     self.label1.config(text=self.input_box.get())
    #     pass