import os

def launch_gui_clients():
    try:
        n = int(input("Enter number of GUI clients to create: "))
    except ValueError:
        print("Invalid number")
        return

    auto = input("Auto-name clients? (yes/no): ").lower()

    for i in range(1, n + 1):
        name = f"Client{i}" if auto == "yes" else ""

        # Windows START command (forces GUI window)
        if name:
            os.system(f'start cmd /k python gui_client.py {name}')
        else:
            os.system('start cmd /k python gui_client.py')

launch_gui_clients()

