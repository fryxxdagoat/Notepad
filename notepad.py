import tkinter as tk

main_window = tk.Tk()

main_window.title("Notepad")
main_window.geometry("800x500")

#Labels
label1 = tk.Label(main_window, text="Notepad", font=("Arial", 30))
label1.pack(padx=40, pady=50)



#button
def notepad_open():
    new_window = tk.Tk()  
    new_window.title("New Notepad")
    new_window.geometry("800x500")

    #Textbox
    notepad_text = tk.Text(new_window, height=600, width=900)
    notepad_text.pack(padx=30, pady=30)

    new_window.mainloop()


btn1 = tk.Button(main_window, text="➕", command=notepad_open)
btn1.pack(pady=20)

main_window.mainloop()