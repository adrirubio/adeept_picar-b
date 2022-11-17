
from socket import *
import speech_recognition as sr
import pyttsx3
import threading as thread

recorder = sr.Recognizer()
engine = pyttsx3.init()
ip_stu = 1 #'1' means disconnected 

def connection_thread():
    global Switch_3, Switch_2, Switch_1, function_stu
    while 1:
        car_info = (tcpClicSock.recv(BUFSIZ)).decode()
        if not car_info:
            continue
        elif 'Switch_3_on' in car_info:
            Switch_3 = 1

        elif 'Switch_2_on' in car_info:
            Switch_2 = 1

        elif 'Switch_1_on' in car_info:
            Switch_1 = 1

        elif 'Switch_3_off' in car_info:
            Switch_3 = 0

        elif 'Switch_2_off' in car_info:
            Switch_2 = 0

        elif 'Switch_1_off' in car_info:
            Switch_1 = 0

        elif 'U:' in car_info:
            print('ultrasonic radar')
            #new_number2view(30,290,car_info)

        elif 'function_1_on' in car_info:
            function_stu = 1

        elif 'function_2_on' in car_info:
            function_stu = 1

        elif 'function_3_on' in car_info:
            function_stu = 1

        elif 'function_4_on' in car_info:
            function_stu = 1

        elif 'function_5_on' in car_info:
            function_stu = 1

        elif 'function_6_on' in car_info:
            function_stu = 1

        elif 'CVFL_on' in car_info:
            function_stu = 1

        elif 'CVFL_off' in car_info:
            function_stu = 0

        elif 'function_1_off' in car_info:
            function_stu = 0

        elif 'function_2_off' in car_info:
            function_stu = 0

        elif 'function_3_off' in car_info:
            function_stu = 0

        elif 'function_4_off' in car_info:
            function_stu = 0

        elif 'function_5_off' in car_info:
            function_stu = 0

        elif 'function_6_off' in car_info:
            function_stu = 0

        elif 'CVrun_on' in car_info:
            print("CVrun_on")

        elif 'CVrun_off' in car_info:
            print("CVrun_off")

        elif 'police_on' in car_info:
            print("police_on")

        elif 'police_off' in car_info:
            print("police_off")

        elif 'rainbow_on' in car_info:
            print("rainbow_on")

        elif 'rainbow_off' in car_info:
            print("rainbow_off")

        elif 'sr_on' in car_info:
            print("sr_on")

        elif 'sr_off' in car_info:
            print("sr_off")

def socket_connect():    #Call this function to connect with the server
    global ADDR,tcpClicSock,BUFSIZ,ip_stu,ipaddr
    ip_adr="192.168.1.29"

    SERVER_IP = ip_adr
    SERVER_PORT = 10223   #Define port serial 
    BUFSIZ = 1024        #Define buffer size
    ADDR = (SERVER_IP, SERVER_PORT)
    tcpClicSock = socket(AF_INET, SOCK_STREAM) #Set connection value for socket

    for i in range (1,6): #Try 5 times if disconnected
        #try:
        if ip_stu == 1:
            
            engine.say("connecting to rover")
            engine.runAndWait()
            print("Connecting to server @ %s:%d..." %(SERVER_IP, SERVER_PORT))
            print("Connecting")
            tcpClicSock.connect(ADDR)       #Connection with the server
            
            engine.say("connected to rover")
            engine.runAndWait()
            print("Connected")
            ip_stu=0                         #'0' means connected

            connection_threading=thread.Thread(target=connection_thread)         #Define a thread for FPV and OpenCV
            connection_threading.setDaemon(True)                             #'True' means it is a front thread,it would close when the mainloop() closes
            connection_threading.start()                                     #Thread starts

            #info_threading=thread.Thread(target=Info_receive)        #Define a thread for FPV and OpenCV
            #info_threading.setDaemon(True)                           #'True' means it is a front thread,it would close when the mainloop() closes
            #info_threading.start()                                   #Thread starts
            break
        else:
            print("Could not connect to rover, trying again!")
            print('Try %d/5 time(s)'%i)
            ip_stu=1
            time.sleep(1)
            continue

    if ip_stu == 1:
        print('Disconnected')


def connect():    #Call this function to connect with the server
    if ip_stu == 1:
        sc=thread.Thread(target=socket_connect) #Define a thread for connection
        sc.setDaemon(True)                    #'True' means it is a front thread,it would close when the mainloop() closes
        sc.start()                            #Thread starts


def loop():
    while True:
        try:
            with sr.Microphone() as source:
                print("Speak:")                                                                                   
                audio = recorder.listen(source)
                print("Recognizing:")
                text = recorder.recognize_google(audio)
                print(text)
                if "Jarvis" in text:
                    print(text)
                    engine.say("sending command to mars rover")
                    if "forward" in text:
                        tcpClicSock.send(('forward').encode())
                        
                    elif "backward" in text:
                        tcpClicSock.send(('backward').encode())
                        
                    elif "left" in text:
                        tcpClicSock.send(('left').encode())
                        
                    elif "right" in text:
                        tcpClicSock.send(('right').encode())
                    
                    elif "up" in text:
                        tcpClicSock.send(('up').encode())
                        
                    elif "down" in text:
                        tcpClicSock.send(('down').encode())
                    
                    elif "lookleft" in text:
                        tcpClicSock.send(('lookleft').encode())
                    
                    elif "lookright" in text:
                        tcpClicSock.send(('lookright').encode())
                    
                    elif "stop" in text:
                        tcpClicSock.send(('stop').encode())
                        
                    elif "home" in text:
                        tcpClicSock.send(('home').encode())
                else:
                    engine.say("could you repeat that?")
                        
                    
                engine.runAndWait()
                
        except sr.UnknownValueError:
            print("UnknownValueError")
            pass
        except sr.RequestError:
            print("RequestError")    



if __name__ == '__main__':
    connect()
    loop()
