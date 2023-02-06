c= 0
soma=0
cd=0
media=0
s=0
while c < 7:
	dias = int(input ())
	if dias >= 100:
		soma+= dias
		cd+=1
	s+=dias
	c+=1
	
media = s/7

print(cd)
print(int(media))
