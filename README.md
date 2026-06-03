# Multithreaded Chat System

## Overview

The Multithreaded Chat System is a Python-based client-server chat application that enables multiple users to communicate in real time over a local network. The project uses socket programming for communication, multithreading for handling multiple clients simultaneously, and Tkinter for a graphical user interface.

The system supports public messaging, private messaging, active user tracking, chat history storage, and theme customization.

---

## Features

### Real-Time Communication

* Instant message delivery between connected clients.
* Supports multiple users simultaneously.

### Multithreaded Server

* Each connected client is handled in a separate thread.
* Ensures uninterrupted communication among multiple users.

### Private Messaging

* Send direct messages to a specific user.
* Format:

```
@username Your message here
```

### Active User List

* Displays all currently connected users.
* Updates automatically when users join or leave.

### System Notifications

* Join and leave notifications are broadcast to all users.

### Chat History

* Stores chat messages locally.
* Automatically loads previous messages when the client starts.

### GUI Interface

* Built using Tkinter.
* Easy-to-use graphical interface for chatting.

### Theme Switching

* Toggle between light and dark mode.

### Client Automation

* Launch multiple GUI clients automatically for testing purposes.

---

## Technologies Used

* Python
* Socket Programming
* Multithreading
* Tkinter GUI
* File Handling
* Client-Server Architecture

---

## Project Structure

```
Multithreaded-Chat-System/
│
├── server.py
├── gui_client.py
├── client_launcher.py
├── chat_history/
│   └── history.txt
└── README.md
```

### File Descriptions

#### server.py

* Creates and manages the chat server.
* Handles client connections.
* Maintains active user list.
* Supports broadcasting and private messaging.
* Uses multithreading for concurrent client handling.

#### gui_client.py

* Graphical chat client built using Tkinter.
* Sends and receives messages.
* Displays active users.
* Loads and saves chat history.
* Supports theme switching.

#### client_launcher.py

* Automates launching multiple GUI client windows.
* Useful for testing multi-user communication.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Multithreaded-Chat-System.git
cd Multithreaded-Chat-System
```

### Requirements

Python 3.8 or above.

No external libraries are required.

---

## Running the Application

### Step 1: Start Server

```bash
python server.py
```

Output:

```
Server started...
```

### Step 2: Start Client

```bash
python gui_client.py
```

Enter a username and join the chat.

---

## Launch Multiple Clients Automatically

```bash
python client_launcher.py
```

Choose:

```
Enter number of GUI clients to create:
```

You may also enable automatic client naming.

---

## Private Messaging Example

To send a private message:

```
@Client2 Hello, this is a private message
```

Only Client2 will receive the message.

---

## Learning Outcomes

This project demonstrates:

* TCP Socket Programming
* Multithreading in Python
* GUI Development with Tkinter
* Client-Server Architecture
* Real-Time Communication Systems
* Concurrent Programming
* Network Application Development

---

## Future Enhancements

* User authentication and login system
* Group chat rooms
* End-to-end encryption
* File sharing support
* Emoji support
* Message delivery status
* Database-backed chat history
* LAN/Wi-Fi deployment support

---

## Author

Developed as a learning project to explore networking, multithreading, and GUI development using Python.
