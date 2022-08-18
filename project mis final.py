
#Aatish Patel MIS 315 FINAL PROJECT 2022 Summer

from tkinter import Label, Button, StringVar, Tk, ttk, messagebox, simpledialog

#learnt about pandas from w3schools
import pandas as pd

def get_puranusdm(df, date):
    """
    Get the puranusdm data for a given date.
    """
    price = df[df['DATE'] == date]["PURANUSDM"].values[0]
    messagebox.showinfo("Uranium Price", "The price for {} is {}".format(date, price))

def get_month(event, month_var):
    """
    Get the month from the month combobox.
    """
    # print(month_var.get())
    return month_var.get()

def get_year(event, year_var):
    """
    Get the year from the year combobox.
    """
    # print(year_var.get())
    return year_var.get()

def gen_avg_price(df, from_year, to_year):
    """
    Generate the average price for a given range of years.
    """
    if from_year > to_year:
        messagebox.showinfo("Error", "Invalid Range: From year must be greater than to year.")
    else:
        file_name = "avg_price_data.txt"

        avg_price = df[df['DATE'] >= (from_year + "-" + "01" + "-01")][df['DATE'] <= (to_year + "-" + "12" + "-01")]["PURANUSDM"].mean()
    
        with open(file_name, "a") as f:
            f.write("Average Price for {} to {}: {}\n".format(from_year, to_year, round(avg_price, 2)))
        file_save_message = "Results saved to {}".format(file_name)
        messagebox.showinfo("Average Price", "The average price for {} to {} is {}.\n{}".format(from_year, to_year, round(avg_price, 2), file_save_message))

root = Tk()
root.title("Global Price of Uranium")
root.resizable(False, False)
root.geometry("500x500")

data = pd.read_csv("PURANUSDM.csv", parse_dates=True)

#Creating the labels color and fonts and dimensions

lbl_search = Label(root, text="Search Uranium Price", font=("Arial", 14, "bold"))
lbl_search.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

lbl_month = Label(root, text="Month:", font=("Arial", 12, "bold"))
lbl_month.grid(row=1, column=0, padx=10, pady=10, sticky="e")

#To ensure that the months are valid as in 12 months in a year

month_var = StringVar()
cbx_month = ttk.Combobox(root, textvariable=month_var, state="readonly", font=("Arial", 12, "bold"))
cbx_month["values"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
cbx_month.current(0)
cbx_month.bind("<<ComboboxSelected>>", lambda event: get_month(event, month_var))
cbx_month.grid(row=1, column=1, padx=10, pady=10)

lbl_year = Label(root, text="Year:", font=("Arial", 12, "bold"))
lbl_year.grid(row=2, column=0, padx=10, pady=10, sticky="e")

year_var = StringVar()
cbx_year = ttk.Combobox(root, textvariable=year_var, state="readonly", font=("Arial", 12, "bold"))
cbx_year["values"] = [i for i in range(1990, 2022)]
cbx_year.current(0)
cbx_year.bind("<<ComboboxSelected>>", lambda event: get_year(event, year_var))
cbx_year.grid(row=2, column=1, padx=10, pady=10)

btn_search = Button(root, text="Search", font=("Arial", 12, "bold"), command=lambda: get_puranusdm(data, str(year_var.get()) + "-" + str(month_var.get()) + "-01"))
btn_search.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

lbl_generate_avg = Label(root, text="Generate Uranium Average Price", font=("Arial", 14, "bold"))
lbl_generate_avg.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

lbl_from_year = Label(root, text="From Year:", font=("Arial", 12, "bold"))
lbl_from_year.grid(row=5, column=0, padx=10, pady=10)

from_year_var = StringVar()
cbx_from_year = ttk.Combobox(root, textvariable=from_year_var, state="readonly", font=("Arial", 12, "bold"))
cbx_from_year["values"] = [i for i in range(1990, 2022)]
cbx_from_year.current(0)
cbx_from_year.bind("<<ComboboxSelected>>", lambda event: get_year(event, from_year_var))
cbx_from_year.grid(row=5, column=1, padx=10, pady=10)

lbl_to_year = Label(root, text="To Year:", font=("Arial", 12, "bold"))
lbl_to_year.grid(row=6, column=0, padx=10, pady=10, sticky="e")

to_year_var = StringVar()
cbx_to_year = ttk.Combobox(root, textvariable=to_year_var, state="readonly", font=("Arial", 12, "bold"))
cbx_to_year["values"] = [i for i in range(1990, 2022)]
cbx_to_year.current(0)
cbx_to_year.bind("<<ComboboxSelected>>", lambda event: get_year(event, to_year_var))
cbx_to_year.grid(row=6, column=1, padx=10, pady=10)

btn_generate = Button(root, text="Generate Uranium Average Price", font=("Arial", 12, "bold"), command=lambda: gen_avg_price(data, from_year_var.get(), to_year_var.get()))
btn_generate.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()