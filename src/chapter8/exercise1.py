
# a function called chop that takes a list and modifies it and returns none

def chop(list):
    fchop = list[1:]
    onumb = len(fchop)
    none = fchop[:onumb-1]
    print(none)
    return none


def middle(mlist):
    newlist = mlist[1]
    nnumb = len(newlist)
    new = newlist[:nnumb-1]
    print(new)
    return new


fruit = ['Mango', 'Orange', 'Pineapple', 'Peach']
print(fruit)

x = chop(fruit)
y = middle(fruit)

if x == y:
    print('Shits identical AND equivalent yo!')
else:
    print('Damn, it\'s equivalent but NOT identical')