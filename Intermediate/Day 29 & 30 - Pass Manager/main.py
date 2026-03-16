from tkinter import messagebox,Label,Entry,PhotoImage,Canvas,Tk,END
from tkmacosx import Button
import random, string, json, os

window = Tk()
window.title("Password Manager")
window.minsize(width=500,height=400)
window.config(padx=20,pady=20,bg="black")
app_logo = PhotoImage(file="./logo.png") #200x189
canvas = Canvas(bg='black',highlightthickness=0)
canvas.create_image(84,105,image=app_logo)
canvas.grid(column=3,rowspan=1)
 
def generate_password():
    print("Generated Password")
    acceptable_punctuations = ['!','@','#','$','%','^','&','*','(',')']
    num_of_alphabets = 4
    num_of_symbols = 2

    alphabets = string.ascii_lowercase + string.ascii_uppercase
    punctuation = string.punctuation

    clean_punctuation = ""
    clean_punctuation = [symbol for symbol in punctuation if symbol in acceptable_punctuations]
    random_alphabets = random.sample(alphabets,num_of_alphabets)
    random_punctuation = random.sample(clean_punctuation,num_of_symbols)
    password_list = random_alphabets + random_punctuation
    final_password = "".join(password_list)
    print(final_password)

    password_entry.delete(0,END)
    password_entry.insert(0,final_password)
    password_entry.clipboard_clear()
    password_entry.clipboard_append(final_password)

def save_details():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    if password != "" and email != "":
        if website == "":
            website = None

        string_data = {
            website : [
            {
            "email" : email,
            "password" : password
            }
        ]
        }
    else:
        messagebox.showerror(message="Password or Email is invalid or Empty!")
        return

    confirm_write = messagebox.askquestion(message="Would you like to save your data?")
    if confirm_write == 'yes':
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        try :
            with open('./password.json',mode="r") as json_file:
                json_data = json.load(json_file)
        except FileNotFoundError as e:
            with open('./password.json',mode="w") as json_file:
                print(f"{e}, fixing..")
                print("new JSON File has been created..")
                json.dump(string_data,json_file,indent=4)
            print(f"Fixed and data updated..")
        except json.decoder.JSONDecodeError as e:
            print(f"{e}, fixing..")
            with open('./password.json',mode="w") as json_file:
                json_data = json.dump(string_data,json_file,indent=4)
            print(f"Fixed and data updated..")
        else:
            with open('./password.json',mode="w") as json_file:
                json_data.update(string_data)
                json.dump(json_data,json_file,indent=4)
            print("Data updated with zero errors..")
    else:
        return
    
def search_entry():
    try :
        with open("password.json","r") as json_file:
            website = website_entry.get().lower()
            json_data = json.load(json_file)
            website_entry.clipboard_clear()
            website_entry.clipboard_append(json_data[website][0]['password'])
            messagebox.showinfo(title=website,message=f"Email : {json_data[website][0]['email']}\nPassword : {json_data[website][0]['password']}")
    except FileNotFoundError as e:
        messagebox.showerror(title=website,message=f"File doesn't exist!")
    except KeyError as e:
        messagebox.showerror(title=website,message=f"Website : {e}, does not exist!")
    except json.decoder.JSONDecodeError as e:
        messagebox.showerror(title=website,message=f"File empty, Add a new record before searching..")
        
#------------------Entry-------------------#

website_entry = Entry(width=22,bg="black")
website_entry.grid(column=3,row=5,sticky="w")

email_entry = Entry(width=40,bg="black")
email_entry.insert(0,string="sahil@gmail.com")
email_entry.grid(column=3,row=7)

password_entry = Entry(width=22,bg="black")
password_entry.grid(column=3,row=8,sticky="w")

#------------------Label-------------------#

website_label = Label(text="Website :",bg="black")
website_label.grid(columnspan=1,row=5,sticky="w")

email_label = Label(text="Email/Username :",bg="black")
email_label.grid(columnspan=1,row=7,sticky="w")

password_label = Label(text="Password :",bg="black")
password_label.grid(columnspan=1,row=8,sticky="w")

#-------------------Buttons-------------------#

generate_button = Button(text="Generate Password",command=generate_password,highlightbackground="black",bg="white")
generate_button.grid(column=3,row=8,sticky="e")

add_button = Button(text="Add",command=save_details,width=30,highlightbackground="black",bg="white")
add_button.grid(column=3,row=10,sticky="ew")

search_button = Button(text="Search",command=search_entry,highlightbackground="black",bg="white",width=160)
search_button.grid(column=3,row=5,sticky="e")
 
window.mainloop()