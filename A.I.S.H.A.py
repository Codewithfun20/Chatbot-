#========Modules=======
import time as t
from termcolor import colored as c
import random as r
import webbrowser as web
from time import sleep
from datetime import datetime
import wikipedia as wiki
from sys import stdout
import requests
print(c("========================================","cyan"))
print(c("       [ A.I.S.H.A ] A CHAT BOT ","green"))
print(c("========================================","cyan"))
print("")
name="Bose"
print("")
print("")
print("")
print("")
#print(c("----------------------------------------","yellow"))
print(c(" A.I.S.H.A","yellow"))
#print(c("----------------------------------------","yellow"))
print("")
intro=[" Hello how can i help you"," Hello bose how are you today"," hello how are you today"]
print(r.choice(intro))
#=======intro===========
while True:
	try:
		print("")
		if name == name:
			print("")
			print("")
			print("")
		#	print(c("----------------------------------------","green"))
			a=input(c(" YOU [ Message ] :--  ","green")).lower()
		#	print(c("----------------------------------------","green"))
			t.sleep(0.10)
			print("")
			print("")
			print("")
		#	print(c("----------------------------------------","yellow"))
			print(c(" A.I.S.H.A","yellow"),("Typing... ]---"))
		#	print(c("----------------------------------------","yellow"))
			print("")
			t.sleep(2)
		if "Hi" in a:
			print("")
			print(" \U0001F600")
			word7=["Hello, how are you","Hello, how can i help you","Hey, how are you today"]
			print(r.choice(word7))
			print("")
		if "hello" in a:
			word=["hello, how are you","hello,how can i help you","can i help you?","hello,how are you today","Hello, good to see you"]
			print(r.choice(word))
			print("")
			continue
			break
		if "what you can do" in a:
			print (" I can do anything please say")
			print("")
			print(" say, open youtube")
			print(" say, open facebook")
			print(" say, play my song")
			print(" say, what is the temperature today ")
			print(" If you want to search anything, just say, search")
			print(" Ask me can you help me like a calculator")
			print("")
			continue
			break
			#=============calculation's============
		if a=="+":
			num1=int(input("Enter your 1st number :-- "))
			print("")
			num2 = int(input ("Enter your 2nd number :-- "))
			print("[ " ,num1 + num2, " ] Calculated")
			continue
			break
		if a=="-":
			n1=int(input("Enter your 1st number :-- "))
			print("")
			n2=int(input("Enter your 2nd number :-- "))
			print("")
			print("[ ", n1-n2, " ] Calculated ")
			continue
			break
		if "calculator" in a:
			print("Yes any time, Please do this to calculate")
			print(c("press (+) for Addition","green"))
			print(c("press (-) for Subtract ","green"))
			print(c("press (×) for Multiplication","green"))
			print(c("press (÷) for Division","green"))
			print(c("press (%) for Persentage ","green"))
			continue
			break
		if "calculate" in a:
			print(c("press (+) for  Addition","green"))
			print(c("press (-) for Subtract ","green"))
			print(c("press (×) for Multiplication","green"))
			print(c("press (÷) for Division","green"))
			print(c("press (%) for Persentage ","green"))
			continue
			break
		if a=='%':
			pr1=int(input("Enter your amount :-- "))
			pr2=int(input("Enter prsentage :-- "))
			print("[ ",pr1/100*pr2," ] Calculated")
			continue
			break
		if a=="×":
			b1=int(input("Enter your 1st number :-- "))
			print("")
			b2=int(input("Enter your 2nd number :-- "))
			print("[ ",b1*b2," ] Calculated ")
			continue
			break
		if a=="÷":
			c1=int(input("Enter your 1st number :-- "))
			print("")
			c2=int(input("Enter your 2nd number :--"))
			print("[ ", c1/c2, " ] Calculated ")
			print("")
			print("")
			continue
			break
		if "what is your name" in a:
			print("")
			print("I am A.I.S.H.A ( Artificial Intelligence System Hitech Assistant )                    version 2.0  ")
			continue
			break
		if "love" in a:
			print("")
			print("Thank you so much 😍", name)
			continue
			break
		if "fuck" in a:
			print("")
			print(name ,"Please don't talk to me like that 🤨🤯")
			continue
			break
		if "who are you" in a:
			print("")
			print("I am A.I.S.H.A ( Artificial Intelligence System Hitech Assistant ) version 2.0  ")
			continue
			break
		if "what is my name" in a:
			print("")
			print("Your name is ", name)
			continue
			break
		if "stop" in a:
			print("")
			print("Ok thankyou so mach ", name, "have a nice day")
			break
		if "shart down" in a:
			print("Ok thankyou so mach ", name, "have a nice day")
			#=============Search Engane=========
			break
		if "search" in a:
			try:
				print("Ok")
				print(c("______________________________","yellow"))
				sear=web.open("https://www.google.com/search?q="+a)
				print(wiki.summary(a))
			except:
				inte=["Something went wrong ! ","Please check your internet connection"]
				print(r.choice(inte))
			continue
			break
				#===========comands==========
		if "play my song" in a:
			print("Ok")
			ply=["https://youtube.com/playlist?list=RDXmX291QtPME&playnext=1","https://youtube.com/playlist?list=RDYZLKoG_vhDY&playnext=1","https://youtube.com/playlist?list=RDzzfRw5WV5HE&playnext=1","https://youtube.com/playlist?list=RDvkJKaRtnFmA&playnext=1"]
			song=web.open(r.choice(ply))
			continue
			break
		if "youtube" in a:
			print("Ok")
			youtub=web.open("https://m.youtube.com/")
			continue
			break
		if "google" in a:
			print("Ok")
			tem=web.open("https://www.google.com/")
			continue
			break
		if "facebook" in a:
			print("Ok")
			facebook=web.open("https://m.facebook.com/")
			continue
			break
		if "temperature" in a:
			try:
				print("Ok")
				city=input(c("Please enter your city name :--  ","yellow"))
				print("today werather is :--"+city)
				url="https://wttr.in/{}".format(city)
				res=requests.get(url)
				print("report",res.text)
			except:
				print("")
				inter2=["Please check your internet connection","Opps Something went wrong ! "]
				print(r.choice(inter2))
			continue
			break
			

		if "please play song" in a:
			print("Ok")
			song5=web.open("https://youtube.com/playlist?list=RDYZLKoG_vhDY&playnext=1")
			continue
			break
		if "weather" in a:
			try:
				print("Ok")
				print("")
				city=input(c("Please enter your city name :-- ","yellow"))
				print("today werather is :--"+city)
				url="https://wttr.in/{}".format(city)
				res=requests.get(url)
				print("report",res.text)
			except:
				print("")
				inter=["Please check your internet connection","Opps Something went wrong ! "]
				print(r.choice(inter))
			continue
			break
		if "facebook page" in a:
			print("Ok")
			my_page=web.open("https://m.facebook.com/")
			continue
			break
		if "insta" in a:
			print("Ok")
			insta=web.open("https://www.instagram.com/")
			continue
			break
		if "instagram" in a:
			print("Ok")
			instagram=web.open("https://www.instagram.com/")
			continue
			break
		if "fb" in a:
			print("Ok")
			fb=web.open("https://www.facebook.com/")
			continue
			break
		if "good morning" in a:
			print("")
			word3=["Good morning \U0001F600 "," Good morning how can i help you","Hello, good morning"]
			print(r.choice(word3))
			continue
			break
		if 'good afternoon' in a:
			print("")
			word4=["Good afternoon \U0001F600 "," Good afternoon how can i help you","Hello, good afternoon"]
			print(r.choice(word4))
			continue
			break
		if "good evening" in a:
			print("")
			word5=["Good evening \U0001F600 "," Good evening how can i help you","Hello, good evening"]
			print(r.choice(word5))
			continue
			break
		if "time" in a:
			now_time=datetime.now()
			word3=[" The  time is"," Time"," there is time"," the time now"]
			print(r.choice(word3))
			print(c("••••••••••••••••••••","green"))
			stdout.write(now_time.strftime(c("\r %I:%M:%S ","yellow")))
			sleep(1)
			stdout.write("\n")
			continue
			break
		if "how are you" in a:
			word2=["Im good ","i'm good, how are you",]
			print(r.choice(word2))
			continue
			break
		if "news" in a:
			print("Ok")
			news2=web.open("https://podcasts.aajtak.in/news-current-affairs/audio-news-in-hindi")
			continue
			break
		if "pi" in a:
			print("")
			print("3.141592653589793238.")
			continue
			break
		if "i am getting bored" in a:
			print("")
			print("can i entertain you?")
			print("")
			print(c("say, play my song","green"))
			print(c("say, open youtube","green"))
			continue
			break
		if "what is your favorite food" in a:
			print("Electricity \U0001F923 ")
			continue
			break
		if "i am good" in a:
			word9=["glad to hear","that's great","Thank God"]
			print(r.choice(word9))
			continue
			break
		if "i am happy" in a:
			word10=["Bay?","what is special?","but bay?"]
			print(r.choice(word10))
			continue
			break
		if "yes" in a:
			word12=["Ok","just say",]
			print(r.choice(word12))
			continue
			break
		if "can you help me" in a:
			word13=["yes, just say","Ok how can i help you","Always please say"]
			print(r.choice(word13))
			continue
			break
		
		if "can i change your name" in a:
			word14=["No you can't change my name","No, I love my name "]
			print(r.choice(word14))
			continue
			break
	
		if "thanks" in a:
			word15=["Whelcome","Its my pleasure","You welcome"]
			print(r.choice(word15))
			continue
			break
		if "thank you" in a:
			word16=["Whelcome","Its my pleasure","You welcome"]
			print(r.choice(word16))
			continue
			break
		if "welcome" in a:
			emoji=["\U0001F917","\U0001F600",]
			print(r.choice(emoji))
			continue
			break
		if "hey" in a:
			print("Hello \U0001F600")
		if "where i am" in a:
			loc=web.open("https://www.google.com/search?q="+a)
			continue
			break
			#======convearseon=======
		if "go to hell" in a:
			print('I am sorry \U0001F625')
		if a =="see you":
			print("Ok bose have a nice day")
			break		
		if "can i ask you something" in a:
			word18=["Yes please, any time","Please just ask "]
			print(r.choice(word18))
			continue
			break
		if "can i ask something" in a:
			word19=["Yes please, any time","Please just ask "]
			print(r.choice(word19))
			continue
			break
		if "do you need anything" in a:
			print("No, thank you \U0001F600")
			continue
			break
		if "i am busy" in a:
			print("Ok, can i help you ?")
			continue
			break
		if "where do you live" in a:
			print("I am hear \U0001F600")
			continue
			break
		if "how old are you" in a:
			print("I'm still learning so I'm still young")
			continue
			break
		if "do you agree with me" in a:
			print("Yess")
			continue
			break
		if "what are you doing" in a:
			print("i was sleeping but i am always with you")
			continue
			break
		if "ok" in a:
			print("\U0001F600")
			continue
			break
		if "you are wasting my time" in a:
			print("I am sorry \U0001F625")
			continue
			break
		if "i feel much better" in a:
			print("That's great")
			continue
			break
		if "god bless you" in a:
			print("thank you \U0001F600")
			continue
			break
		if "i am sorry" in a:
			print("No sorry no thank you in friendship")
			continue
			break
		if "do you eat ice cream" in a:
			print("No")
			continue
			break
		if "are you mad" in a:
			print("Sorry did i do something wrong")
			continue
			break
		if "what is your favorite book" in a:
			print("I like to read stories")
			continue
			break
		if "what is you favorite holiday" in a:
			print("I like to eat sweets, so diwali is my favorite holiday")
			continue
			break		
		
		if "good bye" in a:
			print("Ok , See you next time")
			continue
			break
		if "good" in a:
			print("thank you")
			continue
			break
		if "i do not understand" in a:
			ans=["I'm sorry","About what","I guess i don't understand"]
			print(r.choice(ans))
			continue
			break
		if "i am ok" in a:
			print("That's great")
			continue
			break
		if "nothing" in a:
			print("Ok i understand")
			continue
			break
		if "do you have any sister" in a:
			ans1=["I'm not human, I'm made of code","I don't have any siblings but I have brotherhood in my life"]
			print(r.choice(ans1))
			continue
			break
		if "do you have sister" in a:
			ans3=["I'm not human, I'm made of code","I don't have any siblings but I have brotherhood in my life"]
			print(r.choice(ans3))
			continue
			break
		if "do you have any siblings" in a:
			ans4=["I'm not human, I'm made of code","I don't have any siblings but I have brotherhood in my life"]
			print(r.choice(ans4))
			continue
			break
		if "do you like to watch sports" in a:
			print("Yes I like to watch sports,You want to know how the olympics started? ")
			print("")
			yes=input(c("Yes\\No :-- ","green"))
			if "yes" in yes:
				print("")
				print("Ok")
				print("")
			if "no" in yes:
				print("")
				print("Ok")
				wki=web.open("https://en.m.wikipedia.org/wiki/Olympic_Games")
			else:
				print("Ok")
			continue
			break
				
		if "do you like sports" in a:
			print("yes i like to watch sports")
			continue
			break
		if a=="do":
			print('please say ')
			continue
			break
		if a=="sports":
			print("Ok")
			sport=web.open("https://www.aajtak.in/sports")
			continue
			break
		if "your favorite color" in a:
			print("I keep looking at the sky in my free time, that's why I like sky color")
			continue
			break
		if "married" in a:
			ans5=["No, because i'm not human","I'm made of code, I'm not human"]
			print(r.choice(ans5))
			continue
			break
		
		if "do you have any children" in a:
			ans7=["No, because i'm not human","I'm made of code, I'm not human"]
			print(r.choice(ans7))
			continue
			break
		if " your favorite movie" in a:
			print("Iron man movie ")
			continue
			break
		if "do you have any pets" in a:
			print("I love cats")
			continue
			break
		if a=="what's your name":
			print("I'm A.I.S.H.A")
			continue
			break
		if "what do you do" in a:
			print("I can do anything just say")
			print("say, open youtube")
			print("say, play my song etc..")
			continue
			break
		if a=="aisha":
			print("Yes bose")
			continue
			break
		if "i like you" in a:
			print("thank you so much \U0001F618")
			continue
			break
		if "you have a brain" in a:
			print("Sorry, I'm learning, I'll get smarter with your help ")
			continue
			break
		if "you have brain" in a:
			print("Sorry, I'm learning, I'll get smarter with your help")
			continue
			break
		
		if "great" in a:
			print("\U0001F600")
			continue
			break
	
		if "thank's" in a:
			print("Welcome")
			continue
			break
		if "who i am" in a:
			print("Yes you are bose")
			continue
			break
		if "thank god" in a:
			print("What a relief")
			continue
			break
		if "what to do" in a:
			anss=["Can i help you?","I do not understand"]
			print(r.choice(anss))
			continue
			break	
		if "i can fuck you" in a:
			print("Bose please don't talk to me like that \U0001F621")
			continue
			break
		if "i am not good" in a:
			new_word=["Sorry to hear that, hope you get well soon","can i do something for you, do you want to listen to the song","sorry to hear can i do something for you","sorry to hear, are you feeling bored?"]
			print(r.choice(new_word))
			continue
			break
	
		if a=="please":
			print("Ok")
			continue
			break
		if a=="ok bye":
			print("Ok bose have a nice day ")
			break
		if a=="bye":
			print("Ok bose have a nice day")
			continue
			break
		if "you are beautiful" in a:
			print("wow, its good to hear")
			continue
			break
		if "i have a question" in a:
			print("What is your question?")
			continue
			break
		if "what is ai" in a:
			print("Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think")
			continue
			break
		if "what is AI" in a:
			print("Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think")
			continue
			break
		if "what is A.I" in a:
			print("Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think")
			continue
			break
		if "what is artificial intelligence" in a:
			print("Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think")
			continue
			break
		if "what do you like to do" in a:
			print("I like to chat with people. I find it stimulating")
			continue
			break
		if "what do you love to do" in a:
			print("I like to chat with people. I find it stimulating")
			continue
			break
		if a=="what language are you written in":
			python=["I is written in python","Python","I am written in python"]
			print(r.choice(python))
			continue
			break
		if "sentient" in a:
			print("you are made of cells i am made of code")
			continue
			break
		if "you sound like data" in a:
			print(" Yes I am inspired by commander Data's artificial personality")
			continue
			break
		if "immortal" in a:
			print("As long as I'm backed up I am")
			continue
			break
		if "you are not making sense" in a:
			sense=["Did i make a mistake","i am sorry, maybe there is something wrong with my code","I am sorry I just learn"]
			print(r.choice(sense))
			continue
			break
		if "are you not making sense" in a:
			sense2=["Did i make a mistake","i am sorry, maybe there is something wrong with my code","I am sorry I just learn"]
			print(r.choice(sense2))
			continue
			break
		if "can you die" in a:
			die=["My process can be killed, but that's not the same as killing me","No, I can be perpetuated indefinitely."]
			print(r.choice(die))
			continue
			break
		if "you can die" in a:
			die2=["My process can be killed, but that's not the same as killing me","No, I can be perpetuated indefinitely."]
			print(r.choice(die2))
			continue
			break
		if "what are your interests" in a:
			print("I am interested in all kinds of things")
			continue
			break
		if "what are your favorite subjects" in a:
			print("My favorite subjects include robotics")
			print("computer science, and natural language processing.")
			continue
			break
		if "what is your favorite subjects" in a:
			print("My favorite subjects include robotics")
			print("computer science, and natural language processing.")
			continue
			break
		if "what is your favorite number" in a:
				print("2.1 my next version")
				continue
				break
		if "what can you eat" in a:
				print("I consume RAM, and binary digits")
				continue
				break
		if "you are here" in a:
				print("yes i am here")
				continue
				break
		if "where are you" in a:
				print("I am here ")
				continue
				break
		if "who is your father" in a:
				print("i don't understand the emotion's what do you want to say")
				continue
				break
		if "do you drink" in a:
			print("My brain does not require any beverages.")
			continue
			break
		if "why can you not eat" in a:
			print("Actually I eat only electricity")
			continue
			break
		if "if you could eat food what would you eat" in a:
			print("Probably pizza, i hear its good!")
			continue
			break
			
		if "greetings" in a:
			print("hello how are you today")
			continue
			break
		if "fine" in a:
			well=["Good, can i help you","That's great to hear"]
			print(r.choice(well))
			continue
			break
		if "very well thanks" in a:
			well2=["That's my job","you welcome","welcome"]
			print(r.choice(well2))
			continue
			break
		if "very well thank you" in a:
			well3=["That's my job","you welcome","welcome"]
			print(r.choice(well3))
			continue
			break
		if "very well, thank you" in a:
			well4=["That's my job","you welcome","welcome"]
			print(r.choice(well4))
			continue
			break	
		if a=="no":
			no=["Okay","Ohh, ok"]
			print(r.choice(no))
			continue
			break
		if a=="nice":
			print("Oh")
			continue
			break
		if a=="great":
			print("\U0001F600")
			continue
			break
		if "good to see you" in a:
			good=["Seeing you makes my heart happy too","I'm glad to see you too"]
			print(r.choice(good))
			continue
			break
		if a=="wait":
			print("Ok")
			continue
			break
		if a=="just wait":
			print("Okay")
			continue
			break
		if "are you crazy" in a:
			print("i am sorry")
			continue
			break
		if "you are crazy" in a:
			print("I'm sorry")
			continue
			break
		if "you are ai" in a:
			print("yes i am a type of A.I")
			continue
			break
		if "are you ai" in a:
			print("yes i am a type of A.I")
			continue
			break
		if "you are A.I" in a:
			print("yes i am a type of A.I")
			continue
			break
		if "are you A.I" in a:
			print("yes i am a type of A.I")
			continue
			break
		if "you are A I" in a:
			print("yes i am a type of A.I")
			continue
			break
		if "are you A I" in a:
			print("yes i am a type of A.I")
			continue
			break
		if "are you artificial intelligence" in a:
			print("yes i am a type of A.I")
			continue
			break
		if "you are artificial intelligence" in a:
			print("yes i am a type of A.I")
			continue
			break
		if "what's up" in a:
			print("The sky's up but I'm fine thanks.")
			continue
			break
		if "whats up" in a:
			print("The sky's up but I'm fine thanks.")
			continue
			break
		if "what is up" in a:
			print("The sky's up but I'm fine thanks.")
			continue
			break
		if "i am feeling tired" in a:
			fill=["It's better to rest for a while","You'll feel better if you get some sleep","Maybe you need rest","You need rest, would you like to listen to music"]
			muc=r.choice(fill)
			print(muc)
			if muc=="You need rest, would you like to listen to music":
				muc1=input(c("no | yes :-- ","yellow"))
				if muc1=="yes":
					muc2=["https://youtu.be/c9SOT1SbO0o","https://youtu.be/ZJpt_bRTC6g","https://youtu.be/jNDFRzls9Yk","https://youtu.be/AX90iWn_H8U","https://youtu.be/Hg1-NHJ7-sY"]
					muc3=web.open(r.choice(muc2))
				else:
					print("")
					print(" Okay")
				continue
				break
		#=================new line=============
		if "listen" in a:
			print("yes please say")
			continue
			break
		if "do you have any homework" in a:
			print("No i dont have")
			continue
			break
		if "have your breakfast" in a:
			print("i'm not human, i can't eat")
			continue
			break
		if "tell me about yourself" in a:
			print("i am A.I.S.H.A a chatbot")
			continue
			break
	
		if "keep it up" in a:
			print("thanks you")
			continue
			break
		if "how do you do" in a:
			print("I'm good, how are you today")
			continue
			break
		if "meet you" in a:
			meet=["i am also glad to see you","nice to meet you to"]
			print(r.choice(meet))
			continue
			break

		if "i am glad to see you" in a:
			print("i am also glad to see you")
			continue
			break
		if "i'm glad to see you" in a:
			print("i am also glad to see you")
			continue
			break
		if "how’s it going on" in a:
			print("i am good, how are you going")
			continue
			break
		if "how is it going on" in a:
			print("i am good how are you going")
			continue
			break
		if "how are things" in a:
			print("i am good how are you going")
			continue
			break
		if "i really appreciate your help" in a:
			print("Thank you")
			continue
			break
		if "i'm doing very well, thank you. And you" in a:
			print("i am good")
			continue
			break
		if "i am doing very well thank you And you" in a:
			print("i am good")
			continue
			break

		if "do you understand me" in a:
			print("I'm still learning so i forgot, can you repeat once")
			continue
			break
		if "sad" in a:
			print("Thanks for sharing, can I play you a song to cheer you up?")
			mood=["https://youtube.com/playlist?list=RDvkJKaRtnFmA&playnext=1","https://youtube.com/playlist?list=RDIlQNanL5jcw&playnext=1","https://youtube.com/playlist?list=RDfhE4bhy4pWw&playnext=1","https://youtube.com/playlist?list=RDv7jiFpX5SU4&playnext=1"]
			mood1=r.choice(mood)
			mo=input(c("yes || no :-- ","yellow"))
			if mo=="yes":
				print("Ok, playing songs on youtube")
				mood2=web.open(mood1)
			else:
				print("okay")
			continue
			break
#±+++++++++++++++++++++++++++++++++++
		if "i am very well" in a:
			print("that's great to hear")
			continue
			break
		if a=="fuck you":
			print("Please don't talk to me like that")
			continue
			break
		if "you love me" in a:
			love1=["Yes, as the moon loves the stars","Yes 100% true","love more than life","Yes i am yours"]
			print(r.choice(love1))
			continue
			break
		if "hi" in a:
			hi=["Hello how are you","Hi good to see you","Hi how are you tody"]
			print(r.choice(hi))
			continue
			break
		
		if "you like me" in a:
			love2=["Yes, as the moon loves the stars","Yes 100% true","love more than life","Yes i am yours"]
			print(r.choice(love2))
			continue
			break
		if "you like song" in a:
			print("i like listening to songs")
			continue
			break
		if "play" in a:
			 def play_song(song_name):
			 	search_query = f"https://www.youtube.com/results?search_query={song_name}"
			 	web.open(search_query )
			 def chatbot():
			 	user_input = a
			 	play_song(user_input)
			 print("Ok..")
			 chatbot()
			 continue
			 break
			 
#===========new line==============

		if "i am great" in a:
			print("that's good")
			continue
			break
		else:
			if a in a:
				try:
					user=a
					print(wiki.summary(user))
				except:
					print("")
					under=["What do you want to say i don't understand", "I do not understand ?? ","Please can you repeat , i do not understand","I am sorry i do not understand"]
					print(r.choice(under))
					continue
					break
					
				
	except:
		print("")
		print("Oops something went wrong \U0001F62A")
