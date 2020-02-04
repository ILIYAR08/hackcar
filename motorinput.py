import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
while True:
    input1=input('put in a word: ')
    if input1=='back':
        
        
       
        
       
        
        GPIO.output(3, True)    #motor 1
        GPIO.output(5, False)   #motor 1
        
        GPIO.output(7, True)    #enable motor 1
        sleep(.5)
        GPIO.output(3, False)
        GPIO.output(5, False) #disable motor 1
        GPIO.output(7, False)
        

    else:
        if input1=='go':
            
            GPIO.output(3, False)    
            GPIO.output(5, True)   
            GPIO.output(7,True)
           
            sleep(.5)
            GPIO.output(3, False)
            GPIO.output(5, False)
            GPIO.output(7,False)
        else:
            if input1=='right':
                GPIO.output(3, False)    #motor 1
                GPIO.output(5, True)   #motor 1
                GPIO.output(7, True) 
                GPIO.output(11, True)    #motor 1
                GPIO.output(13, False)   #motor 1
                GPIO.output(15, True) 
                sleep(.5)
                GPIO.output(3, False)
                GPIO.output(5, False) #disable motor 1
                GPIO.output(7, False)
                GPIO.output(11, False)    #motor 1
                GPIO.output(13, False)   #motor 1
                GPIO.output(15, False) 
            else:
                if input1=='left':
                    GPIO.output(3, False)    #motor 1
                    GPIO.output(5, True)   #motor 1
                    GPIO.output(7, True) 
                    GPIO.output(11, False)    #motor 1
                    GPIO.output(13, True)   #motor 1
                    GPIO.output(15, True) 
                    sleep(.5)
                    GPIO.output(3, False)
                    GPIO.output(5, False) #disable motor 1
                    GPIO.output(7, False)
                    GPIO.output(11, False)    #motor 1
                    GPIO.output(13, False)   #motor 1
                    GPIO.output(15, False) 
GPIO.cleanup()

            
            
        
        