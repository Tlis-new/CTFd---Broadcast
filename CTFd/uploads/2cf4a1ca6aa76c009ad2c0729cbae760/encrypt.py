cipher=''
for i in range(len(flag)):
	cipher+=chr(ord(flag[i])^i + i<<1)
print cipher.encode('hex')

#encrypt: 7468617f4f72747d475f4e4342574d4f1f2b382922352c33123b181e191b0a15f4fdf5