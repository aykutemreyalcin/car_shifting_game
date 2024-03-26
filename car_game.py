import time
import random

def Main():
    x = True
    while x == True:
        print("\nget ready!",sep="",end="\r",flush=True)
        time.sleep(1)
        print("3!               ",sep="",end="\r",flush=True)
        time.sleep(1)
        print("2!!              ",sep="",end="\r",flush=True)
        time.sleep(1)
        print("1!!!             ",sep="",end="\r",flush=True)
        time.sleep(1)
        print("GO               ",sep="",end="\r",flush=True)
        time.sleep(0.5)
        time_list = []
        for i in range(1,7):
            random_number = random.randint(1,9)
            max_speed = i*30
            print("speed is",max_speed-20)
            time.sleep(0.5)
            print("speed is",max_speed-10)
            time.sleep(0.5)
            print("speed is",max_speed)
            time.sleep(0.5)
            print("shift in gear",i,"by inputting",random_number)
            print("you have <1.5> seconds")
            time.sleep(0.2)
            time_start = time.time()
            shift = int(input(""))
            time_end = time.time()
            time_result = time_end - time_start
            if time_result <= 1.5 and shift == random_number:
                time_list.append("gear{} --> {} seconds".format(i,time_result))
                print("LEETTSS GOOO!!")
                time.sleep(0.3)     
            else:
                print("OH NO CRASHING!")
                time.sleep(1)
                print(":/")
                time_list.append("gear{} --> {} seconds (this is where you messed up)".format(i,time_result))
                break
        print("Hell Yeah you made it")
        answer_1 = input("wanna see the results? yes/no?\n")
        if answer_1 == "yes":
            for result in time_list:
                print(result)
        answer_2 = input("wanna play again? yes/no?")
        if answer_2 == "no":
            print(":(")
            x = False       

Main()