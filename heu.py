# -*- coding: utf-8 -*-
"""
Created on Fri May  4 22:06:50 2018

@author: seongsong park
"""

def attack_critical_choice(intable, moves):
    for i in range(7):
        for j in range(6):
            # check vertical streaks
            try:
                if intable[j][i] == intable[j + 1][i] == intable[j + 2][i] == 1:
                    if [j - 1, i] in moves:
                        return moves.index([j - 1, i])
                    elif [j + 3, i] in moves:
                        return moves.index([j + 3, i])

            except IndexError:
                pass

            # check horizontal streaks
            try:
                if intable[j][i] == intable[j][i + 1] == intable[j][i + 2] == 1:
                    if [j, i + 3] in moves:
                        return moves.index([j, i + 3])

                    elif i - 1 > 0 and [j, i - 1] in moves:
                        return moves.index([j, i - 1])
                elif intable[j][i] == intable[j][i + 2] == intable[j][i + 3] == 1:
                    if [j, i + 1] in moves:
                        return moves.index([j, i + 1])

                elif intable[j][i] == intable[j][i + 1] == intable[j][i + 3] == 1:
                    if [j, i + 2] in moves:
                        return moves.index([j, i + 2])

            except IndexError:
                pass

            # check positive diagonal streaks
            try:

                if not i + 3 > 6 and intable[j][i] == intable[j + 1][i + 1] == intable[j + 2][i + 2] == 1:
                    if [j + 3, i + 3] in moves:
                        return moves.index([j + 3, i + 3])
                    # return intable
                    elif i - 1 > 0 and [j - 1, i - 1] in moves:
                        return moves.index([j - 1, i - 1])
                elif not i + 3 > 6 and intable[j][i] == intable[j + 1][i + 1] == intable[j + 3][i + 3] == 1:
                    if [j + 2, i + 2] in moves:
                        return moves.index([j + 2, i + 2])
                elif not i + 3 > 6 and intable[j][i] == intable[j + 2][i + 2] == intable[j + 3][i + 3] == 1:
                    if [i + 1, j + 1] in moves:
                        return moves.index([i + 1, j + 1])


            except IndexError:
                pass

            # check negative diagonal streaks
            try:

                if not i - 3 < 0 and intable[j][i] == intable[j + 1][i - 1] == intable[j + 2][i - 2] == 1:
                    if i - 3 > 0 and [j + 3, i - 3] in moves:
                        return moves.index([j + 3, i - 3])
                    elif [j - 1, i + 1] in moves:
                        return moves.index([j - 1, i + 1])
                elif not i - 3 < 0 and intable[j][i] == intable[j + 1][i - 1] == intable[j + 3][i - 3] == 1:
                    if i - 2 > 0 and [j + 2, i - 2] in moves:
                        return moves.index([j + 2, i - 2])
                elif not i - 3 < 0 and intable[j][i] == intable[j + 2][i - 2] == intable[j + 3][i - 3] == 1:
                    if i - 1 > 0 and [j + 1, i - 1] in moves:
                        return moves.index([j + 1, i - 1])

            except IndexError:
                pass
    return "not critical"

def protect_critical_choice(t,moves):
    #당장 안 막으면 지는 수 확인
    valid_m = validMoves2(t)
    # 왼쪽에서 오른쪽 위 대각선 /
    for i in range(5): #연속된 대각선
        for j in range(3,-1,-1):#3~0
            if is_two(t[j][i], t[j+1][i+1], t[j+2][i+2]):
                if is_in_table(j-1, i-1) and [j-1,i-1] in valid_m: #비워있지 않으면
                    return moves.index([j-1,i-1])
                elif is_in_table(j+3, i+3) and [j+3,i+3] in valid_m:
                    return moves.index([j+3,i+3])
    for i in range(4): #한 칸 띄어진 대각선
        for j in range(2,-1,-1):
            if is_two(t[j][i], t[j+1][i+1], t[j+3][i+3]) and [j+2,i+2] in valid_m:
                return moves.index([j + 2, i + 2])
            elif is_two(t[j][i], t[j+2][i+2], t[j+3][i+3]) and [j+1,i+1] in valid_m:
                return moves.index([j + 1, i + 1])
    #왼쪽에서 오른쪽 아래 대각선
    for i in range(5):
        for j in range(5,1,-1): #연속된 대각선
            if is_two(t[j][i], t[j-1][i+1], t[j-2][i+2]):
                if is_in_table(j+1,i-1) and [j+1,i-1] in valid_m:
                    return moves.index([j + 1, i - 1])
                elif is_in_table(j-3,i+3) and [j-3,i+3] in valid_m:
                    return moves.index([j - 3, i + 3])
    for i in range(4):
        for j in range(5,2,-1): #한 칸 띄어진 대각선
            if is_two(t[j][i], t[j-1][i+1], t[j-3][i+3]) and [j-2,i+2] in valid_m:
                return moves.index([j - 2, i + 2])
            elif is_two(t[j][i], t[j-2][i+2], t[j-3][i+3]) and [j-1,i+1] in valid_m:
                return moves.index([j - 1, i + 1])
    #아래, 오른쪽 직선
    for k in range(7):
        j, i = valid_m[k]
        if j == -1: # 해당 열에 valid move 없는 경우
            continue
        if j>=3 and is_two(t[j-1][i], t[j-2][i], t[j-3][i]): #아래 줄 검사
            print(moves)
            return moves.index([j, i])
        elif (i<=3 and is_two(t[j][i+1], t[j][i+2], t[j][i+3])) or\
             (i<=3 and i>=1 and is_two(t[j][i-1], t[j][i+1], t[j][i+2])) or\
             (i<=5 and i>=2 and is_two(t[j][i-2], t[j][i-1], t[j][i+1])) or\
             (i>=3 and is_two(t[j][i-1], t[j][i-2], t[j][i-3])):#오른쪽 줄 검사
            return moves.index([j, i])

    return "not critical"

def is_two(a,b,c):
    if a == 2 and b == 2 and c == 2:
        return True
    return False

def is_in_table(j,i):
    if j>=0 and j<=5 and i >= 0 and i <=6:
        return True
    return False

def validMoves2(intable):
    moves = []
    for col in range(7):
        for row in range(6):
            if intable[row][col] == 0:
                moves.append([row, col])
                break
            elif row == 5 and intable[row][col] !=0:
                moves.append([-1, col])

    return moves