import fileinput
from collections import deque

def gs(men, women, prefs):
    def engage(mnbr, wnbr):
        wengaged[wnbr] = mnbr 
        mengaged[mnbr] = wnbr 

    mengaged = {mnbr: None for mnbr in men}
    wengaged = {wnbr: None for wnbr in women}
    queue = deque(men)
    while queue:
        mnbr = queue.popleft()
        wnbr = prefs[mnbr].pop(0)
        if wengaged[wnbr] is None:
            engage(mnbr, wnbr)
        else:
            mnbr_ = wengaged[wnbr]
            if prefs[wnbr].index(mnbr) < prefs[wnbr].index(mnbr_):
                queue.append(mnbr_)
                engage(mnbr, wnbr)
            else:
                queue.append(mnbr)
    return mengaged

if __name__ == '__main__':
    stdin = fileinput.input()
    for line in stdin:
        if (line.startswith('#')): continue
        n = int(line.split('=')[1])
        break
    men, women = [], []
    names, prefs = dict(), dict()
    for i in range(0, n*2):
        line = stdin.readline()
        data = line.rstrip('\n ').split(' ')
        nbr = int(data[0])
        names[nbr] = data[1]
        (women if nbr % 2 == 0 else men).append(nbr)
    stdin.readline() # jump over empty line
    for line in stdin:
        data = line.rstrip('\n ').split(': ')
        nbr = int(data[0])
        prefs[nbr] = [int(n) for n in data[1].split(' ')]

    couples = gs(men, women, prefs) # do the hard work
    for mnbr in men:
        print '%s -- %s' % (names[mnbr], names[couples[mnbr]])
