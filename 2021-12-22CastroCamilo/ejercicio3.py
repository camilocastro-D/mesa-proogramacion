a = int(input("ingrese valor a"))
b = int(input("ingrese valor b"))
c = int(input("ingrese valor c"))
if a>b and a>c and b>c:
	print(a,b,c)
if a>b and a>c and c>b:
		print(a,c,b)
if b>a and b>c and a>c:
		    print(b,a,c)
if b>a and b>c and c>a:
		    print(b,c,a)
if c>a and c>b and a>b:
		        print(c,a,b)
if c>a and c>b and b>a:
		        print(c,b,a)