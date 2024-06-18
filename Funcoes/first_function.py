def show_message():
    print("Hello, World!")

def show_message_2(name):
    print(f"Seja bem vindo(a), {name}")

def show_message_3(name = "Anônimo"):
    print(f"Seja bem vindo(a), {name}")

show_message()
show_message_2("Maria")
show_message_3()
show_message_3("Anya")