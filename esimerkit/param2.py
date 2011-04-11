def tulosta_kaikki(a, b, *c, **d):
    print('tavalliset parametrit: ', a, b)
    print('listaparametrit: ')
    for arg in c:
        print(arg)
    print('nimiparametrit: ')
    for kwarg in d.items():
        print(kwarg)

# pääohjelma
c = [1, 2, 3, 4]
d = {'pi': 3.14, 'e': 2.72}

tulosta_kaikki('eka', 'toka', *c, **d)
# sama kuin: 
# tulosta_kaikki('eka', 'toka', c[0], c[1], c[2], c[3], pi=3.14, e=2.72)

# ohjelman tulostus 
'''
tavalliset parametrit:  eka toka
listaparametrit: 
1
2
3
4
nimiparametrit: 
('pi', 3.14)
('e', 2.72)
'''
