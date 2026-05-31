<<<<<<< HEAD
from tkinter import *
from tkinter.scrolledtext import ScrolledText

# MAIN WINDOW
root = Tk()
root.title("AI Shopping Assistant")
root.geometry("450x600")
root.config(bg="#1e3c72")

# HEADER
header = Label(
    root,
    text="🤖 AI Shopping Assistant",
    bg="#1e3c72",
    fg="white",
    font=("Arial", 18, "bold"),
    pady=10
)
header.pack(fill=X)

# CHAT AREA
chat_area = ScrolledText(
    root,
    wrap=WORD,
    font=("Arial", 12),
    bg="white",
    fg="black"
)
chat_area.pack(padx=10, pady=10, fill=BOTH, expand=True)
chat_area.config(state=DISABLED)

# INPUT FRAME
input_frame = Frame(root, bg="#1e3c72")
input_frame.pack(fill=X, padx=10, pady=10)

# INPUT BOX
msg_entry = Entry(
    input_frame,
    font=("Arial", 14),
    width=25
)
msg_entry.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)

# ADD MESSAGE FUNCTION
def add_message(text):
    chat_area.config(state=NORMAL)
    chat_area.insert(END, text + "\n\n")
    chat_area.config(state=DISABLED)
    chat_area.yview(END)

# AI RESPONSE FUNCTION
def ai_reply(msg):

    msg = msg.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! I am your AI Shopping Assistant 😊"

    elif "phone" in msg:
        return "Tell me your budget: 10k / 20k / 30k / 50k"

    elif "10k" in msg:
        return "Redmi A3 or Realme C53 are good options."

    elif "20k" in msg:
        return "Samsung M35 or Vivo T3 are best choices."

    elif "laptop" in msg:
        return "What budget? 30k / 50k / 70k"

    elif "50k" in msg:
        return "HP Pavilion or Dell Inspiron are great!"

    elif "dress" in msg or "clothes" in msg:
        return "Do you want Casual, Party or Traditional wear?"

    elif "casual" in msg:
        return "Try T-shirt + Jeans combo 👕👖"

    elif "bye" in msg:
        return "Goodbye! Happy Shopping 🛍️"

    else:
        return "Hmm 🤔 I’m still learning. Ask about phones, laptops, or clothes."

# SEND FUNCTION
def send():

    user_text = msg_entry.get().strip()

    if user_text == "":
        return

    add_message("You: " + user_text)

    bot_response = ai_reply(user_text)

    add_message("Bot: " + bot_response)

    msg_entry.delete(0, END)

# SEND BUTTON
send_btn = Button(
    input_frame,
    text="SEND ➤",

    bg="#ff6600",
    fg="white",
    font=("Arial", 12, "bold"),
    width=10,
    command=send
)
send_btn.pack(side=RIGHT, padx=5)

# ENTER KEY SUPPORT
root.bind("<Return>", lambda event: send())

# START MESSAGE
add_message("Bot: Hello 👋 Ask me about phones, laptops, or clothes!")

# RUN APP
=======
from tkinter import *
from tkinter.scrolledtext import ScrolledText

# MAIN WINDOW
root = Tk()
root.title("AI Shopping Assistant")
root.geometry("450x600")
root.config(bg="#1e3c72")

# HEADER
header = Label(
    root,
    text="🤖 AI Shopping Assistant",
    bg="#1e3c72",
    fg="white",
    font=("Arial", 18, "bold"),
    pady=10
)
header.pack(fill=X)

# CHAT AREA
chat_area = ScrolledText(
    root,
    wrap=WORD,
    font=("Arial", 12),
    bg="white",
    fg="black"
)
chat_area.pack(padx=10, pady=10, fill=BOTH, expand=True)
chat_area.config(state=DISABLED)

# INPUT FRAME
input_frame = Frame(root, bg="#1e3c72")
input_frame.pack(fill=X, padx=10, pady=10)

# INPUT BOX
msg_entry = Entry(
    input_frame,
    font=("Arial", 14),
    width=25
)
msg_entry.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)

# ADD MESSAGE FUNCTION
def add_message(text):
    chat_area.config(state=NORMAL)
    chat_area.insert(END, text + "\n\n")
    chat_area.config(state=DISABLED)
    chat_area.yview(END)

# AI RESPONSE FUNCTION
def ai_reply(msg):

    msg = msg.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! I am your AI Shopping Assistant 😊"

    elif "phone" in msg:
        return "Tell me your budget: 10k / 20k / 30k / 50k"

    elif "10k" in msg:
        return "Redmi A3 or Realme C53 are good options."

    elif "20k" in msg:
        return "Samsung M35 or Vivo T3 are best choices."

    elif "laptop" in msg:
        return "What budget? 30k / 50k / 70k"

    elif "50k" in msg:
        return "HP Pavilion or Dell Inspiron are great!"

    elif "dress" in msg or "clothes" in msg:
        return "Do you want Casual, Party or Traditional wear?"

    elif "casual" in msg:
        return "Try T-shirt + Jeans combo 👕👖"

    elif "bye" in msg:
        return "Goodbye! Happy Shopping 🛍️"

    else:
        return "Hmm 🤔 I’m still learning. Ask about phones, laptops, or clothes."

# SEND FUNCTION
def send():

    user_text = msg_entry.get().strip()

    if user_text == "":
        return

    add_message("You: " + user_text)

    bot_response = ai_reply(user_text)

    add_message("Bot: " + bot_response)

    msg_entry.delete(0, END)

# SEND BUTTON
send_btn = Button(
    input_frame,
    text="SEND ➤",

    bg="#ff6600",
    fg="white",
    font=("Arial", 12, "bold"),
    width=10,
    command=send
)
send_btn.pack(side=RIGHT, padx=5)

# ENTER KEY SUPPORT
root.bind("<Return>", lambda event: send())

# START MESSAGE
add_message("Bot: Hello 👋 Ask me about phones, laptops, or clothes!")

# RUN APP
>>>>>>> 3beb5497e5856241cb89f7e7f7807243c426971f
root.mainloop()