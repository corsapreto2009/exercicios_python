n1 = int(input('me dê um valor em metros e eu converterei para centímetros ou milímetros. '))

cm = n1 * 100
mm = n1 * 1000

print ('Centímetros ou Milímetros?')
input()

if "Centímetros" or "centímetros" or "cm":
    print (n1, 'em centímetros é:', cm)
elif "Milímetros" or "milímetros" or "mm":
    print (n1 + ' em milímetros é: ' + mm)