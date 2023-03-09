import tkinter

import customtkinter
import os
from PIL import Image

import sqlite3

connection = sqlite3.connect("LH_Database.db")
cursor = connection.cursor()

from CreateCustomer import add_customer_function
from CreateCustomer import get_all_customers

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        width = 1000
        height = 650

        self.screen_width = self.winfo_screenwidth()  # Width of the screen
        self.screen_height = self.winfo_screenheight() # Height of the screen
        
        # Calculate Starting X and Y coordinates for Window
        x = (self.screen_width/2) - (width/2)
        y = (self.screen_height/2) - (height/2)

        self.title("LH Loan Management")
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

        customtkinter.set_appearance_mode("dark")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets/")
        self.navigation_background_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Images/navigation_background.jpg")))
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Icons/LH_logo.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Images/large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Images/image_icon_light.png")), size=(20, 20))
        self.dashboard_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Icons/dashboard_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "Icons/dashboard_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Images/chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "Images/chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Images/add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "Images/add_user_light.png")), size=(20, 20))




        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)


        
        # load and create background image
   

        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/Assets/Images/navigation_background.jpg"), size=(100,400))
        self.bg_image_label = customtkinter.CTkLabel(self.navigation_frame, image=self.bg_image)


        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  LH", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.dashboard_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Dashboard",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.dashboard_image, anchor="w", command=self.dashboard_button_event)
        self.dashboard_button.grid(row=1, column=0, sticky="ew")

        self.customers_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Customers",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.customers_button_event)
        self.customers_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.add_new_customer_button = customtkinter.CTkButton(self.navigation_frame, text="Add New Customer", image=self.image_icon_image, command=self.create_new_customer_toplevel)
        self.add_new_customer_button.grid(row=5, column=0, padx=20, pady=20,sticky="s")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")



        # create dashboard frame
        self.dashboard_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="lightgrey")
        self.dashboard_frame.grid_columnconfigure(0, weight=1)
        
        # self.dashboard_frame_large_image_label = customtkinter.CTkLabel(self.dashboard_frame, text="", image=self.large_test_image)
        # self.dashboard_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # self.dashboard_frame_button_1 = customtkinter.CTkButton(self.dashboard_frame, text="", image=self.image_icon_image)
        # self.dashboard_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.dashboard_frame_button_2 = customtkinter.CTkButton(self.dashboard_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        # self.dashboard_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.dashboard_frame_button_3 = customtkinter.CTkButton(self.dashboard_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        # self.dashboard_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        # self.dashboard_frame_button_4 = customtkinter.CTkButton(self.dashboard_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        # self.dashboard_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        self.active_customer_frame = customtkinter.CTkFrame(self.dashboard_frame, fg_color="white")
        self.active_customer_frame.grid(row=0, column=0, sticky="ew",padx=10, pady=10)

        self.finished_customer_frame = customtkinter.CTkFrame(self.dashboard_frame, fg_color="white")
        self.finished_customer_frame.grid(row=0, column=1, sticky="ew",padx=10, pady=10)

        self.add_new_customer_frame = customtkinter.CTkFrame(self.dashboard_frame, fg_color="white")
        self.add_new_customer_frame.grid(row=0, column=2, sticky="ew",padx=10, pady=10)

        self.transaction_history_frame = customtkinter.CTkFrame(self.dashboard_frame, fg_color="white")
        self.transaction_history_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        self.longest_unpaid_frame = customtkinter.CTkFrame(self.dashboard_frame, fg_color="white")
        self.longest_unpaid_frame.grid(row=1, column=1, sticky="ew", padx=10, pady=10)











        # create customers frame
        self.customers_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        get_customers = get_all_customers()

        for customer in get_customers:
            i = 0
            customer_button = "customers_frame_button_" + str(i)
            self.customer_button = customtkinter.CTkButton(self.customers_frame, text=customer[1])
            # self.customer_button.grid(row=i, column=0, padx=20, pady=10)
            self.customer_button.pack(padx=20, pady=10)

            i = i + 1
 










        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("dashboard")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.dashboard_button.configure(fg_color=("gray75", "gray25") if name == "dashboard" else "transparent")
        self.customers_button.configure(fg_color=("gray75", "gray25") if name == "customers" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "dashboard":
            self.dashboard_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.dashboard_frame.grid_forget()
        if name == "customers":
            self.customers_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.customers_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def dashboard_button_event(self):
        self.select_frame_by_name("dashboard")

    def customers_button_event(self):
        self.select_frame_by_name("customers")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def create_new_customer_toplevel(self):

        width = 500
        height = 400

        # Calculate Starting X and Y coordinates for Window
        x = (self.screen_width/2) - (width/2)
        y = (self.screen_height/2) - (height/2)

        window = customtkinter.CTkToplevel(self)
        window.title("Create New Customer")
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))

        #labels
        customerNameLabel = customtkinter.CTkLabel(window, text="Customer Name:")
        customerNameLabel.grid(row=0, column=0, sticky = "W", pady = 2)

        plateNoLabel = customtkinter.CTkLabel(window, text="Plate No:")
        plateNoLabel.grid(row=1, column=0, sticky = "W", pady = 2)

        depositLabel = customtkinter.CTkLabel(window, text="Deposit:")
        depositLabel.grid(row=2, column=0, sticky = "W", pady = 2)

        loanTermLabel = customtkinter.CTkLabel(window, text="Loan Term:")
        loanTermLabel.grid(row=3, column=0, sticky = "W", pady = 2)          
        
        monthlyLabel = customtkinter.CTkLabel(window, text="Monthly:")
        monthlyLabel.grid(row=4, column=0, sticky = "W", pady = 2)

        vehicleModelLabel = customtkinter.CTkLabel(window, text="Vehicle Model:")
        vehicleModelLabel.grid(row=5, column=0, sticky= "W", pady = 2)

        vehicleEngineNoLabel = customtkinter.CTkLabel(window, text="Engine No:")
        vehicleEngineNoLabel.grid(row=6, column=0, sticky="W", pady = 2)

        bookNoLabel = customtkinter.CTkLabel(window, text="Book No:")
        bookNoLabel.grid(row=7, column=0, sticky="W", pady=2)

        positionInBookLabel = customtkinter.CTkLabel(window, text="Position In Book:")
        positionInBookLabel.grid(row=8, column=0, sticky = "W", pady =2 )


        # entries

        customerNameEntry = customtkinter.CTkEntry(window, placeholder_text="")
        customerNameEntry.grid(row=0, column=1, sticky = "W", pady = 2)

        plateNoEntry = customtkinter.CTkEntry(window, placeholder_text="")
        plateNoEntry.grid(row=1, column=1, sticky = "W", pady = 2)

        depositEntry = customtkinter.CTkEntry(window, placeholder_text="")
        depositEntry.grid(row=2, column=1, sticky = "W", pady = 2)

        loanTermEntry = customtkinter.CTkEntry(window, placeholder_text="")
        loanTermEntry.grid(row=3, column=1, sticky = "W", pady = 2)          
        
        monthlyEntry = customtkinter.CTkEntry(window, placeholder_text="")
        monthlyEntry.grid(row=4, column=1, sticky = "W", pady = 2)

        vehicleModelEntry = customtkinter.CTkEntry(window, placeholder_text="")
        vehicleModelEntry.grid(row=5, column=1, sticky= "W", pady = 2)

        vehicleEngineNoEntry = customtkinter.CTkEntry(window, placeholder_text="")
        vehicleEngineNoEntry.grid(row=6, column=1, sticky="W", pady = 2)

        bookNoEntry = customtkinter.CTkEntry(window, placeholder_text="")
        bookNoEntry.grid(row=7, column=1, sticky="W", pady=2)

        positionInBookEntry = customtkinter.CTkEntry(window, placeholder_text="")
        positionInBookEntry.grid(row=8, column=1, sticky = "W", pady =2 )

        # # create label on CTkToplevel window
        # label = customtkinter.CTkLabel(window, text="CTkToplevel window")
        # label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

        submitCustomerButton = customtkinter.CTkButton(window, text="Submit", command=lambda: self.create_new_customer(customerNameEntry.get(), plateNoEntry.get(), depositEntry.get(), loanTermEntry.get(), monthlyEntry.get(), vehicleModelEntry.get(), vehicleEngineNoEntry.get(), bookNoEntry.get(), positionInBookEntry.get()))
        submitCustomerButton.grid(row=10)


    def create_new_customer(self, name, plate, deposit, loanterm, monthly, vehicle, engineno, bookno, bookindex):
        # print("Customer Name: ", customerName)
        # print("Plate No ", plateNo)
        # print("Deposit: RM", deposit)
        # print("Loan Term: ", loanTerm, " Months")
        # print("Monthly: RM", monthly)
        # print("Vehicle Model: ", vehicleModel)
        # print("Vehicle Engine No: ", vehicleEngineNo)
        # print("Book No: ", bookNo)
        # print("Position In Book", positionInBook)
        add_customer_function(name, plate, deposit, loanterm, monthly, vehicle, engineno, bookno, bookindex)




       


if __name__ == "__main__":
    app = App()
    app.mainloop()

