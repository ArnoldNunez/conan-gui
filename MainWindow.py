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
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)
        self.rowconfigure(6, weight=0)

        max_rows = 4
        max_cols = 3

        # Create widgets
        title_lbl: ttk.Label = ttk.Label(self, background='red', text="Current Settings", anchor='center')

        work_dir_lbl: ttk.Label = ttk.Label(self, background='green', text="Working Directory:")
        work_dir_val: ttk.Label = ttk.Label(self, background='green', text="N/A")
        
        title_conan_lbl: ttk.Label = ttk.Label(self, background='red', text="Conan Settings", anchor='center')

        build_profile_lbl: ttk.Label = ttk.Label(self, background='green', text="Build Profile:",)
        build_profile_val: ttk.Label = ttk.Label(self, background='green', text="N/A")

        host_profile_lbl: ttk.Label = ttk.Label(self, background='green', text="Host Profile")
        host_profile_val: ttk.Label = ttk.Label(self, background='green', text="N/A")

        conan_pkg_lbl: ttk.Label = ttk.Label(self, background='green', text="Top Level Conan Package")
        conan_pkg_val: ttk.Label = ttk.Label(self, background='green', text="N/A")

        # Position elements
        title_lbl.grid(row=0, column=0, columnspan=max_cols, sticky=tk.NSEW)

        work_dir_lbl.grid(row=1, column=0, columnspan=max_cols, sticky=tk.NSEW)
        work_dir_val.grid(row=2, column=0, columnspan=max_cols, sticky=tk.NSEW)

        title_conan_lbl.grid(row=3, column=0, columnspan=max_cols, sticky=tk.NSEW)

        build_profile_lbl.grid(row=4, column=0, columnspan=max_cols, sticky=tk.NSEW)
        build_profile_val.grid(row=5, column=0, columnspan=max_cols, sticky=tk.NSEW)

        host_profile_lbl.grid(row=6, column=0, columnspan=max_cols, sticky=tk.NSEW)
        host_profile_val.grid(row=7, column=0, columnspan=max_cols, sticky=tk.NSEW)

        conan_pkg_lbl.grid(row=8, column=0, columnspan=max_cols, sticky=tk.NSEW)
        conan_pkg_val.grid(row=9, column=0, columnspan=max_cols, sticky=tk.NSEW)



        # Apply theming
        # TODO

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