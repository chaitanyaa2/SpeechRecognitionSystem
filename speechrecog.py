
import speech_recognition as sr
import webbrowser as wb
r1=sr.Recognizer()
#to take verbal input
with sr.Microphone() as source:
  print('Say something\n[say VIDEO if you wanna search something on Youtube]')
  print('speak now!')
  audio=r1.listen(source)
  try:
      text = r1.recognize_google(audio)
  except:
      print("Sorry, could'nt catch that!")
#to search a video
if 'video' in r1.recognize_google(audio):
  print('You said: VIDEO')
  r1=sr.Recognizer()
  url='https://www.youtube.com/results?search_query='
  with sr.Microphone() as source:
      print('search your video!\n Speak now!')
      audio=r1.listen(source)
      #try-except block
      try:
          get=r1.recognize_google(audio)
          print(get)
          wb.get().open_new(url+get)
      except sr.UnknownValueError:
          print('error')
      except sr.RequestError as e:
          print('failed to get results'.format(e))
#speech to text convert
else:
  print('You said :',text)
