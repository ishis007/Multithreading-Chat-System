import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import os
import sys

HOST = '127.0.0.1'
PORT = 1234
HISTORY_FILE = "chat_history/history.txt"

class ChatGUI:
    def __init__(self, preset_name=None):
        self.root = tk.Tk()
        self.root.title("Advanced Chat System")
        self.root.geometry("800x500")

        self.dark = False
        self.name = preset_name
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.build_login() if not self.name else self.connect()
        self.root.mainloop()

    # ---------- LOGIN ----------
    def build_login(self):
        self.login = tk.Frame(self.root)
        self.login.pack(expand=True)

        tk.Label(self.login, text="Enter Name", font=("Arial", 16)).pack(pady=10)
        self.name_entry = tk.Entry(self.login, font=("Arial", 14))
        self.name_entry.pack(pady=10)

        tk.Button(self.login, text="Join", command=self.manual_login).pack(pady=10)

    def manual_login(self):
        self.name = self.name_entry.get().strip()
        if self.name:
            self.login.destroy()
            self.connect()

    # ---------- CHAT ----------
    def build_chat(self):
        main = tk.Frame(self.root)
        main.pack(fill=tk.BOTH, expand=True)

        self.users = tk.Listbox(main, width=20)
        self.users.pack(side=tk.LEFT, fill=tk.Y)

        right = tk.Frame(main)
        right.pack(fill=tk.BOTH, expand=True)

        self.chat = scrolledtext.ScrolledText(right, state='disabled')
        self.chat.pack(fill=tk.BOTH, expand=True)

        bottom = tk.Frame(right)
        bottom.pack(fill=tk.X)

        self.msg = tk.Entry(bottom)
        self.msg.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.msg.bind("<Return>", lambda e: self.send())

        tk.Button(bottom, text="Send", command=self.send).pack(side=tk.RIGHT)
        tk.Button(bottom, text="Toggle Theme", command=self.toggle_theme).pack(side=tk.RIGHT)

        self.load_history()

    # ---------- CONNECT ----------
    def connect(self):
        self.client.connect((HOST, PORT))
        self.client.send(self.name.encode('utf-8'))
        self.build_chat()

        threading.Thread(target=self.receive, daemon=True).start()

    # ---------- RECEIVE ----------
    def receive(self):
        while True:
            try:
                msg = self.client.recv(1024).decode('utf-8')

                if msg.startswith("USERS:"):
                    self.update_users(msg[6:])
                elif msg.startswith("SYSTEM:"):
                    self.display(msg[7:], "blue")
                else:
                    self.display(msg)
                    self.save_history(msg)

            except:
                break

    # ---------- SEND ----------
    def send(self):
        text = self.msg.get().strip()
        if text:
            self.client.send(text.encode('utf-8'))
            self.msg.delete(0, tk.END)

    # ---------- UI HELPERS ----------
    def display(self, msg, color="black"):
        self.chat.config(state='normal')
        self.chat.insert(tk.END, msg + "\n", color)
        self.chat.tag_config(color, foreground=color)
        self.chat.config(state='disabled')
        self.chat.yview(tk.END)

    def update_users(self, users):
        self.users.delete(0, tk.END)
        for u in users.split(","):
            self.users.insert(tk.END, u)

    def toggle_theme(self):
        self.dark = not self.dark
        bg = "#2b2b2b" if self.dark else "white"
        fg = "white" if self.dark else "black"
        self.chat.config(bg=bg, fg=fg)
        self.msg.config(bg=bg, fg=fg)

    # ---------- HISTORY ----------
    def save_history(self, msg):
        os.makedirs("chat_history", exist_ok=True)
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n")

    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    self.display(line.strip())

# ---------- RUN ----------
if __name__ == "__main__":
    preset = sys.argv[1] if len(sys.argv) > 1 else None
    ChatGUI(preset)
