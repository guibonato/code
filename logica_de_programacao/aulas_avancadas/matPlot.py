import matplotlib.pyplot as plt
""" plt.plot([1, 2, 3, 4], [2, 4, 9, 16])
plt.show() """

""" listax = []
listay = []

for i in range (10):
    listax.append(i)
    listay.append(i*i)

plt.plot(listax, listay)
plt.show()
 """

listax = [x for x in range(10)]
listay = [x*x for x in range(10)]

plt.plot(listax, listay)
plt.show()