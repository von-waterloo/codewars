'''def n_sqrt(n):
    if n < 0:
        return False
    s = n**0.5 - int(n**0.5)
    if s == 0 or n == 0:
        return True
    else:
        return False
print(n_sqrt(4))'''

'''def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            print(seq.count(i))
            return i
print(find_it([0,1,2,3,0,1,2,4]))'''
'''
def ste (n):
    v=2
    if n == 0:
        return 1
    for i in range(1,n):
        v*=2
    return v
print(ste(4))
'''
'''def disemvowel(string_):
    news = ''
    for i in string_:
        if i not in 'aeuioAEUIO':
            news = news + i
    return news
print(disemvowel('This website is for losers LOL!'))


def disemvowel(string_):
    return ''.join([i for i in string_ if i not in 'aeuioAEUIO'])
print(disemvowel('This website is for losers LOL!'))
'''
'''def spin_words(sentence):
    sp = sentence.split(' ')
    new_sp = []
    for i in sp:
        if len(i) >= 5:
            new_sp.append(i[::-1])
        else:
            new_sp.append(i)
    return ' '.join(new_sp)
print(spin_words('This sentence is a sentence'))'''

'''def printer_error(s):
    count = 0
    for i in s:
        if i in 'noprstuzxvqwy':
            count += 1
    return f'{count}/{len(s)}'
print(printer_error('aaaaabbbbbzzz'))'''

class Music:
    def __init__(self, name, genre, century):
        self.name = name
        self.genre = genre
        self.century = century
    def info(self):
        print(f'{self.name} - композитор {self.century} века. {self.name} писал музыку в жанре {self.genre}.')
    def packman (self, victim):
        print(f'{self.name} укусил падлу {victim} за жопку -- остался {victim[3:].capitalize()}')

beethoven = Music('Beethoven', 'romanticism', 'XIX')
mozart = Music('Mozart', 'classicism', 'XVIII')
bach = Music('Bach', 'barocco', 'XVIII')
# mozart.info(),bach.info(),beethoven.info()
beethoven.packman(mozart.name)
