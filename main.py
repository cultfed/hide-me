import tkinter as tk
from tkinter import ttk
from tkinter import * 
import webbrowser, requests, json
from anyio import CapacityLimiter

with open('config.json') as f:
    config = json.load(f)
useragent = config.get('useragent')
def googleclick():
    
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://www.google.com/search?q=intext%3A%22%28%27{query1}%27%2C+%27{query2}%27%29%22&rlz=1C1VDKB_enUS959US959&ei=qF6FYrHuGveH9PwPwPeuuA0&ved=0ahUKEwix4vb8-On3AhX3A50JHcC7C9cQ4dUDCA0&oq=intext%3A%22%28%27aamaris%27%2C+%27walker%27%29%22&gs_lcp=Cgdnd3Mtd2l6EAxKBAhBGABKBAhGGABQAFgAYABoAHAAeACAAQCIAQCSAQCYAQA&sclient=gws-wiz"
    r = requests.get(url)
    if r.status_code == 200:
         webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
def thatsthemclick():
    
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://thatsthem.com/name/{query1}-{query2}"
    headerss = {f'User-Agent': '{useragent}'}
    r = requests.get(url, headers=headerss)
    if r.status_code == 200:
         webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
    else:
         print(r.status_code)
def searchpeoplefreeclick():
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://www.searchpeoplefree.com/find/{query1}-{query2}"
    headerss = {f'User-Agent': '{useragent}'}
    r = requests.get(url, headers=headerss)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
    else:
        print(r.status_code)
def nuwberclick():
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://nuwber.com/search?name={query1}%20{query2}"
    headerss = {f'User-Agent': '{useragent}'}
    r = requests.get(url, headers=headerss)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
    else:
        print(r.status_code)
def xlekclick():
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://xlek.com/search_results.php?fname={query1}&lname={query2}&locations:all"
    headerss = {f'User-Agent': '{useragent}'}
    r = requests.get(url, headers=headerss)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
    else:
        print(r.status_code)
def radarisclick():
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://radaris.com/ng/search?ff={query1}&fl={query2}"
    headerss = {f'User-Agent': '{useragent}'}
    r = requests.get(url, headers=headerss)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
    else:
        print(r.status_code)
def peoplesearchnowclick():
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://www.peoplesearchnow.com/person/{query1}-{query2}"
    headerss = {f'User-Agent': '{useragent}'}
    r = requests.get(url, headers=headerss)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
    else:
        print(r.status_code)

def webmiiclick():
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://webmii.com/people?n=%22{query1}%20{query2}%22#gsc.tab=0&gsc.q=%22{query1}%20{query2}%22&gsc.sort=date"
    headerss = {f'User-Agent': '{useragent}'}
    r = requests.get(url, headers=headerss)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
    else:
        print(r.status_code)
def abclick():
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://www.advancedbackgroundchecks.com/names/{query1}-{query2}"
    headerss = {f'User-Agent': '{useragent}'}
    r = requests.get(url, headers=headerss)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
    else:
        print(r.status_code)
def zabassearch():
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://www.zabasearch.com/people/{query1}+{query2}/"
    headerss = {f'User-Agent': '{useragent}'}
    r = requests.get(url, headers=headerss)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
    else:
        print(r.status_code)
def ssndeathindex():
    query1 = Firstname.get()
    query2 = Lastname.get()
    url = f"https://www.fold3.com/search?full-name~={query1}+{query2}:%22{query1}+{query1}%22&general.title.id=830:Social+Security+Death+Index"
    headerss = {f'User-Agent': '{useragent}'}
    r = requests.get(url, headers=headerss)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 429:
        print("Rate Limited!, try again later")
    else:
        print(r.status_code)

def getInputBoxValue():
	userInput = Lastname.get()
	return userInput
def getInputBoxValue():
	userInput = Firstname.get()
	return userInput

root = Tk()
root.geometry('780x393')
root.configure(background='#000000')
root.title('Welcome to cultfed OSINT tools t.me/cultfed')

Firstname=Entry(root)
Firstname.place(x=280, y=172)

Lastname=Entry(root)
Lastname.place(x=500, y=172)

Button(root, text='dead ssn', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=ssndeathindex).place(x=18, y=60)
Button(root, text='zabassearch', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=zabassearch).place(x=18, y=90)
Button(root, text='abc', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=abclick).place(x=18, y=120)
Button(root, text='webmii', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=webmiiclick).place(x=18, y=150)
Button(root, text='peoplesearchnow', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=peoplesearchnowclick).place(x=18, y=180)
Button(root, text='radaris', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=radarisclick).place(x=18, y=210)
Button(root, text='Nuwber', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=nuwberclick).place(x=18, y=302)
Button(root, text='xlek', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=xlekclick).place(x=18, y=240)
Button(root, text='searchpeoplefree', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=searchpeoplefreeclick).place(x=18, y=332)
Button(root, text='thatsthem', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=thatsthemclick).place(x=18, y=362)
Button(root, text='google', bg='#DCDCDC', font=('helvetica', 8, 'normal'), command=googleclick).place(x=18, y=270)

Label(root, text='HOMESINT', bg='#000000', font=('helvetica', 8, 'normal')).place(x=348, y=-18)
Label(root, text='First Name', bg='#FFFFFF', font=('helvetica', 8, 'normal')).place(x=280, y=200)
Label(root, text='First Name', bg='#FFFFFF', font=('helvetica', 8, 'normal')).place(x=500, y=200)


root.mainloop()


