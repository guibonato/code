print('Avaliação de notas.')

nota = float(input('Digite o valor da nota: '))

if 9 <= nota <= 10: print('Conceito A, parabéns!')
elif 7 <= nota < 9: print('Conceito B, muito bom!')
elif 5 <= nota < 7: print('Conceito C, estude mais!')
elif 3 <= nota <5: print('Conceito D, recuperação!')
elif 0 <= nota < 3: print('Conceito E, reprovado!')
else:
    print('Nota inválida')
