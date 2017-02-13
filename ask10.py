import urllib2
import json
import sys

coins = {} # map pou krataei pairs bitcoinValue-onomaNomismatos
#H sunarthsh getBitCoinValues briskei thn timh bitCoin gia to nomisma pou pernei orisma(coinList)
#gia thn hmeromhnia pou dialeje o xrhsths pou thn pairnei ws orisma(date) kai to kanei add sto map coinsValueMap. 
def getBitCoinValues(coinslist,date):	
	#print 'bika me coin: ',coinsList,' kai date: ',date
	request = urllib2.Request("http://api.coindesk.com/v1/bpi/historical/close.json?start=%s&end=%s&currency=%s"%(date,date,coinslist))	
   	response = urllib2.urlopen(request)
   	html =  response.read()
   	html = html.split(':')
   	tmp = html[2]
   	tmp = tmp.split('}')   	
   	coins[tmp[0]]=coinslist # kanoume add to neo pair value-nomisma

coins2 = raw_input("Peite poia kruptonomismata 8elete na deite xwrismena me keno.px: USD EUR GBP:\n")
hmerominia = raw_input("Dwste hmerominia se morfh: YYYY-MM-DD \n")
coins2 = coins2.split(' ') # xwrizei apla ta nomismata me keno 

# kalw th synarthsh oses fores oses einai kai ta nomismata tou xrhsth me thn IDIA hneronhnia
for i in range(len(coins2)): 
	getBitCoinValues(coins2[i],hmerominia)

#Typwnw ta pairs tou map kanontas to sort ws pros thn ajia nomismatwn
for value in sorted(coins,key=float):
	print value,coins[value]
