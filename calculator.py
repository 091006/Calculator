import tkinter as tk

def button_clicknum(add):
    global fo, os1, os2, num1, num2, su

    fo = str(fo) + str(add)

    if os1 == "":
        num1 = str(num1) + str(add)
    elif os2 == "":
        num2 = str(num2) + str(add)

    label.config(text=f"{str(fo)}")

def button_clickos(add):
    global fo, os1, os2, num1, num2, su

    if add == "=":
        if os1 == "+":
            su = float(num1) + float(num2)
        elif os1 == "-":
            su = float(num1) - float(num2)
        elif os1 == "*":
            su = float(num1) * float(num2)
        elif os1 == "/":
            su = float(num1) / float(num2)

        fo = str(su)
        os1 = ""
        os2 = ""
        num1 = str(su)
        num2 = ""

    else:
        fo = str(fo) + str(add)
        if os1 == "":
            os1 = str(add)
        else:
            if os1 == "+":
                num1 = float(num1) + float(num2)
            elif os1 == "-":
                num1 = float(num1) - float(num2)
            elif os1 == "*":
                num1 = float(num1) * float(num2)
            elif os1 == "/":
                num1 = float(num1) / float(num2)

            os1 = str(add)
            num2 = ""

    label.config(text=f"{str(fo)}")

def button_clickc():
    global fo, os1, os2, num1, num2, su

    fo = ""
    os1 = ""
    os2 = ""
    num1 = ""
    num2 = ""
    su = ""

    label.config(text=f"{str(fo)}")

fo = ""
su = ""

os1 = ""
os2 = ""

num1 = ""
num2 = ""

bw = 80
bh = 70
iv = 80

root = tk.Tk()

root.title("계산기")
root.geometry("320x500")

label_font = ("None", 40)
label = tk.Label(root, text="", font=label_font)
label.place(x=0, y=20)

button = tk.Button(root, text="0", command=lambda: button_clicknum("0"))
button.place(x=iv, y=500-bh, width=bw, height=bh)

button = tk.Button(root, text=".", command=lambda: button_clicknum("."))
button.place(x=iv*2, y=500-bh, width=bw, height=bh)

button = tk.Button(root, text="=", command=lambda:button_clickos("="), bg="blue")
button.place(x=iv*3, y=500-bh, width=bw, height=bh)

button = tk.Button(root, text="1", command=lambda: button_clicknum("1"))
button.place(x=0, y=500-(bh*2), width=bw, height=bh)

button = tk.Button(root, text="2", command=lambda: button_clicknum("2"))
button.place(x=iv, y=500-(bh*2), width=bw, height=bh)

button = tk.Button(root, text="3", command=lambda: button_clicknum("3"))
button.place(x=iv*2, y=500-(bh*2), width=bw, height=bh)

button = tk.Button(root, text="+", command=lambda add="+": button_clickos(add))
button.place(x=iv*3, y=500-(bh*2), width=bw, height=bh)

button = tk.Button(root, text="4", command=lambda: button_clicknum("4"))
button.place(x=0, y=500-(bh*3), width=bw, height=bh)

button = tk.Button(root, text="5", command=lambda: button_clicknum("5"))
button.place(x=iv, y=500-(bh*3), width=bw, height=bh)

button = tk.Button(root, text="6", command=lambda: button_clicknum("6"))
button.place(x=iv*2, y=500-(bh*3), width=bw, height=bh)

button = tk.Button(root, text="-", command=lambda add="-": button_clickos(add))
button.place(x=iv*3, y=500-(bh*3), width=bw, height=bh)

button = tk.Button(root, text="7", command=lambda: button_clicknum("7"))
button.place(x=0, y=500-(bh*4), width=bw, height=bh)

button = tk.Button(root, text="8", command=lambda: button_clicknum("8"))
button.place(x=iv, y=500-(bh*4), width=bw, height=bh)

button = tk.Button(root, text="9", command=lambda: button_clicknum("9"))
button.place(x=iv*2, y=500-(bh*4), width=bw, height=bh)

button = tk.Button(root, text="*", command=lambda add="*": button_clickos(add))
button.place(x=iv*3, y=500-(bh*4), width=bw, height=bh)

button = tk.Button(root, text="C", command=button_clickc)
button.place(x=iv*2, y=500-(bh*5), width=bw, height=bh)

button = tk.Button(root, text="/", command=lambda add="/": button_clickos(add))
button.place(x=iv*3, y=500-(bh*5), width=bw, height=bh)

root.mainloop()