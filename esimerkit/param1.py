def muuta1(y):
    print('muuta1 sai', y)
    y = [1, 2, 3]
    print('muuta1 muutti y arvoksi', y)
    
def muuta2(y):
    print('muuta2 sai', y)
    y.append(3)
    print('muuta2 muutti y arvoksi', y)
	
def muuta3(y):
    print('muuta3 sai', y)
    y = "egg and bacon"
    print('muuta3 muutti y arvoksi', y)    

# pääohjelma
x = [1, 2]
print('ennen muuta1 x arvo on', x)
muuta1(x)
print('muuta1 jälkeen x arvo on', x)

x = [1, 2]
print('ennen muuta2 x arvo on', x)
muuta2(x)
print('muuta2 jälkeen x arvo on', x)

x = "spam spam spam"
print('ennen muuta3 x arvo on', x)
muuta3(x)
print('muuta3 jälkeen x arvo on', x)

# ohjelman tulostus 
'''
ennen muuta1 x arvo on [1, 2]
muuta1 sai [1, 2]
muuta1 muutti y arvoksi [1, 2, 3]
muuta1 jälkeen x arvo on [1, 2]
ennen muuta2 x arvo on [1, 2]
muuta2 sai [1, 2]
muuta2 muutti y arvoksi [1, 2, 3]
muuta2 jälkeen x arvo on [1, 2, 3]
ennen muuta3 x arvo on spam spam spam
muuta3 sai spam spam spam
muuta3 muutti y arvoksi egg and bacon
muuta3 jälkeen x arvo on spam spam spam
'''
