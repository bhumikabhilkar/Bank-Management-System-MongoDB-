import pymongo
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Bank:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost:27017")
        self.db = self.client['Bank']
        self.collection = self.db['Bank_collection']

    def insert_data(self, name, location, bank_name):
        try:
            self.collection.insert_one({'Name': name, 'Location': location, 'Bank Name': bank_name})
            messagebox.showinfo("Success", "Data inserted successfully!")
        except pymongo.errors.PyMongoError as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")

    def view_data(self):
        cursor = self.collection.find({})
        data = []
        for document in cursor:
            data.append(document)
        return data

    def delete_data(self, name):
        try:
            self.collection.delete_one({'Name': name})
            messagebox.showinfo("Success", "Data deleted successfully!")
        except pymongo.errors.PyMongoError as e:
            messagebox.showerror("Error", f"Error deleting data: {e}")

    def update_data(self, name, new_location, new_bank_name):
        try:
            self.collection.update_one({'Name': name}, {'$set': {'Location': new_location, 'Bank Name': new_bank_name}})
            messagebox.showinfo("Success", "Data updated successfully!")
        except pymongo.errors.PyMongoError as e:
            messagebox.showerror("Error", f"Error updating data: {e}")

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management System GUI")
        root.geometry("500x400")
        self.bank = Bank()

        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.location_label = tk.Label(root, text="Location:")
        self.location_entry = tk.Entry(root)

        self.bank_name_label = tk.Label(root, text="Bank Name:")
        self.bank_name_entry = tk.Entry(root)

        self.insert_button = tk.Button(root, text="Insert", command=self.insert_data)
        self.view_button = tk.Button(root, text="View All", command=self.view_all_data)
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_data)
        self.update_button = tk.Button(root, text="Update", command=self.update_data)

        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.location_label.grid(row=1, column=0)
        self.location_entry.grid(row=1, column=1)
        self.bank_name_label.grid(row=2, column=0)
        self.bank_name_entry.grid(row=2, column=1)

        self.insert_button.grid(row=3, column=0, columnspan=2)
        self.view_button.grid(row=4, column=0, columnspan=2)
        self.delete_button.grid(row=5, column=0, columnspan=2)
        self.update_button.grid(row=6, column=0, columnspan=2)

        self.text_box = tk.Text(root, height=10, width=40)
        self.text_box.grid(row=7, column=0, columnspan=2)

        # Colored buttons with appropriate background color property
        self.insert_button = tk.Button(root, text="Insert", command=self.insert_data, bg="lightgreen")
        self.insert_button.grid(row=3, column=0, columnspan=2)
        self.view_button = tk.Button(root, text="View All", command=self.view_all_data, bg="lightblue")
        self.view_button.grid(row=4, column=0, columnspan=2)
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_data, bg="gray")
        self.delete_button.grid(row=5, column=0, columnspan=2)
        self.update_button = tk.Button(root, text="Update", command=self.update_data, bg="lightpink")
        self.update_button.grid(row=6, column=0, columnspan=2)

        self.text_box = tk.Text(root, height=10, width=40)
        self.text_box.grid(row=7, column=0, columnspan=2)

        

    def insert_data(self):
        name = self.name_entry.get()
        location = self.location_entry.get()
        bank_name = self.bank_name_entry.get()
        self.bank.insert_data(name, location, bank_name)
        self.clear_fields()

    def view_all_data(self):
        data = self.bank.view_data()
        self.text_box.delete('1.0', tk.END)
        for document in data:
            self.text_box.insert(tk.END, str(document) + '\n')

    def delete_data(self):
        name = self.name_entry.get()
        self.bank.delete_data(name)
        self.clear_fields()

    def update_data(self):
        name = self.name_entry.get()
        new_location = self.location_entry.get()
        new_bank_name = self.bank_name_entry.get()
        self.bank.update_data(name, new_location, new_bank_name)
        self.clear_fields()

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.bank_name_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()