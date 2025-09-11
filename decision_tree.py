def read_file(msg_num):
    with open("Messages", "r") as file:
        messages = file.read()