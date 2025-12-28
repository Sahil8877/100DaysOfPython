import tkinter as tk

window = tk.Tk()
window.title("Miles to KM converter")
window.minsize(width=300,height=290)

def button_click():
    '''
    when button click event occurs, the str from input box is fetched
    we check if the string is valid floting number 
    convert the miles to km and return the result, and 
    insert the km into its label
    ''' 
    input_string = miles_textbox.get()
    try:
        if float(input_string):
            result_in_km = float(input_string) * 1.609
            miles_to_km_label.config(text=f"{result_in_km:.2f} Km")
    except ValueError:
        miles_to_km_label.config(text="Invalid Input!")

def delete_temp_text(self):
    #deletes initial text in the entry widget
    miles_textbox.delete(0,"end")

#labels
title_label = tk.Label(text="Miles To KiloMeter Converter",font=("helvtica",20,"bold","italic"))
title_label.pack(side="top",pady=30)
miles_label = tk.Label(text="Miles :",font=(None,15))
miles_label.place(x=10,y=100)
km_label = tk.Label(text="KM :",font=(None,15))
km_label.place(x=10,y=150)
miles_to_km_label = tk.Label(text=f"0",font=(None,15))
miles_to_km_label.place(x=100,y=150)

#Entry box for miles
starting_text = "Enter Miles here.." #initial instructions
miles_textbox = tk.Entry()
miles_textbox.insert(0,starting_text)
miles_textbox.place(x=100,y=100)
miles_textbox.bind("<FocusIn>",delete_temp_text)

#button
convert_button = tk.Button(text="Convert",fg="green",font=("Ariel",15,"bold"),command=button_click)
convert_button.place(x=110,y=200,width=80,height=30)


window.mainloop()
