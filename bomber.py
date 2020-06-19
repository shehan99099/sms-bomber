import urllib.request
import json
import requests
import os
import urllib
import sys
import time

os.system('clear')

bar = "\033[1;33;40m\n_________________________________________________\n"
name = ""



print("\033[0;36m "" ///////       ////    ////   ////////               ////////////   //////////  //////////  //")
print("\033[0;36m "" //           // //  // //    //                          //        //      //  //      //  //")                                                 
print("\033[0;36m "" //          //   //   //     //                          //        //      //  //      //  //")
print("\033[0;36m "" ///////    //        //      ////////                    //        //      //  //      //  //")                                                              
print("\033[0;36m ""      //   //        //             //                    //        //      //  //      //  //")                                                           
print("\033[0;36m ""      //  //        //              //                    //        //      //  //      //  //")                                                                     
print("\033[0;36m "" /////// //        //         ////////                    //        //////////  //////////  //////////")
print("\033[0;35m ""                                          [TOOL BY MEGARUN] ")
print("")
print("\033[1;33m ""#YOU CAN SEND 10 MESSAGE ONLY ONE NUMBER")
print("\033[0;32m ""#OUT PUT = 200  message was sent successfully")
print("\033[1;31m ""#OUT PUT = 400  LIMITED ")
print("")
print("")

number = int(input("\033[1;37m""@ Enter phone number with international format (94xxxxxxxxx) - "))


def main():
    os.system("clear")
    print("\n\n") 
    s = int(input("\033[1;0;40mEnter Amount - "))



url : 'https://api.getshoutout.com/coreservice/messages',

method : 'POST',

headers : {

'Content-Type' : 'application/json',

'Authorization' : 'Apikey xxxxx.xx.xx.xxxx',

},

body : JSON.stringify({

"source" : "ShoutDEMO",

"destinations" : ["number"],

"transports" : ["sms"],

"content" : {

"sms" : "Sent via ShoutOUT Lite"

},

}),


    

    ss = 0
    while s > ss:
        os.system("clear")
        print(name)
        size = 0
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        resp = str(r)
        if resp == '<Response [200]>':
            print("200 success")
        elif resp == '<Response [204]>':
            print("204  limited")
        else:
            print("\033[1;31m ""something wrong please try again")

        ss+=1
        print("\033[1;0;40m\n",str(ss), end="")
        for i in range(180):
            
            pr = i/180*1000
            print("\033[1;36;40m\n>>>",str(int(pr)) +"% ",end="")
            
            time.sleep(0.002)
            sys.stdout.write("\033[F")


    os.system('')
    again()


def again():
    again = input(' (y/n) - ')
    if again == "y" or again == "Y":
        os.execl(sys.executable, sys.executable, * sys.argv)
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
