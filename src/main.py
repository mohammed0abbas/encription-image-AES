import aes
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


bass = tk.Tk()
bass.title("AES image encription")
bass.geometry("600x500")
bass.resizable(0, 0)
#set bass center
bass.update_idletasks()
width = bass.winfo_width()
height = bass.winfo_height()
x = (bass.winfo_screenwidth() // 2) - (width // 2)
y = (bass.winfo_screenheight() // 2) - (height // 2)
bass.geometry('{}x{}+{}+{}'.format(width, height, x, y))




class main_form(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # self.create_widgets()
        self.ui_of_encript()

    
    
    def button_command(self):
            file_path = filedialog.askopenfilename(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
            self.bros_label.config(text=file_path)
            pass


    def ui_of_encript(self):
        button_browser = tk.Button(bass, text="Browser image",width=15, command=self.button_command)
        button_browser.place(x=20, y=20)
        self.bros_label = tk.Label(bass,width=50, height=1, bg="white", text="No file selected")
        self.bros_label.place(x=140, y=22)

        self.key_label = tk.Label(bass, text="Key :").place(x=100, y=57)
        self.key = tk.Entry(bass, width=59, bg="white")
        self.key.place(x=140, y=60)
        tk.Label(bass, text="Note : Key must be 16, 24, 32 or null bytes long").place(x=140, y=80)

        button_encript = tk.Button(bass, text="Encript Image", command=self.encript)
        button_encript.place(x=200, y=120)
        button_decript = tk.Button(bass, text="Decript Image", command=self.decript)
        button_decript.place(x=310, y=120)

        button_exit = tk.Button(bass, text="Exit", command=self.destroy)
        button_exit.place(x=550, y=20)

    def save_file_dilog(self):
        file = filedialog.asksaveasfilename(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        return file
    
    def encript(self):
       
        if self.key.get() != "" and (len(self.key.get()) == 16 or len(self.key.get()) == 24 or len(self.key.get()) == 32):
            key_var = self.key.get().encode()
            
        elif self.key.get() == "":
           key_var = b'1234567890123456'
        else:
            messagebox.showerror("Error", "Key must be 16, 24, 32 or null bytes long")
            return
    
        file = self.save_file_dilog()
        aes.encrypt(self.bros_label.cget('text'), file, key_var)
        messagebox.showinfo("Encript", "Encripted")

    def decript(self):
        if self.key.get() != "" and (len(self.key.get()) == 16 or len(self.key.get()) == 24 or len(self.key.get()) == 32):
            key_var = self.key.get().encode()
            
        elif self.key.get() == "":
           key_var = b'1234567890123456'
        else:
            messagebox.showerror("Error", "Key must be 16, 24, 32 or null bytes long")
            return
    
        file = self.save_file_dilog()
        aes.decrypt(self.bros_label.cget('text'), file, key_var)
        messagebox.showinfo("Decript", "Decripted")
    










x = main_form(bass)
x.mainloop()



def main():
    # Test the AES implementation
    # aes.encrypt('./src/test2.jpg', './src/encript_image/test.enc', b'1234567890123456')
    # aes.decrypt('test.enc', './src/decript_image/test.jpg', b'1234567890123456')
    pass


