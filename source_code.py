import time
import threading
dic={}
def create(): #timeout=0 means no expiry time if so we need to have an expiry time for key we can pass a third argument.
    key = input("enter a key: ")
    values= int(input("enter a value: "))
    timeout= int(input("enter expiry time: "))
    if key in dic:
        print("Key already present in database. Enter a valid key \n")# if key is already present print this statement
    else:
        if (key.isalpha()):#to check whether all the elements in key are alphabets
            if (len(dic)<(1024*1024*1024) and values <= (16*1024*1024)):#to check the specified requirements in assignment
                if (timeout == 0):
                    store=[values,timeout] #since in this case we need two values for one key (i.e) value as well as timeout; we are storing it in list
                else:
                    store=[values, time.time()+timeout]# in this time  is an inbuilt function is used to get the present time and to it the timeout variable is added so the key expires in mentioned time
            if (len(key)<= 32):#to check the specified requirements in assignment
                dic[key]=store
                print("Key stored \n")
            else:
                print("Memory limit exceeded \n ")# if the entered value exceed the mentioned requirement then print this error message
        else:
            print("Key only take alphabets. Please enter a valid key\n")# if entered key is not alphabets print this error message

def read():
    key = input("enter a key: ")
    # if key is not present in the dictionary then print the following statement
    if key not in dic:
        print("Invalid key. Key is not present")
    else:
        a=dic[key]
        if (a[1] == 0): #if timeout is zero we can print the key and value in json format 
            obj=str(key)+":"+str(a[0])
            print (obj)
            print("\n")
        else:
            if (time.time() < a[1]): # if there is a timeout then we need to compare with the present time and if it is less than the timeout variable then print as per the requiremnets
                obj=str(key)+":"+str(a[0])
                print (obj)
                print("\n")
            else:
                print("Key expired \n") # if the time is greater than timeout then it means the key is expired


def delete():
    key = input("enter a key: ")
    # if key is not present in the dictionary then print the following statement
    if key not in dic:
        print("\nInvalid key. Key is not present ")
    else:
        a=dic[key]
        if (a[1]==0):#if timeout is zero we can delete the key
            del dic[key]
            print("\nKey deleted\n ")
        else:
            if (time.time() < a[1]): # if there is a timeout then we need to compare with the present time and if it is less than the timeout variable then delete it
                del dic[key]
                print("\nKey deleted \n")
            else:
                print("\nKey expired\n ") # if the time is greater than timeout then it means the key is expired


n = int(input("\nEnter number of threads: "))

if n==1:
    print("\n\nSingle threading process!!!")
    val = int(input("Enter 1.CREATE     2.READ        3.DELETE         "))
    if val == 1:
        create()
    elif val==2:
        read()
    else:
        delete()
else:
    print ("\n\nMultiple Threading process!!!")
    for i in range(n):
        val = int(input("Enter 1.CREATE     2.READ        3.DELETE       "))
        if val == 1:
            d1= threading.Thread(target=(create),args =())
            d1.start()
            d1.join()  
        elif(val==2):
            d2= threading.Thread(target=(read),args =())
            d2.start()
            d2.join()
        else:
            d3= threading.Thread(target=(delete),args =())
            d3.start()
            d3.join()

    

print ("\n\nIMPLEMENTATION SUCCESS!!!!!")


