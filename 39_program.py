
# python proram to shuffle deck of cards(using random and itertools)
import random,itertools

deck = list(itertools.product(range(1,14),["spade","club","hearts","diamond"]))
# print(deck)

random.shuffle(deck)
print(deck)


for i in range(5):
    print(deck[i][0], 'of', deck[i][1])