import tkinter
import customtkinter
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- SEARCH PASSWORD ------------------------------- #

    
    


def search_pw():
    search_website = search_ws_name.get()
    try:
        with open("Password.json", "r") as file:
            global data
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
        # filenotfound()

    else:

        if search_website in list(data):
            # deatails()     add pyperclip as well to copy the pw to clipboard

            pw_found(w=search_website,e=f"{data[search_website]['email']}",p=f"{data[search_website]['password']}")
        
        else:
            messagebox.showinfo(title=f"{search_website}", message=f"{search_website} Email and Password is not saved here.")

            
            # no_deatils()


def all_pw():
    try:
        with open("Password.json", "r") as file:
            global data
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        r_grid = 3
        for w in list(data):
            e = data[w]['email']
            p = data[w]['password']
            customtkinter.CTkLabel(master=search_pw_tab, justify=tkinter.CENTER, text=f"{w}").grid(row=r_grid,column=0,pady=5) 
            customtkinter.CTkLabel(master=search_pw_tab, justify=tkinter.CENTER, text= f"{e}").grid(row=r_grid,column=1,pady=5) 
            customtkinter.CTkLabel(master=search_pw_tab, justify=tkinter.CENTER, text= f"{p}").grid(row=r_grid,column=2,pady=5)
            r_grid+=1
        


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def pw_gen():
    entry_pw.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password_gen = "".join(password_list)
    entry_pw.insert(0, password_gen)
    pyperclip.copy(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    website = entry_ws.get()
    email = entry_email.get()
    password = entry_pw.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Password Manager", message="One or more entity is empty!")
    else:
        try:
            with open("Password.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("Password.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("Password.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            entry_ws.delete(0, tkinter.END)
            entry_pw.delete(0, tkinter.END)
            entry_email.delete(0, tkinter.END)
            entry_ws.focus()


# ---------------------------- UI SETUP ------------------------------- #

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("850x750")
app.title("PASSWORD MANAGER")

def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


frame_0 = customtkinter.CTkFrame(master=app,corner_radius=30)
frame_0.pack(pady=20, padx=60, fill="both", expand=False)

label_0 = customtkinter.CTkLabel(master=frame_0, justify=tkinter.CENTER, text="PASSWORD\nMANAGER", font=customtkinter.CTkFont(size=30,weight='bold'))
label_0.pack(pady=10, padx=10)

main_frame = customtkinter.CTkFrame(master=app,corner_radius=30)
main_frame.pack(pady=20, padx=40, fill="both", expand=False)

#Adding tabs --->
tabview = customtkinter.CTkTabview(main_frame,width=600,corner_radius=20)
tabview.pack(padx=5, pady=20)
add_pw_tab = tabview.add("Add Password")
search_pw_tab = tabview.add("Search Password")
tabview.set("Add Password")


#add_pw_tab -->

# Labels -->
label_ws = customtkinter.CTkLabel(master=add_pw_tab, justify=tkinter.LEFT, text="Website:")
label_ws.grid(row=0,column=0)

label_ws = customtkinter.CTkLabel(master=add_pw_tab, justify=tkinter.LEFT, text="Email/Username:")
label_ws.grid(row=1,column=0)

label_ws = customtkinter.CTkLabel(master=add_pw_tab, justify=tkinter.LEFT, text="Password:")
label_ws.grid(row=2,column=0)


entry_ws = customtkinter.CTkEntry(master=add_pw_tab, placeholder_text="Enter Website Name", width=250, justify=tkinter.CENTER,corner_radius=20)
entry_ws.grid(row=0,column=1,pady=10, padx=10)

entry_email = customtkinter.CTkEntry(master=add_pw_tab, placeholder_text="Enter your email", width=250, justify=tkinter.CENTER,corner_radius=20)
entry_email.grid(row=1,column=1,pady=10, padx=10)

entry_pw = customtkinter.CTkEntry(master=add_pw_tab, placeholder_text="Enter your Password", width=250, justify=tkinter.CENTER,corner_radius=20)
entry_pw.grid(row=2,column=1,pady=10, padx=10)

generate_pw_btn= customtkinter.CTkButton(master=add_pw_tab,text="Generate Password", command=pw_gen)
generate_pw_btn.grid(row=3,column=0,pady=10, padx=10)

save_pw_btn= customtkinter.CTkButton(master=add_pw_tab,text="Save Password", command=save_pass)
save_pw_btn.grid(row=3,column=2,pady=10, padx=10)


fotter_frame = customtkinter.CTkFrame(master=app,corner_radius=30)
fotter_frame.pack(pady=20, padx=40, fill="both", expand=False)

appearance_mode_label = customtkinter.CTkLabel(fotter_frame, text="Appearance Mode:", anchor="w").grid(row=0,column=0,padx=20, pady=(10, 0))

appearance_mode_optionemenu = customtkinter.CTkOptionMenu(fotter_frame, values=["System", "Dark", "Light"],command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(row=1,column=0,padx=20, pady=(10, 10))
appearance_mode_optionemenu.set("System")

scaling_label = customtkinter.CTkLabel(fotter_frame, text="UI Scaling:", anchor="w")
scaling_label.grid(row=0, column=1, padx=20, pady=(10, 0))
scaling_optionemenu = customtkinter.CTkOptionMenu(fotter_frame, values=["80%", "90%", "100%", "110%", "120%"], command=change_scaling_event)
scaling_optionemenu.set("100%")
scaling_optionemenu.grid(row=1, column=1, padx=20, pady=(10, 20))

#search_pw_tab -->
search_ws_name = customtkinter.CTkEntry(master=search_pw_tab, placeholder_text="Enter Website Name", width=300, justify=tkinter.CENTER,corner_radius=20)
search_ws_name.grid(row=0,column=1,pady=5, padx=5)

search_pw_btn= customtkinter.CTkButton(master=search_pw_tab,text="Search Password", command=search_pw,corner_radius=10)
search_pw_btn.grid(row=0,column=2,pady=5, padx=5)

all_pw_pw_btn= customtkinter.CTkButton(master=search_pw_tab,text="Show all Password", command=all_pw,corner_radius=10).grid(row=1,column=1,pady=5, padx=5)

label_ws_all = customtkinter.CTkLabel(master=search_pw_tab, justify=tkinter.CENTER, text="Website").grid(row=2,column=0,pady=10, padx=50)

label_email_all = customtkinter.CTkLabel(master=search_pw_tab, justify=tkinter.CENTER, text="Email/Username").grid(row=2,column=1,pady=10, padx=50)

label_pw_all = customtkinter.CTkLabel(master=search_pw_tab, justify=tkinter.CENTER, text="Passowrd").grid(row=2,column=2,pady=10, padx=50)



def pw_found(w,e,p):
            customtkinter.CTkLabel(master=search_pw_tab, justify=tkinter.CENTER, text=w).grid(row=3,column=0,pady=5) 
            customtkinter.CTkLabel(master=search_pw_tab, justify=tkinter.CENTER, text= e).grid(row=3,column=1,pady=5) 
            customtkinter.CTkLabel(master=search_pw_tab, justify=tkinter.CENTER, text= p).grid(row=3,column=2,pady=5)

 


app.mainloop()





