import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Welcome to simple Calculator")
print (":::::::SIMPLE CALCULATOR :::::::") 

# IMPUT NUMBERS AND OPERATION 
speak("Enter first number:")
a = float ( input ( " Enter first number : " ))
speak("Enter second number:")
b = float ( input ( " Enter second number : " ))
speak("Enter the operation:")
c = str (input ( " Enter the operation : (+,-,*,/,//,**) : " ))

# defining operation for python to understand 

if c ==  "+" :
    print ("sum of",a,"and" ,b, "is" , a+b) 
    speak("sum of")
    speak (a)
    speak("and")
    speak(b)
    speak("is")
    speak(a+b)


elif c == "-" :
    print ("difference of",a,"and" ,b, "is" , a-b) 
    speak("difference of ")
    speak (a)
    speak("and")
    speak(b)
    speak("is")
    speak(a-b)

elif c == "*" :
    print ("product of",a,"and" ,b, "is" , a*b) 
    speak("product of ")
    speak (a)
    speak("and")
    speak(b)
    speak("is")
    speak(a*b)

elif c == "/" :
    print (a,"divided by " ,b, "is" , a/b) 
    speak(a)
    speak ("divided by")
    speak(b)
    speak("is")
    speak(a/b)
    
elif c == "**" :
    print (a,"to the power" ,b, "is" , a**b) 
    speak (a)
    speak("to the power")
    speak(b)
    speak("is")
    speak(a**b)

elif c == "//" :
    print ("floor quotient of",a,"and" ,b, "is" , a//b) 
    speak("floor quotient of ")
    speak (a)
    speak("and")
    speak(b)
    speak("is")
    speak(a//b)

else:
    speak ("Undefined Operation")
    print ("UNDEFINED OPERATION")
    
