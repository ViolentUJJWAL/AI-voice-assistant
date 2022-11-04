import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import wikipedia
from playsound import playsound
import psutil
import requests,json,time



engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
aivoice=input("1 for Male Voice\n2 for Female Voice\nVoice..... ")
if aivoice=="2":
	aivoice=1
else:
	aivoice=0
engine.setProperty("voice" , voices[aivoice].id)

def speak(srt):
	engine.say(srt)
	engine.runAndWait()

def wishMe():
	hour=int(datetime.datetime.now().hour)
	if 3<=hour<12:
		print("Good Morning")
		speak('Good Morning')
	elif 12<=hour<=18:
		print('Good Afternoon')
		speak('Good Afternoon')
	else:
		print('Good Evening')
		speak('Good Evening')

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as mic:
		r.operation_timeout=1
		r.adjust_for_ambient_noise(mic)
		print('Listening.....')
		audio = r.listen(mic)

	try:
		print('Recognition.....')
		query= r.recognize_google(audio)
		print(f"User said: {query}\n")

	except Exception as e:
		print(f'Something wrong\n{e}')
		print('Say that again please.....')
		return "None"
	return query

def open(path):
	try:
		os.startfile(path)
	except Exception as e:
		speak("sorry sir i can't open ")


def news(cetegry):
	def news(url):
		getNews=requests.get(url).text
		news=json.loads(getNews)
		return news

	def genUrl(content):
		url=''
		if 'business' in content:
			print("Business News")
			url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c05311dd07454c879a94745debf670e2"
		elif 'entertainment' in content:
			print("Entertainment News")
			url="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=c05311dd07454c879a94745debf670e2"
		elif "health" in content:
			print("Health News")
			url="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=c05311dd07454c879a94745debf670e2"
		elif "science" in content:
			print("Science News")
			url="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=c05311dd07454c879a94745debf670e2"
		elif "sports" in content:
			print("sports news")
			url="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=c05311dd07454c879a94745debf670e2"
		elif "technology" in content:
			print("technology news")
			url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c05311dd07454c879a94745debf670e2"

		Tnews=news(url)
		return Tnews

	try:
		print("\nPlease wait Dawnload News....")
		news=genUrl(cetegry)
		speak("listening carefully")
		for i,a in enumerate(news["articles"]):
			today=f"{a['title']}, \nDescription - \n{a['description']}"
			url=a['url']
			print(f'\n\nNews {i+1} \n{today}')
			print(f'URL- {url}')
			speak(f'News {i+1} {today}')
			if 5==(i+1):
				break;
			time.sleep(1)
	except Exception as e:
		print(e)
		print('sorry sir, no match result')
		speak('Sorry sir, no match result')


if __name__=="__main__":
	while True:
		# start=takeCommand().lower()
		start=input("Enter hello: ")
		if "hello" in start:
			speak('Hello Ujjwal Sir')
			wishMe()
			speak('i am Violent AI. may i halp you')
			while True:
				command=takeCommand().lower()
				# command=input('command: ')
				
				if "open youtube" in command:
					webbrowser.open('https://www.youtube.com/')
					speak('ok sir, open youtube')

				elif "open google" in command:
					webbrowser.open('https://www.google.co.in/')
					speak('ok Sir, open google')

				elif "the time" in command:
					strTime = datetime.datetime.now().strftime("%H:%M:%S")
					print(f'Time {strTime}')
					speak(f"Sir, the time is {strTime}")

				elif "ok exit" in command:
					speak("ok sir, have a nice day")
					exit()

				elif 'your name' in command:
					speak('sir, my name is Violent A I')

				elif 'your owner name' in command:
					speak("sir, my owner name is ujjwal sir")

				elif "play music" in command:
					music_path='C:\\Users\\UJJWAL\\Music'
					song=os.listdir(music_path)
					print(song[7])
					os.startfile(os.path.join(music_path, song[7]))

				elif "wikipedia" in command:
					print('Searching Wikipedia...')
					command=command.replace("wikipedia", '')
					try:
						searchResult=wikipedia.summary(command, sentences=2)
						speak('According to wikipedia')
						print(searchResult)
						speak(searchResult)
					except Exception as e:
						speak("sorry sir no match result")

				elif 'open spotify' in command:
					open("C:\\Users\\UJJWAL\\OneDrive\\Desktop\\Spotify.lnk")

				elif 'open sublime' in command:
					open("C:\\Users\\UJJWAL\\OneDrive\\Desktop\\Sublime Text.lnk")

				elif 'open chrome' in command:
					open("C:\\Users\\Public\\Desktop\\Google Chrome.lnk")

				elif 'open camera' in command:
					open("C:\\Users\\UJJWAL\\OneDrive\\Desktop\\Camera.lnk")

				elif 'open setting' in command:
					open("C:\\Users\\UJJWAL\\OneDrive\\Desktop\\Settings.lnk")

				elif 'open mails' in command:
					open("C:\\Users\\UJJWAL\\OneDrive\\Desktop\\Mail.lnk")

				elif 'open my code' in command:
					open("C:\\Users\\UJJWAL\\OneDrive\\Desktop\\codes")

				elif 'open my project' in command:
					open("C:\\Users\\UJJWAL\\OneDrive\\Desktop\\codes\\my project")

				elif 'open my file' in command:
					open('C:\\Users\\UJJWAL')

				elif 'open users' in command:
					open('C:\\Users')

				elif "open ms word" in command:
					open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk")

				elif "open ms excel" in command:
					open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk")

				elif 'open powerpoint' in command:
					open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")

				elif 'my laptop battery' in command:
					battery=psutil.sensors_battery()
					print(f'Battery percentage : {battery.percent}%')
					speak(f'Battery percentage : {battery.percent} percent,')
					if battery.power_plugged==True:
						speak('plugged in')
					else:
						speak('no plugged in')

				elif "laptop information" in command:
					import subprocess
					Id=subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
					new=[]
					for item in Id:
						new.append(str(item.split('\r')[:-1]))
					for i in new:
						print(i[2:-2])
						if "Host Name:" in i or "OS Name:" in i or "OS Version:" in i or "OS Manufacturer:" in i or "Registered Owner:" in i or "System Manufacturer:" in i: 
							speak(i)

				elif 'news' in command:
					news(command)

				elif "ok back" in command:
					break;

				else:
					speak('sorry sir')


					