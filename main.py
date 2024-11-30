import os
import random
import getpass
import time
import platform
import zipfile
from colorama import *
from datetime import datetime, date

username = input("Username : ")
password = getpass.getpass("Password : ")


while True:
    terminal = input("$ ")

    if terminal == 'help':
        print("""
        help        Terminal Tutorial
        cal         Open Calculator
        time        Check Time
        ls          Check Directory
        txtwriter   Open Text Writer
        txtreader   Open Text Reader
        rps         Open RPS Game
        unzipper    Open Unzipper App
        about       About Persia OS
        whoami      Check Username
        cls/clear   Clear Screen
        exit        Quit From OS      
        """)
    elif terminal == 'cal':
        intorfloat = input("Int Or Float : ")
        if intorfloat == 'int':
            intnum1 = int(input("Enter Your 1st Number : "))
            intnum2 = int(input("Enter Your 2nd Number : "))
            intoperator = input("Enter Your Operator : ")

            if intoperator == '+':
                print(f"{intnum1 + intnum2:,}")
            elif intoperator == '-':
                print(f"{intnum1 - intnum2:,}")
            elif intoperator == '*':
                print(f"{intnum1 * intnum2:,}")
            elif intoperator == '/':
                print(f"{intnum1 / intnum2:,}")
            else:
                print("Error")
        if intorfloat == 'float':
            floatnum1 = float(input("Enter Your 1st Number : "))
            floatnum2 = float(input("Enter Your 2nd Number : "))
            floatoperator = input("Enter Your Operator : ")

            if floatoperator == '+':
                print(f"{floatnum1 + floatnum2:,}")
            elif floatoperator == '-':
                print(f"{floatnum1 - floatnum2:,}")
            elif floatoperator == '*':
                print(f"{floatnum1 * floatnum2:,}")
            elif floatoperator == '/':
                print(f"{floatnum1 / floatnum2:,}")
            else:
                print("Error")
    elif terminal == 'time':
        time_check = datetime.time(datetime.now())

        date_check = date.today()

        print(f"""
        {time_check.hour}:{time_check.minute}:{time_check.second}
        {date_check.day}/{date_check.month}/{date_check.year}
        """)
    elif terminal == 'ls':
        print(os.getcwd())
    elif terminal == 'txtwriter':
        writetxt = input("Write Your Text(format: *.txt) : ")
        if platform.system() == 'Windows':
            os.system(f"notepad {writetxt}")
        elif platform.system() == 'MacOS':
            os.system(f"TextEdit {writetxt}")
        elif platform.system() == 'Linux':
            os.system(f"nano {writetxt}")
    elif terminal == 'txtreader':
        readtxt = input("Enter Read Your File : ")
        if os.name == 'nt':
            os.system(f"type {readtxt}")
        else:
            os.system(f"cat {readtxt}")
    elif terminal == 'rps':
        print("Loading....")
        time.sleep(5)
        while True:
            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")
            print("""
            ██████╗░██████╗░░██████╗
            ██╔══██╗██╔══██╗██╔════╝
            ██████╔╝██████╔╝╚█████╗░
            ██╔══██╗██╔═══╝░░╚═══██╗
            ██║░░██║██║░░░░░██████╔╝
            ╚═╝░░╚═╝╚═╝░░░░░╚═════╝░
            """)
            startmenu = input("Start Game / Option / Exit ? ".lower())
            
            if startmenu == 'start game' or startmenu == 'start':
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                print("Loading")
                time.sleep(5)
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                player_win = 0
                computer_win = 0
                options_game = ['r', 'p', 's']
                while True:
                    player = input("R / P / S or q to Exit: ".lower())
                    if (player == 'q'):
                        if os.name == 'nt':
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("Exiting...")
                        print("Player Win : ", player_win)
                        print("Computer Win : ", computer_win)
                        time.sleep(5)
                        break
                    elif (player not in options_game):
                        continue
                    random_no = random.randint(0, 2)
                    computer = options_game[random_no]
                    if (player == 's' and computer == 'p'):
                        print("Player Win....")
                        player_win += 1
                    elif (player == 'p' and computer == 'r'):
                        print("Player Win....")
                        player_win += 1
                    elif (player == 'r' and computer == 's'):
                        print("Player Win....")
                        player_win += 1
                    elif (computer == 's' and player == 'p'):
                        print("Computer Win....")
                        computer_win += 1
                    elif (computer == 'p' and player == 'r'):
                        print("Computer Win....")
                        computer_win += 1
                    elif (computer == 'r' and player == 's'):
                        print("Computer Win....")
                        computer_win += 1
                    elif (computer == player):
                        print("Equal")
                    else:
                        print("it Was Worng")
            elif startmenu == 'option':
                color = input("Color : ".lower())

                if color == 'red':
                    print(Fore.RED)
                elif color ==  'blue':
                    print(Fore.BLUE)
                elif color ==  'green':
                    print(Fore.GREEN)
                elif color ==  'yellow':
                    print(Fore.YELLOW)
                elif color ==  'cayan':
                    print(Fore.CYAN)
                elif color ==  'reset':
                    print(Fore.RESET)
                else:
                    print("Error")
            elif startmenu == 'exit' or startmenu == 'quit':
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                print("Bye Bye....")
                time.sleep(5)
                print(Fore.RESET)
                break
    elif terminal == 'unzipper':

        target = input("Enter Your File To Extract : ")
        try:

            print("Start Extrating...")

            unzip = zipfile.ZipFile(target)

            unzip.extractall()
            unzip.close()
            
            print("Extrating is Seccesfull")
        except:
            print("Error")
    elif terminal == 'about':
        print("""
            ██████╗░███████╗██████╗░░██████╗██╗░█████╗░░░░░░░░█████╗░░██████╗
            ██╔══██╗██╔════╝██╔══██╗██╔════╝██║██╔══██╗░░░░░░██╔══██╗██╔════╝
            ██████╔╝█████╗░░██████╔╝╚█████╗░██║███████║█████╗██║░░██║╚█████╗░
            ██╔═══╝░██╔══╝░░██╔══██╗░╚═══██╗██║██╔══██║╚════╝██║░░██║░╚═══██╗
            ██║░░░░░███████╗██║░░██║██████╔╝██║██║░░██║░░░░░░╚█████╔╝██████╔╝
            ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░
            version 0.1
            beta
        """)
    elif terminal == 'cls' or terminal == 'clear':
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
    elif terminal == 'whoami':
        print(username)
    elif terminal == "exit":
        print("Log OFF....")
        time.sleep(5)
        print("Shutting Down....")
        time.sleep(5)
        break
    elif terminal == '':
        pass
    else:
        print("Not Found")
    
                    
                    


                    
                
        
        
