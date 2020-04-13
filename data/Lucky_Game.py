import random
from time import sleep as wait
try: 
	from playsound import playsound
except: pass
        # Function for called file mp3 with playsound module
def voice (mp3):
	try: playsound(mp3)
	except: pass

while True:
	print('\n','<'+'='*16+'>','\n','|  TRY to LUCKY  |','\n','<'+'='*16+'>')
	voice('opening.mp3');wait(1)
	voice('choose.mp3')
	pilihan=input("\n1. What's Your Digit\n2. Coin Guess\n0. Exit\n\n |> Select a Game : ")
	if pilihan == '1':
		while True:
			print('\n','<'+'='*20+'>','\n','|  WHATS YOUR DIGIT  |','\n','<'+'='*20+'>\n')
			voice('welcome.mp3')
			voice('players.mp3')
			# variabel in program
			name,money,player,boundary,guess_player,keluar,ronde,uangTaruhan,uangBandar,start=[],[],[],[],[],False,0,0,0,1
			try:
				players=int(input('How many players will Play? '))
			except:
				wait(1);print('\n'+'='*20,'\nInput ERROR!!')
				voice('error.mp3')
				players=int(input('\nEnter the number of Players in numbers! '));print('='*20,'\n')
			for i in range(players):
				if i == 0: voice('name.mp3')
				else: voice('nextplayer.mp3')
				inputName=input('\n|  >> Enter Name : '.format(i+1));name.append({'name' : inputName});player.append({'player' : str(i+1)});wait(0.5)
				try: 
					inputMoney=int(input('|> How much for your money? '))
					money.append({'money' : inputMoney});wait(1)
				except: 
					wait(1);print('\n'+'='*20,'\nInput ERROR!!')
					voice('ernum.mp3')
					inputMoney=int(input(' >> Input in a Number! '))
					money.append({'money' : inputMoney});print('='*20,'\n');wait(1)
				try: 
					inputBoundary=int(input('| >> How many Round YOu Want? '))
					boundary.append({'bound':inputBoundary})
				except: 
					wait(1);print('\n'+'='*20,'\nInput ERROR!!')
					voice('ernum.mp3')
					inputBoundary=int(input(' >> Input in a Number! '))
					boundary.append({'bound':inputBoundary});print('='*20,'\n')
			wait(1)
			for i in range (len(player)):
				ronde += boundary[i]['bound']
			ronde //= len(player)
			voice('gameround.mp3');print('='*35,'\nRound of Game --> Based on average\n\t>> {} ROUND <<'.format(ronde));print('='*35);wait(1)
			# specify the bet
			for i in range (len(player)):
				uangTaruhan += money[i]['money']
			uangTaruhan //= len(player)
			uangTaruhan *= 50/100
			wait(1);voice('opengame.mp3');print('\n>>> The Bet = {} <<<\n'.format(uangTaruhan));wait(1);voice('moneynow.mp3')

			for i in range (len(player)):
				if money[i]['money'] <uangTaruhan:
					voice('lack.mp3');print('\nSorry you lack money to guess, {}'.format(name[i]['name']))
					voice('choice.mp3')
					pinjaman=input('\n1. Borrow to Bookie\n2. Surrender\n\nMake your Choice {} [1/2]: '.format(name[i]['name']))
					while pinjaman != '1' or pinjaman != '2':
						pinjaman=input('Try Again dude :(  ')
					if pinjaman == '1':
						pinjam=(uangTaruhan*(ronde//2))-money[i]['money']
						print('\n You borrow the money of Bookie, Half of Round You can Survive\n')
						hasilPinjam =(money[i]['money']+pinjam)-uangTaruhan
						money[i]['money']=hasilPinjam
						wait(2);print('='*20+'>');print("You're money NOw :")
						print('>>',name[i]['name'],':',money[i]['money']);print('='*20+'>')
					elif pinjaman == '2':
						voice('leftgame.mp3')
						print('\n{} Quit the Game'.format(name[i]['name']))
						del player[i]
						del name[i]
						del money[i]
						del boundary[i]
						players-=1
						print('\nGame Will be Ended\n');wait(1)
						keluar=True
						break
				else: 
					hasil=money[i]['money']-uangTaruhan
					money[i]['money']=hasil
					wait(2);print('='*20+'>');print("You're money NOw :");print('>>',name[i]['name'],':',money[i]['money']);print('='*20+'>')	
			if keluar:
				wait(2);print('.\n');wait(1);print('.\n');wait(1);print('.\n');wait(1);print('Game is Finished');print ("="*45);voice('repeat.mp3')
				ulang = input("Do you want to Repeat the Game? (Y/N): ")
				if ulang == "N" or ulang == "n" or ulang == "NO" or ulang == "no": print("\nProgram has Ended\n");break
				else: continue
			else: keluar=False
			wait(2);voice('start.mp3');voice('3.mp3');print('\n>> 3 <<');voice('2.mp3');print('>> 2 <<');wait(0.5);voice('1.mp3');print('>> 1 <<');voice('go.mp3')
			taruhan=uangTaruhan*(len(player));print('\n'+'<'+'='*30+'>','\n| The Rule Of the Game:        |\n|  -> Guess 4 Digit number     |\n|  -> True Numer is Random     |\n|  -> Number from 0000 to 9999 |','\n'+'<'+'='*30+'>','\n')
			
			while start<=ronde:
				print('\n','<'+'='*12+'>','\n','|  ROUND {}  |'.format(start),'\n','<'+'='*12+'>')
				if start % 5==0:		
					komp=(uangBandar*10/100);print('\nBONUS LEVEL !!')
					voice('bonus.mp4')
					for i in range (len(player)):
						hasil=money[i]['money']+komp
						money[i]['money']=hasil;voice('moneyup.mp3')
						wait(2);print("-->> You're Money is Up!! :",name[i]['name'],'++>',money[i]['money'],"<<--");wait(2)
					print('\nLets Guess Again!!..')
				
				digit=str(random.randint(0,9))
				for i in range(3):
					num=str(random.randint(0,9))
					digit+=num 
				voice('guess.mp3')
				
				for i in range(len(player)):
					guess_input=input('\n|> Guess {} : '.format(name[i]['name']))
					while len(guess_input) > 4 or len(guess_input) < 4:
						print('='*20,'\nInput ERROR !!\n Please input 4 Character');voice('char.mp3')
						guess_input=input('\n|> Guess Again {} : '.format(name[i]['name']))
					guess_player.append({'guess {}'.format(i+1):guess_input})
				voice('countdown.mp3');wait(0.5);print('\n')
				for i in range (10):
					print('>> {} <<'.format(i+1));wait(1)
				for i in range(len(player)):
					tebakan=guess_player[i]['guess {}'.format(i+1)]
					if tebakan != digit:
						uangBandar+=uangTaruhan
						print('\nGuess again {}\n'.format(name[i]['name']));wait(1)
					elif tebakan == digit:
						voice('win.mp3');print("\nCongratulation {} !! You're The WINNER..!!".format(name[i]['name']))
						menang=money[i]['money']+taruhan
						money[i]['money']=menang
						uangBandar-=uangTaruhan*((len(player))-1)
						wait(2);voice('moneyup.mp3');print("-->> You're Money is Up!! :",name[i]['name'],'++>',money[i]['money'],"<<--");wait(2)
						win=player[i]['player']
				
				print('\n>> Bookie Money ++ ==>',uangBandar,'<<\n')
				for i in range (len(player)):
					if money[i]['money'] <uangTaruhan:
						voice('lack.mp3');print('\nSorry you lack money to guess, {}'.format(name[i]['name']))
						voice('choice.mp3')
						pinjaman=input('\n1. Borrow to Bookie\n2. Surrender\n\nMake your Choice {} [1/2]: '.format(name[i]['name']))
						if pinjaman == '1':
							pinjam=(uangTaruhan*(ronde//2))-money[i]['money']
							print('\n You borrow the money of Bookie, Half of Remaining Round You can Survive\n')
							hasilPinjam =(money[i]['money']+pinjam)-uangTaruhan
							money[i]['money']=hasilPinjam
							wait(2);print('='*20+'>');print("You're money NOw :");print('>>',name[i]['name'],':',money[i]['money']);print('='*20+'>')
						else:
							voice('leftgame.mp3');print('\n{} Quit the Game'.format(name[i]['name']));del player[i];del name[i];del money[i];del boundary[i];players-=1;print('.');wait(0.5);print('.');wait(0.5);print('.');wait(0.5);print('\nGame Will be Ended\n');wait(1);keluar=True;break
					else: 
						hasil=money[i]['money']-uangTaruhan
						money[i]['money']=hasil
						wait(2);print('='*20+'>');print("You're money NOw :");print('>>',name[i]['name'],':',money[i]['money']);print('='*20+'>')
				if keluar: wait(2);print('.\n');wait(1);print('.\n');wait(1);print('.\n');wait(1);print('Game is Finished');break
				else: keluar=False
				start+=1
			print ("="*45);voice('repeat.mp3')
			ulang = input("Do you want to Repeat the Game? (Y/N): ")
			if ulang == "N" or ulang == "n" or ulang == "NO" or ulang == "no": print("\nGame has Ended\n");break
	
	elif pilihan == '2':
		select=["angka","gambar"]
		print('\n','<'+'='*18+'>','\n','|  GUESS THE COIN  |','\n','<'+'='*18+'>');voice('welcomecoin.mp3');wait(1)
		while True:
			result=random.choice(select)
			guess=input("\nGuess the Coin [angka/gambar]: ")
			if guess==result:
				wait(1);voice('check.mp3');print("\n",guess,end=" ");wait(0.5);print("====>",end=" ");wait(1);print(result);wait(0.5)
				print("\nWow..!! You're Guessed Right\n")
				print("="*45)
				again=input("Do You want to Continue ? (Y/N): ")
				if again == 'N' or again=='n'or again=='no'or again=='NO':
					print("\nProgram Ends, Thank you for using this program\n")
					break
			else:
				wait(1);voice('check.mp3');print("\n",guess,end=" ");wait(0.5);print("====>",end=" ");wait(1);print(result);wait(0.5)
				print("\nYou're Guess is Wrong !!\nPlease Try Again\n")
	else: wait(1);voice('finish.mp3');print('\nProgram Finished..');print("\nThank You for using this Program\n");voice('end.mp3');break
