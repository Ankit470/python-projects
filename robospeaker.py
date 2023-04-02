#there is no feature for windows to directly convert the text from terminal to speech 

#it is for mac OS 

import os 
print("welcome to robospeaker")
while True:
    x = input("enter what you want me to speak ")
    if x =='q':
        break
    command = f"say {x}"
    os.system(command)