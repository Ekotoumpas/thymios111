"""
Trexei olouts tous ari8mous ews 1000
kai me thn sunarthsh sum pros8etei ta digit toy
kai an diairei ton ari8mo(ton euato tou) akribws 
ton tupwnei
"""
print '___HARSHAD NUMBERS___'
for harshad in range (1,1000):
	if not harshad % sum(int(ch) for ch in str(harshad)):		
		print harshad
mul =1
""" 
Trexei olous tous ari8mous, ka8e ena ari8mo ton 
epejergazetai ws string pollaplasiazei tous chars tou string(
dld tous ari8mous pou apoteloun ton arithmo)kai kanei thn 
diairesh mod me ton ari8mo an bgei 0 ton tupwnei 
"""
print ' Ari8moi me to ginomeno psifiwn'
for i in range(1,1000):
	tmp = str(i)
	for num in tmp:				
		mul *= int(num)
		if not mul:
			break
	if mul and not i % mul:
		print i
	mul =1
