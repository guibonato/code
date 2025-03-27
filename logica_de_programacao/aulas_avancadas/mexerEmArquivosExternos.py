""" w = open('teste.txt', 'w')

print(w.write('Escrevendo no arquivo\n'))
w.close()
 """

""" w = open('teste.txt')
print(w.read())
w.close() """

w = open('teste.txt')
a = w.readlines()
print(a)
w.close()
