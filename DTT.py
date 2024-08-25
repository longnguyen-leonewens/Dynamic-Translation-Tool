import tkinter as tk
import customtkinter
from tkinter import ttk
from PIL import Image, ImageTk
import os
import accountman
import translatejob
import servicekey
customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 1200
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Title, size, logo
            # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.spawn_x = screen_width//2 - self.width//2
        self.spawn_y = screen_height//2 - self.height//2 -25
        self.title("Dynamic Translation Tool")
        self.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")
        self.resizable(False, False)
        self.iconbitmap("assets/translate.ico")

        # Background image
        self.white_label = customtkinter.CTkLabel(self, text="", fg_color='#701232')
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/assets/yellow3.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)

        # Create default frame
        self.default_frame = customtkinter.CTkFrame(self, fg_color="#BC2C1A", width=400)
        self.default_frame.grid_propagate(False)
        self.default_frame.grid(row=0, column=0, padx=(200,0), sticky="nse")
        # Create login frame
        self.login_frame = customtkinter.CTkFrame(self, fg_color="#BC2C1A", width=400)
        self.login_frame.grid_propagate(False)
        self.login_frame.grid(row=0, column=0, padx=(200,0), sticky="nse")

        # Login label
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Welcome to Dynatrans",
                                                  font=customtkinter.CTkFont(size=28, weight="bold",family="Montserrat"),
                                                  text_color="#D3F3EE")
        self.login_label.grid(row=0, column=0, padx=30,  pady=(50, 50), sticky='w', columnspan=3)

        # Username title
        self.username_title = customtkinter.CTkLabel(self.login_frame, text="Username",
                                                     font=customtkinter.CTkFont(size=14,family="Roboto"),
                                                    text_color="#D3F3EE")
        self.username_title.grid(row=1, column=0, padx=30, sticky ='w', columnspan=3)

        # Username entry
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=300, height=50, border_width=0, corner_radius=10,
                                                     placeholder_text="Enter your username",
                                                     font=customtkinter.CTkFont(size=13,family="Lato"),
                                                     text_color="#7D1538", fg_color='#e9f9f6')
        self.username_entry.grid(row=2, column=0, padx=30, pady=(0, 0), sticky ='we', columnspan=3)

        # Password title
        self.password_title = customtkinter.CTkLabel(self.login_frame, text="Password",
                                                     font=customtkinter.CTkFont(size=14,family="Roboto"),
                                                    text_color="#D3F3EE")
        self.password_title.grid(row=3, column=0, padx=30, pady=(10,0),sticky ='w' ,columnspan=3)

        # Password entry
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=300, height=50, border_width=0, corner_radius=10,
                                                     placeholder_text="Enter your password", show="●",
                                                     font=customtkinter.CTkFont(size=13,family="Lato"),
                                                     text_color="#7D1538", fg_color='#e9f9f6')
        self.password_entry.grid(row=4, column=0, padx=30, pady=(0, 5),sticky='we', columnspan=3)
        self.password_entry.bind("<Return>", self.login_event)

        # Wrong passord
        self.wrong_password = customtkinter.CTkLabel(self.login_frame, text="",
                                                     font=customtkinter.CTkFont(size=12,family="Roboto"),
                                                    text_color="#7D1538")
        self.wrong_password.grid(row=5, column=0, padx=30, pady=(0,0),sticky ='w' ,columnspan=3)
        # Login button
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login",
                                                    command=self.login_event,
                                                    width=200, height=50, corner_radius=10,
                                                    fg_color="#7fb7be",
                                                    font=customtkinter.CTkFont(size=15,family="Lato"), text_color="#D3F3EE", hover_color="#4c6d72")
        self.login_button.grid(row=6, column=0, padx=30, pady=(5, 15), sticky='we', columnspan=3)

        # "or continue with" frame
        self.separator_line_1 = ttk.Separator(self.login_frame, orient='horizontal')
        self.separator_line_1.grid(row=7, column=0,padx=(30,0), sticky='we')

        self.separator_line_2 = ttk.Separator(self.login_frame, orient='horizontal')
        self.separator_line_2.grid(row=7, column=2,padx=(0,30), sticky='we')

        self.separator_line_3 = customtkinter.CTkLabel(self.login_frame, text="or continue with",
                                                     font=customtkinter.CTkFont(size=14,family="Roboto"),
                                                    text_color="#D3F3EE")
        self.separator_line_3.grid(row=7, column=1, padx=(0,0))

        # Google button
        google_icon=customtkinter.CTkImage(Image.open("./assets/googleicon.webp").resize((60,60), Image.ADAPTIVE))
        self.google_button= customtkinter.CTkButton(self.login_frame, image=google_icon,
                                                    text="Google",
                                                    width=50, height=20,
                                                    font=customtkinter.CTkFont(size=12,family="Roboto"),
                                                    fg_color='#D3F3EE',hover_color='#AFAFAF', text_color='#7d1538')
        self.google_button.grid(row=8, column=1, pady=15)

        # create main frame
        self.main_frame = customtkinter.CTkFrame(self, fg_color="#BC2C1A", width=400)
        self.main_frame.grid_propagate(False)

        # Create hello
        self.hello_label = customtkinter.CTkLabel(self.main_frame, text="Hello,",
                                                  font=customtkinter.CTkFont(size=28, weight="bold",family="Montserrat"),
                                                  text_color="#D3F3EE")
        self.hello_label.grid(row=0, column=0, padx=30,  pady=(50,0), sticky='w')

        self.name_label = customtkinter.CTkLabel(self.main_frame, text="Anonymous",
                                                  font=customtkinter.CTkFont(size=28, weight="bold",family="Montserrat"),
                                                  text_color="#D3F3EE")
        self.name_label.grid(row=1, column=0, padx=30,  pady=(0,25), sticky='w')

        # Create choose function
        self.choose_label = customtkinter.CTkLabel(self.main_frame, text="Select Functionality",
                                                  font=customtkinter.CTkFont(size=20, weight="bold",family="Lato"),
                                                  text_color="#D3F3EE")
        self.choose_label.grid(row=2, column=0, padx=30,  pady=(25,10), sticky='w')

        # Functionality
        self.onscreen_button = customtkinter.CTkButton(self.main_frame, text="On-screen Translator",
                                                    command=self.onscreen_choose,
                                                    width=200, height=50, corner_radius=10,
                                                    fg_color="#659298",
                                                    font=customtkinter.CTkFont(size=15,family="Roboto"), text_color="#D3F3EE", hover_color="#4b0c21")
        self.onscreen_button.grid(row=3, column=0, padx=30, pady=(5, 15), sticky='we',)

        self.document_button = customtkinter.CTkButton(self.main_frame, text="Document Translate (W.I.P)",
                                                    command=self.document_choose,
                                                    width=200, height=50, corner_radius=10,
                                                    fg_color="#659298",
                                                    font=customtkinter.CTkFont(size=15,family="Roboto"), text_color="#D3F3EE", hover_color="#4b0c21")
        self.document_button.grid(row=4, column=0, padx=30, pady=(5, 15), sticky='we',)

        # Back
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.back_button = customtkinter.CTkButton(self.main_frame, text="Logout", command=self.back_event, width=200,
                                                   fg_color="#7d1538", hover_color="#4b0c21")
        self.back_button.grid(row=5, column=0, padx=30, pady=(180, 15))

        # OST frame
        self.ost_frame = customtkinter.CTkFrame(self, fg_color="#7d1538", width=400, height=400, corner_radius=20, bg_color='#701232', border_color="#701232")

        # Dropdown list
        self.lang_list = translatejob.get_language_list()
        self.ost_from_lang_choose = customtkinter.CTkOptionMenu(self.ost_frame, dynamic_resizing=False,
                                                                width=60,
                                                                values=self.lang_list,
                                                                fg_color="#7fb7be", button_color="#7fb7be", button_hover_color="#4c6d72",text_color="#2C443E",
                                                                dropdown_fg_color="#D3F3EE", dropdown_hover_color="#697977", dropdown_text_color="#2C443E",
                                                                font=customtkinter.CTkFont(size=12,family="Roboto"),
                                                                dropdown_font=customtkinter.CTkFont(size=12,family="Roboto"))
        self.ost_from_lang_label = customtkinter.CTkLabel(self.ost_frame, text="From",
                                                        font=customtkinter.CTkFont(size=14, weight="normal",family="Lato"),
                                                        text_color="#D3F3EE")
        self.ost_from_lang_choose.grid(row=0, column=1, pady=(30,0),padx=(5,20), sticky='w')
        self.ost_from_lang_label.grid(row=0, column=0, pady=(30,0), padx=(20,0), sticky='w')

        self.ost_to_lang_choose = customtkinter.CTkOptionMenu(self.ost_frame, dynamic_resizing=False,
                                                                values=self.lang_list,
                                                                width=60,
                                                                fg_color="#7fb7be", button_color="#7fb7be", button_hover_color="#4c6d72",text_color="#2C443E",
                                                                dropdown_fg_color="#D3F3EE", dropdown_hover_color="#697977", dropdown_text_color="#2C443E",
                                                                font=customtkinter.CTkFont(size=12,family="Roboto"),
                                                                dropdown_font=customtkinter.CTkFont(size=12,family="Roboto"))
        self.ost_to_lang_label = customtkinter.CTkLabel(self.ost_frame, text="To",
                                                        font=customtkinter.CTkFont(size=14, weight="normal",family="Lato"),
                                                        text_color="#D3F3EE")
        self.ost_to_lang_choose.grid(row=1, column=1, pady=(15,0), padx=(5,20), sticky='w')
        self.ost_to_lang_label.grid(row=1, column=0, pady=(15,0), padx=(20,0), sticky='w')

        # Calibrate
        self.calib_label = customtkinter.CTkLabel(self.ost_frame, text="Calibrate",
                                                        font=customtkinter.CTkFont(size=14, weight="normal",family="Lato"),
                                                        text_color="#D3F3EE")
        self.calib_label.grid(row=2, column=0, pady=(10,0), padx=(20,0), sticky='w')

        self.up_button_img=customtkinter.CTkImage(Image.open("./assets/up_arrow.png").resize((60,60), Image.ADAPTIVE))
        self.up_button_disabled_img=customtkinter.CTkImage(Image.open("./assets/up_arrow_disabled.png").resize((60,60), Image.ADAPTIVE))
        self.up_button= customtkinter.CTkButton(self.ost_frame, image=self.up_button_disabled_img, command=self.ost_calib_up_event,
                                                    text="",
                                                    width=15,height=15,
                                                    font=customtkinter.CTkFont(size=12,family="Roboto"),
                                                    fg_color='#7d1538',hover_color='#7d1538')
        self.up_button.grid(row=2, column=1, pady=(10,0), padx=(20,20),sticky= 'w')

        self.down_button_img=customtkinter.CTkImage(Image.open("./assets/down_arrow.png").resize((60,60), Image.ADAPTIVE))
        self.down_button_disabled_img=customtkinter.CTkImage(Image.open("./assets/down_arrow_disabled.png").resize((60,60), Image.ADAPTIVE))
        self.down_button= customtkinter.CTkButton(self.ost_frame, image=self.down_button_disabled_img, command=self.ost_calib_down_event,
                                                    text="",
                                                    width=15,height=15,
                                                    font=customtkinter.CTkFont(size=12,family="Roboto"),
                                                    fg_color='#7d1538',hover_color='#7d1538')
        self.down_button.grid(row=3, column=1, pady=0, padx=20,sticky= 'w')
        # Delete button
        self.ost_delete_button = customtkinter.CTkButton(self.ost_frame, text="Delete", command=self.ost_delete_event,
                                                         width=100,
                                                   fg_color="#7fb7be", hover_color="#4c6d72", text_color="#BC2C1A")
        self.ost_delete_button.grid(row=3, column=0, padx=(20,0), pady=0, sticky='w')
        # Scrolling lock button
        self.scrolllock = True
        self.ost_scroll_button = customtkinter.CTkButton(self.ost_frame, text="Scrolling", command=self.ost_scrolling_event,
                                                         width=100,
                                                   fg_color="#7fb7be", hover_color="#7fb7be", text_color="#4A2B5D")
        self.ost_scroll_button.grid(row=4, column=0, padx=(20,0), pady=10, sticky='w')
        # OST back button
        self.ost_back_button = customtkinter.CTkButton(self.ost_frame, text="Back", command=self.ost_back_event,
                                                   fg_color="#dacc3e", hover_color="#988e2b", text_color="#BC2C1A")
        self.ost_back_button.grid(row=5, column=0, padx=20, pady=(20,0), sticky='we', columnspan=2)

        # OST collapse button
        self.collapse_img = customtkinter.CTkImage(Image.open("./assets/collapse.png").resize((60,60), Image.ADAPTIVE))
        self.ost_collapse_button = customtkinter.CTkButton(self.ost_frame, text="", command=self.ost_collapse_event,
                                                           image=self.collapse_img, width=15, height= 15,
                                                           fg_color="#7d1538", hover=False)
        self.ost_collapse_button.grid(row=6, column=0, padx=0, pady=(10,5), sticky='n', columnspan=2)

        # OST expand button
        self.expand_img = customtkinter.CTkImage(Image.open("./assets/expand.png").resize((60,60), Image.ADAPTIVE))
        self.ost_expand_button = customtkinter.CTkButton(self.ost_frame, text="", command=self.ost_expand_event,
                                                           image=self.expand_img,
                                                           width=15, height= 15, corner_radius=30,
                                                           fg_color="#bc2c1a", hover=False)
        # Frame dragging
        self.start_x = [0,0]
        self.start_y = [0,0]
        self.ost_frame.bind("<Button-1>", self.start_drag)  # Left mouse button press to start dragging
        self.ost_frame.bind("<B1-Motion>", self.on_drag)

    def login_event(self, *args):
        authen = accountman.check_accounts(self.username_entry.get(), self.password_entry.get())
        authen = True
        if authen is True:
            self.login_frame.grid_forget()  # remove login frame
            self.main_frame.grid(row=0, column=0, sticky="nse")  # show main frame
            self.main_frame.grid_propagate(False)
        else:
            self.wrong_password.configure(text="Incorrect username or password")

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid_propagate(False)
        self.login_frame.grid(row=0, column=0, sticky="nse")  # show login frame

    def ost_back_event(self):
        # Revert attributes
        self.state('normal')
        self.attributes('-transparentcolor', '')
        self.attributes('-topmost', False)
        self.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")
        self.overrideredirect('False')
        # Show main frame
        self.white_label.grid_forget()
        self.bg_image_label.grid(row=0, column=0)
        self.ost_frame.grid_forget()
        self.main_frame.grid(row=0, column=0, sticky="nse")  # show main frame
        self.main_frame.grid_propagate(False)
        self.default_frame.grid(row=0, column=0, padx=(200,0), sticky="nse")

    def ost_delete_event(self):
        None

    def ost_scrolling_event(self):
        if (self.scrolllock == True):
            self.ost_scroll_button.configure(fg_color="#3f5b5f", hover_color="#3f5b5f", text_color="#D3F3EE")
            self.up_button.configure(image=self.up_button_img, hover_color='#4c6d72')
            self.down_button.configure(image=self.down_button_img, hover_color='#4c6d72')
            self.scrolllock = False
        else:
            self.ost_scroll_button.configure(fg_color="#7fb7be", hover_color="#7fb7be", text_color="#4A2B5D")
            self.up_button.configure(image=self.up_button_disabled_img, hover_color='#7d1538')
            self.down_button.configure(image=self.down_button_disabled_img, hover_color='#7d1538')
            self.scrolllock = True

    def ost_calib_up_event(self):
        None

    def ost_calib_down_event(self):
        None

    def ost_collapse_event(self):
        self.ost_from_lang_label.grid_forget()
        self.ost_from_lang_choose.grid_forget()
        self.ost_to_lang_choose.grid_forget()
        self.ost_to_lang_label.grid_forget()
        self.calib_label.grid_forget()
        self.up_button.grid_forget()
        self.down_button.grid_forget()
        self.ost_delete_button.grid_forget()
        self.ost_scroll_button.grid_forget()
        self.ost_back_button.grid_forget()
        self.ost_collapse_button.grid_forget()
        self.ost_frame.configure(fg_color='#701232')
        self.ost_expand_button.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')

    def ost_expand_event(self):
        self.ost_frame.configure(fg_color='#7d1538')
        self.ost_expand_button.grid_forget()
        self.ost_from_lang_choose.grid(row=0, column=1, pady=(30,0),padx=(5,20), sticky='w')
        self.ost_from_lang_label.grid(row=0, column=0, pady=(30,0), padx=(20,0), sticky='w')
        self.ost_to_lang_choose.grid(row=1, column=1, pady=(15,0), padx=(5,20), sticky='w')
        self.ost_to_lang_label.grid(row=1, column=0, pady=(15,0), padx=(20,0), sticky='w')
        self.calib_label.grid(row=2, column=0, pady=(10,0), padx=(20,0), sticky='w')
        self.up_button.grid(row=2, column=1, pady=(10,0), padx=(20,20),sticky= 'w')
        self.down_button.grid(row=3, column=1, pady=0, padx=20,sticky= 'w')
        self.ost_delete_button.grid(row=3, column=0, padx=(20,0), pady=0, sticky='w')
        self.ost_scroll_button.grid(row=4, column=0, padx=(20,0), pady=10, sticky='w')
        self.ost_back_button.grid(row=5, column=0, padx=20, pady=(20,0), sticky='we', columnspan=2)
        self.ost_collapse_button.grid(row=6, column=0, padx=0, pady=(10,5), sticky='n', columnspan=2)

    def start_drag(self, event):
        self.start_x = [event.x, self.ost_frame.grid_info().get('padx', 0)]
        self.start_y = [event.y, self.ost_frame.grid_info().get('pady', 0)]
        print("Start",event.x,event.y, self.start_x[1], self.start_y[1])

    def on_drag(self, event):
        """Move the frame by adjusting padx and pady based on mouse movement."""
        print(event.x,event.y)
        delta_x = self.start_x[0] - event.x
        delta_y = event.y - self.start_y[0]
        # Get current padx and pady
        newpadx = self.start_x[1] + delta_x
        if (newpadx < 0):
            newpadx = 0
        newpady = self.start_y[1] + delta_y
        if (newpady < 0):
            newpady = 0
        print("newposs", event.x, event.y)
        print("newpad", newpadx,newpady)
        self.ost_frame.grid_configure(padx=newpadx, pady=newpady)

    def onscreen_choose(self):
        # Remove main frames
        self.main_frame.grid_forget()  # remove main frame
        self.default_frame.grid_forget()
        self.bg_image_label.grid_forget()
        # Zoom and on top
        self.state('zoomed')
        self.attributes('-topmost', True)
        self.overrideredirect('True')
        # Configure see through
        self.white_label.configure(width=self.winfo_width(), height=self.winfo_height())
        self.white_label.grid(row=0, column=0)
        self.attributes('-transparentcolor', '#701232')
        # Show frames
        self.ost_frame.grid(row=0, column=0, padx=40, pady=100,sticky="ne")

    def document_choose(self):
        None


if __name__ == "__main__":
    app = App()
    app.mainloop()
