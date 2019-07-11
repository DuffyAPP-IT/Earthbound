import subprocess

#Application Configuration
projectname = "Earthbound"
version = "0.5"
domain = ()

#GlobalFunctions

def welcome():
    print("================================")
    print("Welcome To {} {}".format(projectname,version))
    print ("================================", '\n')


def wait():
    waiting = input("")

#Welcome
welcome()
#print (lines)
#print ("Welcome To ", (projectname), " ", (version))
#print (lines, '\n')


#mainmenu


import os
os.system("clear")
welcome()
print("================================\n Welcome To The Main Menu\n================================\n")

def main():
    domaintest = input("Please Enter Domain To Initialise.\nPlease be aware this tool could easily trigger an IDS alert.\n")
    print("Domain ", domaintest," has been initialised. Ensure you have written permission \nbefore using this application. \n")
    con = input("Enter to continue..")

    print("1. Set New Target Domain")
    print("2. TCP-Ping")
    print("3. Fierce")
    print("4. NMAP Probe Scan")
    print("5. NMAP Banner Grab")
    print("6. WAF Detector")
    print("7. RC Scripts")
    print("8. Exit\n")
    menu1 = input("")

    if menu1 == "1":
        os.system("clear")
        welcome()
        print ("Setting New Target Domain\n")
        main()

    elif menu1 == "2":
        os.system("clear")
        welcome()
        hpingport = input("What port would you like to ping?")
        com = "hping3 -S -c 10 -p " + " " + hpingport + " " + domaintest
        os.system(com)
        wait()
        main()

    elif menu1 == "3":
        os.system("clear")
        welcome()
        fiercecon = input("Execute Fierce For Target Domain?\n This will likely trigger an IDS Alert \n Type yes to continue.")
        if fiercecon == "yes":
            print ("This command could take a while.. between 5 and 20 minutes")
            fierceexe = "fierce -dns " + domaintest
            os.system(fierceexe)
            wait()
        else:
            print ("command not executed.")
            wait()
            main()


    if menu1 == "4":
        os.system("clear")
        welcome()
        nmapgo = input("Execute NMap Probe Scan For Target Domain?\n This will likely trigger an IDS Alert \n Type yes to continue.")
        if nmapgo == "yes":
            print ("Identifying information of services running on target host")
            nmappn = "nmap -sV " + domaintest
            os.system(nmappn)
            wait()
            main()
        else:
            print("Invalid Response..\n Press enter to return to main menu.")
            wait()
            main()

    if menu1 == "5":
        os.system("clear")
        welcome()
        nmapgo2 = input("Execute NMap Banner Grab Script For Target Domain?\n This will likely trigger an IDS Alert \n Type yes to continue.")
        if nmapgo2 == "yes":
            print ("Grabbing service banner.. this command could take a while!")
            nmapbannergrab = "nmap -sV --script=banner " + domaintest
            os.system(nmapbannergrab)
            wait()
        else:
            print("Invalid Response.. \n Press enter to return to main menu.\n")
            wait()
            main()

    if menu1 == "6":
        os.system("clear")
        welcome()
        print ("WAF Detector\nThis menu option utilises WafW00f to detect web application firewalls.\n================================")
        wafw00f = "wafw00f " + domaintest
        os.system(wafw00f)
        wait()
        main()

    elif menu1 == "7":
        print("This option will be avalible in a future release \n and will allow you to configure RC Scripts using\na step by step process guided by this application.\nPress Enter to return to the main menu.")
        wait()
        main()



    elif menu1 == "8" or "exit":
        print("Goodbye.")

    else:
        print ("Invalid Option")
        main()
main()
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
