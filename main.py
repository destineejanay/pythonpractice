import sys
sys.path.insert(0, './libs')

import greeting as g
import guess as games
from count import find_length as leng
from numbering import loop_over_list
from lma import lma

def render():
    print(g.greeting('Destinee', 'Muse'))

render()

def game():
    print(games.guessing_game())

game()

def length():
    print(leng.find_length())

length()

def count():
    print(numbering.loop_over_list())

count()

def solve():
    print(lma.lma())

solve()




