import numpy
import sys
print 'dwste to ligotero 5 ari8mous'
a = map(float, raw_input().split())

if len(a)<5: # afou afairoume 4 ari8mous
	print "Prepei na dwsete toulaxiston 5 ari8mous. Exiting..."
	sys.exit(0)

if len(a) == 4: # afou afairoume 2 max , 2 min times
	print "Wrong inputs"
#Afairw tous 2 max kai tous 2 min me 4 for loops
tmp = max(a)
for i in range (len(a)):
	if a[i] == tmp:
		del a[i]
		break

tmp = max(a)
for i in range (len(a)):
	if a[i] == tmp:
		del a[i]
		break

tmp = min(a)
for i in range (len(a)):
	if a[i] == tmp:
		del a[i]
		break
tmp = min (a)
for i in range (len(a)):
	if a[i] == tmp:
		del a[i]
		break

mesoOros =0
####   YPOLOGISMOS typikis apoklishs ###
# 1) briskoume meso oro
# 2) afairoume to meso oro tou sunolou ari8mwn apo ton ka8e arithmo
# 3) Upswnoume sto tetragwnw tis diafores kai tis a8roizoume
# 4) Diaroume to teliko noumero me to a8roisma ari8mwn(xwris tous 2 man,min)
# 5) H riza autou tou ari8mou einai o apoklish

for i in range (len(a)):
	mesoOros+=a[i]  

mesoOros = mesoOros/ len(a) # step 1
tetragwnoDiaforas = 0
athroismaDiaforas=0

for i in range(len(a)):
	tetragwnoDiaforas = (a[i]-mesoOros)**2 #step 2
	athroismaDiaforas += tetragwnoDiaforas # step 3

print 'H tupiki apoklish = ',numpy.sqrt(athroismaDiaforas/len(a)) # step 4 && 5