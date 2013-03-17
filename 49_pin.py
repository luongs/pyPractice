#Pin Program
#Author Sebastien Luong

pin=12345

print "WELCOME TO THE ROYAL BANK OF SEBASTIEN."
print "ENTER YOUR PIN: "
pinInput=raw_input('>')

while(pin != int(pinInput)):
	print "INCORRECT PIN. TRY AGAIN."
	print "ENTER YOUR PIN: "
	pinInput=raw_input('>')

print "\nPIN ACCEPTED, WELCOME TO YOUR ACCOUNT"