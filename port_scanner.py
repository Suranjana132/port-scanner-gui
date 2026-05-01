
import socket
import tkinter as tk
from tkinter import messagebox

#define functions
def port_scan():
    target = entry_ip.get() # type: ignore
    start_port = entry_start.get() # type: ignore
    end_port = entry_end.get() # type: ignore
    
    if not target or not start_port or not end_port:
        messagebox.showerror("Error","Please fill out all the fields")
        return
    
    try:
        start_port = int(start_port)
        end_port = int(end_port)
    except:
        messagebox.showerror("Error","ports must be numbers")
        return

    result_box.delete(1.0,tk.END) # type: ignore
    result_box.insert(tk.END, f"Scanning {target}....\n\n") # type: ignore

#mention the range
    for port in range(start_port, end_port +1): # type: ignore
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port)) # type: ignore

        if result == 0:
                result_box.insert(tk.END, f"Port {port} is OPEN\n") # type: ignore
        sock.close()

    result_box.insert(tk.END,"\n Scan Completed!") # type: ignore

#GUI
root = tk.Tk()
root.title("Port_Scanner_Project")
root.geometry("450x450")
root.configure(bg="black")
tk.Label(root, text="Target IP",bg="black", fg="Yellow").pack()

entry_ip = tk.Entry(root)
entry_ip.pack()
entry_ip.get()

tk.Label(root, text="Start_port", bg="black",fg="yellow").pack()
entry_start = tk.Entry(root)
entry_start.pack()


tk.Label(root, text="End_port",bg="black", fg="yellow").pack()
entry_end = tk.Entry(root)
entry_end.pack()

tk.Button(root, text="Start Scan", command= port_scan).pack(pady=10)

result_box = tk.Text(root, height = 15, bg="black", fg="yellow")
result_box.pack()

result_box.insert(tk.END, "Start Your Scan")

root.mainloop()



