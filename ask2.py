import sys
a = raw_input("Give the sentence: \n")
left = 0
right = 0
canClose = 0

for i in range (len(a)):
	
	if a[i]=='(':
		left+=1
		canClose+=1
	elif a[i]==')':
		right+=1
		canClose-=1
	else:
		continue
	if canClose < 0:
		print "false"
		sys.exit()

if left == right:
	print "true"
else:
	print "false"		