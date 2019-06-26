import subprocess

#Application Configuration
lines = "================================"
projectname = "Earthbound"
version = "0.1"
domain = ()
newline = ("\n")
state = "good"


#Welcome
print (lines)
print ("Welcome To ", (projectname), " ", (version))
print (lines, '\n')

domaintest = input("Please Enter Domain To Initialise.\nPlease be aware this tool could easily trigger an IDS alert.\n")
print("Domain ", domaintest, " has been initialised. Ensure you have written permission \nbefore using this application. \n")
print("Enter to continue..")
con = input()


#mainmenu


import os
os.system("clear")
print(lines)
print("Welcome To The Main Menu")
print(lines)
print(newline)

while state == "good":
    print("1. Set New Target Domain")
    print("2. TCP-Ping")
    print("3. Fierce")
    print("4. NMAP Probe Scan")
    print("5. NMAP Banner Grab")
    print("6. WAF Detector")
    print("7. RC Scripts")
    print("8. Exit")
    print(newline)
    menu1 = input("")

    if menu1 == "1":
        print ("Setting New Target Domain")
        print(newline)
        domaintest = input("Insert New Target")
        print("Domain ", domaintest," has been initialised. Ensure you have written permission \nbefore using this application. \n")
        os.system("clear")
        pause = input("")

    if menu1 == "2":
        os.system("clear")
        print ("What port would you like to ping?")
        hpingport = input("")
        com = "hping3 -S -c 10 -p " + " " + hpingport + " " + domaintest
        os.system(com)
        pause = input("")


    elif menu1 == "8" or "exit":
        state = "bad"

    else:
        print ("Invalid Option")

# class Help:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#         self.slogan = Button(frame,
#                              text="Help", bg="white", fg="black",
#                              command=self.write_slogan)
#         self.slogan.pack(side=LEFT)
#     def write_slogan(self):
#         import os
#         print("sorry, no help yet!")
#         domaintest = input
#
# class Title:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame .pack()
#         self.slogan = Label(frame,
#                             text="Welcome to Earthbound", font=("arial",30))
#         self.slogan.pack(side=LEFT)
# class Title2:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame .pack()
#         self.slogan = Label(frame,
#                             text="WIP", fg="red", font=("arial", 30))
#         self.slogan.pack(side=LEFT)
#
#
#
#
#
# class SetDomain:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#         self.slogan = Button(frame,
#                              text="Initialise Domain", bg="white", fg="black",
#                              command=self.write_slogan)
#         self.slogan.pack(side=LEFT)
#     def write_slogan(self):
#         #Initialise Domain variable for use in other terminal commands..
#         domaintest = input("Please Enter Domain To Initialise.\nPlease be aware this tool could easily trigger an IDS alert.\n")
#         print("Domain ", domaintest, " has been initialised. Ensure you have written permission \nbefore using this application.")
#
# class SynScan:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#         self.slogan = Button(frame,
#                              text="TCP SYN Scan", bg="white", fg="black",
#                              command=self.write_slogan)
#         self.slogan.pack(side=LEFT)
#     def write_slogan(self):
#         import os
#         domainforsynin = ("hping3 -S " + domaintest)
#         print (domainforsynin)
#         os.system(domainforsynin)
#
#
#
#
# root = Tk()
# root.title("Earthbound WIP")
# root.geometry("500x500+200+200")
#
# app = Title(root)
# app = Title2(root)
# app = Help(root)
# app = SetDomain(root)
# app = SynScan(root)
# root.mainloop()
