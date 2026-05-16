from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password?: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():

    print("\nPassword Manager:")
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("\nAccount name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("\nWould you like to add a new password or view the existing ones? (Add/View), press Q to quit: ").lower()

    if mode  == "q":
        break
        
    elif mode == "add":
        add()
        
    elif mode == "view":
        view()
        
    else:
        print("\nInvalid mode.")
        continue
