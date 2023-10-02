frase = 'Curso em Video Python'
print(frase)

print('Fatiação:')
print('frase[3] =',frase[3])
print('frase[3:13] =',frase[3:13])
print('frase[:13] =',frase[:13])
print('frase[13:] =',frase[13:])
print('frase[1:15] =',frase[1:15])
print('frase[1:15:2] =',frase[1:15:2])
print('frase[::2] =',frase[::2])

print("""texto grande exmplo texto grande exmplo texto grande exmplo
      texto grande exmplo texto grande exmplo texto grande exmplo
      texto grande exmplo texto grande exmplo texto grande exmplo""")

print('Análise:')
print('len(frase) =',len(frase))
print('frase.count("o") =',frase.count('o'))
print('frase.count("o",0,13) =',frase.count('o',0,13))
print('frase.find("deo") =',frase.find('deo'))
print('frase.find("Android") =',frase.find('Android'))
print('frase.upper() =',frase.upper())
print('frase.lower() =',frase.lower())
print('frase.upper().count("O") =',frase.upper().count('O'))
print('frase.split() =',frase.split())