#use (py -m install pywin32)

import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    
  text = input("Enter the text to speak")
  if text =='q':
      text = "This program is goint to quit"
      speak.Speak(text)
      break;
  speak.Speak(text)
  