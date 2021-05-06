import tkinter as tk

import requests
from bs4 import BeautifulSoup

root = tk.Tk()
root.geometry("200x300")
root.title("Şehir Sıcaklık")
root.configure(bg="black")

def check():
    city = y.get()

#url
    url = f"https://www.google.com.tr/search?ei=kNcBYImLM8vCgweep5-IAQ&q=weather+in+{city}&oq=weather+in+ankara&gs_lcp=CgZwc3ktYWIQAzICCAAyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAELADEEM6BAgAEENQ9JEBWNuXAWCemwFoAXACeACAAYwBiAH5BZIBAzAuNpgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=psy-ab&ved=0ahUKEwiJk5fcwZ7uAhVL4eAKHZ7TBxEQ4dUDCAw&uact=5"
#Sending HTTP request
    req = requests.get(url)
#Pulling HTTP data from internet
    sor = BeautifulSoup(req.text,"html.parser")
#Finding temperature in Celsius
    temp = sor.find("div",class_="BNeawe").text
    g = f"temprature in {city} is",temp
    l2.configure(text=g)

y = tk.StringVar()
e1 = tk.Entry(root,textvariable=y)
l1=tk.Label(root,text="Enter City: ")
l1.place(x=10,y=5)
e1.place(x=10,y=35,height=35,width=180)
l2=tk.Label(root,text="",bg="black",fg="yellow")
l2.place(x=10,y=105)
b=tk.Button(root,text="Check",command=check)
b.place(x=10,y=75)
root.mainloop()