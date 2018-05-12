############################################################################
# Author: Martin SAVESKI
# Date: May 2009
# License: MIT
#
# AI Agent for Connect Four
#
# ConFour.py
# * Evaluation Function - optimized using hash table
# * Alpha Beta Pruning Search Algorithm
# * Iterative Deepening Search Algorithm
############################################################################

from heu import *
from Con4Utils import *
from time import gmtime
from Rule import rule_eval


def ev_change(l, li):  # 성송 ver eval
    result = 0
    try:
        for i in range(len(li), 0, -1):
            result += 10 ** (i - 1) * li[len(li) - i]
        l[result]
    except KeyError:
            result = 0
            for i in range(len(li), 0, -1):
                result += 10 ** (i - 1) * li[len(li) - i] if li[len(li) - i] != 3 else 0
    try:
        return l[result]
    except KeyError:
        return 0


def ev_change3(l, li):  # 성송 ver eval
    result = 0
    try:
        for i in range(len(li), 0, -1):
            result += 3 ** (i - 1) * li[len(li) - i]
        l[result]
    except KeyError:
        for i in range(len(li), -1, -1):
            result += 3 ** (i - 1) * li[len(li) - i] if li[len(li) - i] != 3 else 0
    return l[result]


# Evaluation Method, uses the hash tables to evalutate lines
def eval(t):  # 성송 ver eval
    evaluation = 0
    moves = validMoves(t)
    t = validmoves_0to3(t,moves)

    for i in range(6):  # l7
        evaluation += ev_change(l7, [t[i][0], t[i][1], t[i][2], t[i][3], t[i][4], t[i][5], t[i][6]])
    for i in range(7):
        evaluation += ev_change(l6, [t[0][i], t[1][i], t[2][i], t[3][i], t[4][i], t[5][i]])
    evaluation += ev_change(l6, [t[0][0], t[1][1], t[2][2], t[3][3], t[4][4], t[5][5]])
    evaluation += ev_change(l6, [t[0][1], t[1][2], t[2][3], t[3][4], t[4][5], t[5][6]])
    evaluation += ev_change(l6, [t[5][1], t[4][2], t[3][3], t[2][4], t[1][5], t[0][6]])
    evaluation += ev_change(l6, [t[5][0], t[4][1], t[3][2], t[2][3], t[1][4], t[0][5]])

    evaluation += ev_change(l5, [t[1][0], t[2][1], t[3][2], t[4][3], t[5][4]])
    evaluation += ev_change(l5, [t[0][2], t[1][3], t[2][4], t[3][5], t[4][6]])
    evaluation += ev_change(l5, [t[4][0], t[3][1], t[2][2], t[1][3], t[0][4]])
    evaluation += ev_change(l5, [t[5][2], t[4][3], t[3][4], t[2][5], t[1][6]])

    evaluation += ev_change(l4, [t[0][3], t[1][4], t[2][5], t[3][6]])
    evaluation += ev_change(l4, [t[2][0], t[3][1], t[4][2], t[5][3]])
    evaluation += ev_change(l4, [t[3][0], t[2][1], t[1][2], t[0][3]])
    evaluation += ev_change(l4, [t[5][3], t[4][4], t[3][5], t[2][6]])
    t = validmoves_3to0(t,moves)
    return evaluation


# valid moves
order=[3,2,4,1,5,0,6]


def validMoves(intable):
    moves = []
    for col in order:
        for row in range(6):
            if intable[row][col] == 0:
                moves.append([row, col])
                break
    return moves


def validmoves_0to3(intable, moves):
    for i in range(len(moves)):
        row = moves[i][0]
        col = moves[i][1]
        if row == -1:
            pass
        intable[row][col] = 3
    return intable


def validmoves_3to0(intable, moves):
    for i in range(len(moves)):
        row = moves[i][0]
        if row == -1:
            pass
        col = moves[i][1]
        intable[row][col] = 0
    return intable

def heuristic_or_rule():
    while True:
        print("Heuristic:1  Rule:2")
        n = int(input("Select: "))
        if n == 1:
            return "Heuristic"
        elif n == 2:
            return "Rule"
        else:
            print("Invalid input")


# moves in slot x acording to valid moves function
def move(intable, x, who):
    val = validMoves(intable)
    intable[val[x][0]][val[x][1]] = who

def move2(intable, x, who): #rule이 사용하는 move
    val = availablemove(intable)
    intable[val[x][0]][val[x][1]] = who

def availablemove(table): #각 칼럼에 둘 수 있는 칸의 주소를 저장
    moves = []
    count = 0
    for col in range(7):
        count = 0
        for row in range(6):
            if table[row][col] == 0: #0은 안둔것 1은 나 2는 너
                moves.append([row, col])
                break
            elif table[row][col] != 0:
                count += 1
            if count == 6:
                moves.append([1000, 1000])
                count = 0
                break
    return moves

# Alpha Beta Pruning Search Algorithm
def alphabetaPruning(intable, depth, startT):
    def ab(intable, depth, alpha, beta, startT):
        values = [];
        v = -10000000
        for a, s in validMoves(intable):
            intable[a][s] = 1
            v = max(v, abmin(intable, depth - 1, alpha, beta))
            values.append(v)
            intable[a][s] = 0
            if time() - startT >= 95:
                return "TimeOut"
        largest = max(values)
        dex = values.index(largest)
        return [dex, largest]


    def abmax(intable, depth, alpha, beta):
        moves = validMoves(intable)
        if (depth == 0 or not moves):
            return eval(intable)

        v = -10000000
        for a, s in moves:
            intable[a][s] = 1
            v = max(v, abmin(intable, depth - 1, alpha, beta))
            intable[a][s] = 0
            if v >= beta: return v
            alpha = max(alpha, v)
        return v


    def abmin(intable, depth, alpha, beta):
        moves = validMoves(intable)
        if (depth == 0 or not moves):
            return eval(intable)

        v = +10000000
        for a, s in moves:
            intable[a][s] = 2
            v = min(v, abmax(intable, depth - 1, alpha, beta))
            intable[a][s] = 0
            if v <= alpha: return v
            beta = min(beta, v)
        return v

    return ab(intable, depth, -10000000, +10000000, startT)


# returns the minutes*60 + seconds in the actial time
def time(): return ((gmtime()[4]) * 60) + gmtime()[5]


# Iterative Deepening Search Algorithm
def iterDeepening(intable):
    global order
    # order=[3,2,4,1,5,0,6]

    timeout = time() + 120
    startT = time()
    depth = 9
    #res=alphabetaPruning(intable, depth, startT)
    while True:
        tStart = time()
        """
        tmp=res[0]
        while tmp!=0:
            order[tmp-1],order[tmp]=order[tmp],order[tmp-1]
            tmp-=1
        """
        #depth+=1
        answer = alphabetaPruning(intable, depth, startT)
        tEnd = time()
        runTime = tEnd - tStart
        print("연산시간", tStart + runTime - (timeout - 120))
        """
        if answer == "TimeOut":
            print("DEPTH", depth-1)
            print("timeout 되기 직전..")
            print(type(res[0]), res[0])
            return res[0]
        else:
            return answer[0]
        """
        return answer[0]
table = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]


if __name__ == "__main__":
    #####SET###########
    table.reverse()

    l4={}
    for li in open("eval/4ki.txt"):
        tok=li.split()
        l4[int(tok[0])]=int(tok[1])

    l5 = {}
    for li in open("eval/5ki.txt"):
        tok = li.split()
        l5[int(tok[0])] = int(tok[1])

    l6 = {}
    for li in open("eval/6ki.txt"):
        tok = li.split()
        l6[int(tok[0])] = int(tok[1])

    l7 = {}
    for li in open("eval/7ki.txt"):
        tok = li.split()
        l7[int(tok[0])] = int(tok[1])

    ######## GAME ###########
    agent = 0
    player = 0
    first = input("Do you want to play first? (y/n) >> ")
    player_input = ['5', '5', '5', '5', '5']

    # the player plays first
    if first == 'y' or first == 'Y':
        draw(table)
        step = 0
        moves = validMoves(table)
        while validMoves(table):
            step += 1
            #상대 player 입력
            n = input("n: ")
            hmove(table, n)

            moves = validMoves(table)

            draw(table)

            if win(table) == 2:
                player += 1
                draw(table)
                break

            if not moves:  # 더이상 둘 공간 없는 경우
                break

            h = heuristic_or_rule()
            print("Hmmm let me think ?!??!")
            cStart = time()

            need_iterdeep = True
            if h == "Rule": #Rule 기반 연산
                move2(table, rule_eval(table), 1)
            else:           #Heuristic 기반 연산
                state = attack_critical_choice(table, moves)

                if state == "not critical":
                    state = protect_critical_choice(table, moves)
                    if state == "not critical":
                        move(table, iterDeepening(table), 1)
                    else: #막아야 할 critical choice
                        move(table, state, 1)
                        print("critical! defense")
                else: #공격 가능한 critical choice
                    need_iterdeep = False
                    move(table, state, 1)
                    print("critical! attack")


            moves = validMoves(table)

            draw(table)
            print("After ", time() - cStart, " seconds thinking!")
            if win(table) == 1:
                agent += 1
                break



    # The AI agent plays first
    else:
        step = 0
        moves = validMoves(table)

        while validMoves(table):
            step += 1

            h = heuristic_or_rule()
            print("Hmmm let me think ?!??!")
            cStart = time()
            need_iterdeep = True

            if step == 1:  # 첫번째 수에 가운데 안놓게 하는 장치(여기서는 3번째 줄에 둠)
                move(table, 1, 1)
            elif h == "Rule": #Rule 기반 연산
                move2(table, rule_eval(table), 1)
            else:             #Heuristic 기반 연산
                state = attack_critical_choice(table, moves)

                if state == "not critical":
                    state = protect_critical_choice(table, moves)
                    if state == "not critical":
                        move(table, iterDeepening(table), 1)
                    else: #막아야 할 critical choice
                        move(table, state, 1)
                        print("critical! defense")
                else: #공격 가능한 critical choice
                    need_iterdeep = False
                    move(table, state, 1)
                    print("critical! attack")

            draw(table)
            print("After ", time() - cStart, " seconds thinking!")

            if win(table) == 1:
                agent += 1
                break

            moves = validMoves(table)
            if not moves: ##더이상 둘 공간 없는 경우
                break

            #player 입력
            n = input("n: ")
            hmove(table, n)
            moves = validMoves(table)
            draw(table)

            if win(table) == 2:
                player += 1
                break

    if agent == player:
        print("DRAW")
    else:
        print("AI AGENT ", agent, " : ", player, " PLAYER")
