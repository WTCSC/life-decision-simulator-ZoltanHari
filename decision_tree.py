import re 

def read_file(msg_num):
    with open("Messages", "r") as file:
        message = file.read().split(f"%msg{msg_num}%")[1]
        try:
            responses = message.split("1.")[1].split("2.")
            while True:
                option = input(re.sub(r"%..%","",re.sub(r"%.%","",message)))
                if option == "1":
                    read_file(responses[0].split("%")[1])
                    break
                elif option == "2":
                    read_file(responses[1].split("%")[1])
                    break
                else:
                    print("Invalid Choice, Please Choose 1 or 2")
        except:
            print(re.sub(r"%..%","",re.sub(r"%.%","",message)))

read_file("0")