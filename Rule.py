from time import gmtime
import re



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

def boxno(table, columnNo, boxnumber):  #table의 하나의 유효한 칼럼에 주변 박스 번호를 통해 값을 반환하는 함수
    x = 0
    y = 0
    if boxnumber == 1:
        x += 1
        y -= 1
    elif boxnumber == 2:
        x += 1
        y = 0
    elif boxnumber == 3:
        x += 1
        y += 1
    elif boxnumber == 4:
        x = 0
        y -= 1
    elif boxnumber == 5:
        x = 0
        y += 1
    elif boxnumber == 6:
        x -= 1
        y -= 1
    elif boxnumber == 7:
        x -= 1
        y = 0
    elif boxnumber == 8:
        x -= 1
        y += 1
    ac = availablemove(table)  # ac = available column
    if (ac[columnNo - 1][0] + x) >= 0 and (ac[columnNo - 1][1] + y) >= 0 and (ac[columnNo - 1][0] + x) <= 5 and (
            ac[columnNo - 1][1] + y) <= 6:  # 테이블 범위 안에 들어가면
        value = table[ac[columnNo - 1][0] + x][ac[columnNo - 1][1] + y]
    else:  # 테이블 범위 안에 들어가지 않으면
        value = -1
    return value  # -1은 범위 밖의 것, 0은 안둔것, 1은 나, 2는 너


def furtherboxno(table, columnNo, boxdirection, repeatitiontime): #같은 방향으로의 특정값 번째 박스의 값
    x=0
    y=0
    for i in range(repeatitiontime):
        if boxdirection == 1:
            x += 1
            y -= 1
        elif boxdirection == 2:
            x += 1
            y = 0
        elif boxdirection == 3:
            x += 1
            y += 1
        elif boxdirection == 4:
            x = 0
            y -= 1
        elif boxdirection == 5:
            x = 0
            y += 1
        elif boxdirection == 6:
            x -= 1
            y -= 1
        elif boxdirection == 7:
            x -= 1
            y = 0
        elif boxdirection == 8:
            x -= 1
            y += 1
    ac = availablemove(table)  # ac = available column
    if (ac[columnNo - 1][0] + x)>=0 and (ac[columnNo - 1][1] + y)>=0 and (ac[columnNo - 1][0] + x)<=5 and (ac[columnNo - 1][1] + y)<=6:#테이블 범위 안에 들어가면
        value = table[ac[columnNo - 1][0] + x][ac[columnNo - 1][1] + y]
    else: # 테이블 범위 안에 들어가지 않으면
        value = -1
    return value #-1은 범위 밖의 것, 0은 안둔것, 1은 나, 2는 너


def checkmypoint(table, columnNo): #하나의 칼럼에 대해 확인, value 2은 양쪽 다 막힘 1은 한쪽만 막힘 0은 안막힘
    count = 0
    front = 0
    back = 0
    pair = []
    point = []
    for i in range(1, 9):  #각각의 box를 확인
        if boxno(table, columnNo, i) == 1 :  # 첫번째 layer에서 나의 돌일때
            count += 1 #하나의 반복된 노드
            for j in range(1, 6): # 같은 (앞)방향에서 계속 하나씩 나아가서 확인
                if furtherboxno(table, columnNo, i, j+1) == 1:#앞방향으로 계속 나의 돌일때
                    count += 1 #계속 몇번 반복인지 늘려나간다
                elif furtherboxno(table, columnNo, i, j+1) == 0:#앞방향이 비어 있을때
                    front = 0
                    break
                else: #앞방향이 막혔거나 상대방 돌일때
                    front = 1 #앞방향 막혀있음
                    break
            for z in range(1, 5): # 반대 (뒷)방향에서 계속 하나씩 나아가서 확인
                if furtherboxno(table, columnNo, abs(9-i), z) == 1: #뒷방향으로 계속 나의 돌일때
                    count += 1 #계속 몇번 반복인지 늘려나간다
                elif furtherboxno(table, columnNo, abs(9-i), z) == 0: #뒷방향이 비어 있을때
                    back = 0
                    break
                else: #앞방향이 막혔거나 상대방 돌일때
                    back = 1 #뒷방향 막혀있음
                    break
            value = front + back
            pair.append((value, count, i))
            count = 0
            value = 0
    for y in range(len(pair)):
        if pair[y][0] == 2 and pair[y][1] == 2: #둘다 막혔으면서 연속된 것이 2개면 소용이 없음 value 유지
            value = 0;
        elif pair[y][1] >= 3: #연속된 것이 3개라면 무조건 이기니 value up!
            value = 10000
        elif pair[y][0] == 1 and pair[y][1] == 2: #한쪽만 막혔으면서 연속이 2개이면 value 추가!
            value = 1000
        elif pair[y][0] == 0 and pair[y][1] == 2: #양쪽 다 막히지 않았으며 연속이 2개이면 value 추가!
            value = 5000
        else:
            value = 0
        point.append(value)
        value = 0
    point.sort(reverse= True)
    if point == []:
        point.append(0)
    return point[0]




def checkopponentpoint(table, columnNo): #하나의 칼럼에 대해 확인, value 2은 양쪽 다 막힘 1은 한쪽만 막힘 0은 안막힘
    count = 0
    front = 0
    back = 0
    pair = []
    point = []
    for i in range(1, 9):  #각각의 box를 확인
        if boxno(table, columnNo, i) == 2 :  # 첫번째 layer에서 상대의 돌일때
            count += 1 #하나의 반복된 노드
            for j in range(1, 6): # 같은 (앞)방향에서 계속 하나씩 나아가서 확인
                if furtherboxno(table, columnNo, i, j+1) == 2:#앞방향으로 계속 상대의 돌일때
                    count += 1 #계속 몇번 반복인지 늘려나간다
                elif furtherboxno(table, columnNo, i, j+1) == 0:#앞방향이 비어 있을때
                    front = 0
                    break
                else: #앞방향이 막혔거나 나의 돌일때
                    front = 1 #앞방향 막혀있음
                    break
            for z in range(1, 5): # 반대 (뒷)방향에서 계속 하나씩 나아가서 확인
                if furtherboxno(table, columnNo, abs(9-i), z) == 2: #뒷방향으로 계속 상대의 돌일때
                    count += 1 #계속 몇번 반복인지 늘려나간다
                elif furtherboxno(table, columnNo, abs(9-i), z) == 0: #뒷방향이 비어 있을때
                    back = 0
                    break
                else: #앞방향이 막혔거나 나의 돌일때
                    back = 1 #뒷방향 막혀있음
                    break
            value = front + back
            pair.append((value, count, i))
            count = 0
            value = 0
    for y in range(len(pair)):
        if pair[y][0] == 2 and pair[y][1] == 2: #둘다 막혔으면서 연속된 것이 2개이면 소용이 없음 value 유지
            value = 0
        elif pair[y][1] >= 3: #연속된 것이 3개라면 무조건 이기니 value up!
            value = 10001
        elif pair[y][0] == 1 and pair[y][1] == 2: #한쪽만 막혔으면서 연속이 2개이면 value 추가!
            value = 1001
        elif pair[y][0] == 0 and pair[y][1] == 2: #양쪽 다 막히지 않았으며 연속이 2개이면 value 추가!
            value = 5001
        else:
            value = 0
        point.append(value)
        value = 0
    point.sort(reverse= True)
    if point == []:
        point.append(0)
    return point[0]


def aboveavailablemove(table): #각 칼럼에 둘 수 있는 칸 바로 위의 주소
    moves2 = []
    count = 0
    for col in range(7):
        count = 0
        for row in range(6):
            if table[row][col] == 0: #0은 안둔것 1은 나 2는 너
                moves2.append([row+1, col])
                break
            elif table[row][col] != 0:
                count += 1
            if count == 6:
                moves2.append([1000, 1000])
                count = 0
                break
    return moves2




def aboveboxno(table, columnNo, boxnumber):  #둘 수 있는 칸 바로 위의 주소를 기준으로 하는 box넘버링
    x = 0
    y = 0
    if boxnumber == 1:
        x += 1
        y -= 1
    elif boxnumber == 2:
        x += 1
        y = 0
    elif boxnumber == 3:
        x += 1
        y += 1
    elif boxnumber == 4:
        x = 0
        y -= 1
    elif boxnumber == 5:
        x = 0
        y += 1
    elif boxnumber == 6:
        x -= 1
        y -= 1
    elif boxnumber == 7:
        x -= 1
        y = 0
    elif boxnumber == 8:
        x -= 1
        y += 1
    ac = aboveavailablemove(table)  # ac = available column
    if (ac[columnNo - 1][0] + x) >= 0 and (ac[columnNo - 1][1] + y) >= 0 and (ac[columnNo - 1][0] + x) <= 5 and (
            ac[columnNo - 1][1] + y) <= 6:  # 테이블 범위 안에 들어가면
        value = table[ac[columnNo - 1][0] + x][ac[columnNo - 1][1] + y]
    else:  # 테이블 범위 안에 들어가지 않으면
        value = -1
    return value  # -1은 범위 밖의 것, 0은 안둔것, 1은 나, 2는 너


def abovefurtherboxno(table, columnNo, boxdirection, repeatitiontime): #같은 방향으로의 특정값 번째 박스의 값
    x=0
    y=0
    for i in range(repeatitiontime):
        if boxdirection == 1:
            x += 1
            y -= 1
        elif boxdirection == 2:
            x += 1
            y = 0
        elif boxdirection == 3:
            x += 1
            y += 1
        elif boxdirection == 4:
            x = 0
            y -= 1
        elif boxdirection == 5:
            x = 0
            y += 1
        elif boxdirection == 6:
            x -= 1
            y -= 1
        elif boxdirection == 7:
            x -= 1
            y = 0
        elif boxdirection == 8:
            x -= 1
            y += 1
    ac = aboveavailablemove(table)  # ac = available column
    if (ac[columnNo - 1][0] + x)>=0 and (ac[columnNo - 1][1] + y)>=0 and (ac[columnNo - 1][0] + x)<=5 and (ac[columnNo - 1][1] + y)<=6:#테이블 범위 안에 들어가면
        value = table[ac[columnNo - 1][0] + x][ac[columnNo - 1][1] + y]
    else: # 테이블 범위 안에 들어가지 않으면
        value = -1
    return value #-1은 범위 밖의 것, 0은 안둔것, 1은 나, 2는 너

def checkaboveopponentpoint(table, columnNo): #내가 해당 available칸에 두었을 때 바로 윗칸을 이용해 상대가 이기는 경우에 대한 차감값
    count = 0
    front = 0
    back = 0
    pair = []
    point = []
    for i in range(1, 9):  #각각의 box를 확인
        if aboveboxno(table, columnNo, i) == 2 :  # 첫번째 layer에서 상대의 돌일때
            count += 1 #하나의 반복된 노드
            for j in range(1, 6): # 같은 (앞)방향에서 계속 하나씩 나아가서 확인
                if abovefurtherboxno(table, columnNo, i, j+1) == 2:#앞방향으로 계속 상대의 돌일때
                    count += 1 #계속 몇번 반복인지 늘려나간다
                elif abovefurtherboxno(table, columnNo, i, j+1) == 0:#앞방향이 비어 있을때
                    front = 0
                    break
                else: #앞방향이 막혔거나 나의 돌일때
                    front = 1 #앞방향 막혀있음
                    break
            for z in range(1, 5): # 반대 (뒷)방향에서 계속 하나씩 나아가서 확인
                if abovefurtherboxno(table, columnNo, abs(9-i), z) == 2: #뒷방향으로 계속 상대의 돌일때
                    count += 1 #계속 몇번 반복인지 늘려나간다
                elif abovefurtherboxno(table, columnNo, abs(9-i), z) == 0: #뒷방향이 비어 있을때
                    back = 0
                    break
                else: #앞방향이 막혔거나 나의 돌일때
                    back = 1 #뒷방향 막혀있음
                    break
            value = front + back
            pair.append((value, count, i))
            count = 0
            value = 0
    for y in range(len(pair)):
        if pair[y][1] >= 3: #연속된 것이 3개라면 무조건 이기니 value up!
            value = -10000
        elif pair[y][0] == 0 and pair[y][1] == 2: #양쪽 다 막히지 않았으며 연속이 2개이면 value 추가!
            value = -5000
        else:
            value = 0
        point.append(value)
        value = 0
    point.sort()
    if point == []:
        point.append(0)
    return point[0]


def checkabovemypoint(table, columnNo): #내가 해당 available칸에 두었을 때 바로 윗칸을 이용해 상대가 이기는 경우에 대한 차감값
    count = 0
    front = 0
    back = 0
    pair = []
    point = []
    for i in range(1, 9):  #각각의 box를 확인
        if aboveboxno(table, columnNo, i) == 1 :  # 첫번째 layer에서 상대의 돌일때
            count += 1 #하나의 반복된 노드
            for j in range(1, 6): # 같은 (앞)방향에서 계속 하나씩 나아가서 확인
                if abovefurtherboxno(table, columnNo, i, j+1) == 1:#앞방향으로 계속 상대의 돌일때
                    count += 1 #계속 몇번 반복인지 늘려나간다
                elif abovefurtherboxno(table, columnNo, i, j+1) == 0:#앞방향이 비어 있을때
                    front = 0
                    break
                else: #앞방향이 막혔거나 나의 돌일때
                    front = 1 #앞방향 막혀있음
                    break
            for z in range(1, 5): # 반대 (뒷)방향에서 계속 하나씩 나아가서 확인
                if abovefurtherboxno(table, columnNo, abs(9-i), z) == 1: #뒷방향으로 계속 상대의 돌일때
                    count += 1 #계속 몇번 반복인지 늘려나간다
                elif abovefurtherboxno(table, columnNo, abs(9-i), z) == 0: #뒷방향이 비어 있을때
                    back = 0
                    break
                else: #앞방향이 막혔거나 나의 돌일때
                    back = 1 #뒷방향 막혀있음
                    break
            value = front + back
            pair.append((value, count, i))
            count = 0
            value = 0
    #(x, y, z)는 z박스의 방향으로 x만큼 양쪽이 막혔고 y만큼 연속으로 나의 돌이 있다는 뜻
    for y in range(len(pair)):
        if pair[y][1] >= 3: #연속된 것이 3개라면 무조건 이기니 value up!
            value = -10000
        elif pair[y][0] == 0 and pair[y][1] == 2: #양쪽 다 막히지 않았으며 연속이 2개이면 value 추가!
            value = -5000
        else:
            value = 0
        point.append(value)
        value = 0
    point.sort()
    if point == []:
        point.append(0)
    return point[0]


def rule_eval(table):
    index = 0;
    count3 = 0
    h=0
    fullcol = []
    count = []
    total = 0
    zerocount = 0
    evaltable = []
    initialvalue = [-2, -1, 0, 1, 0, -1, -2]
    for i in range(1, 8):
        if table[5][i-1] == 2 or table[5][i-1] == 1: #칼럼이 꽉차면 방지
            total = -1
        else:
            total = (checkopponentpoint(table, i)) + (checkmypoint(table, i)) +(checkaboveopponentpoint(table, i)) + (checkabovemypoint(table, i)) #상대와 나의 돌의 점수를 더한다
        evaltable.append(total)
        total = 0
    for y in range(len(evaltable)): #처음의 벨류가 다 0일때나 모든 available 칸의 값이 0이나 -1 즉 꽉찼을 때 벨류값 넣기!
        if evaltable[y] == 0 or evaltable[y] == -1:
            zerocount += 1
    if zerocount == 7:
        for z in range(len(initialvalue)):
            count.append(initialvalue[z])
        count.sort(reverse=True)
        for col in range(7): # 꽉차있는 col을 제외시키기 위한 것
            for row in range(6):
                if table[row][col] != 0:
                    count3 += 1
                if count3 == 6:
                    fullcol.append(col) #fullcol안에는 꽉차있는 행이 다 들어있다
                    count3 = 0
                    break
        for j in range(0, 7):
            if initialvalue[j] == count[h]: #이미 큰것이 왼쪽으로 정리된 count에 0번 원소와 initialvalue가 일치한다면 값을 리턴! 하지만 선택된 col이 꽉차있다면
                if fullcol == []: #꽉차 있는 것이 없다면 그대로 return
                    return j
                else:
                    for r in range(len(fullcol)): #꽉차있는 col과 놓으려는 col이 같다면 그 다음 높은 벨류를 선택한다
                        if j == fullcol[r]:
                            h += 1
                            break
                        h = 0
                        if r == len(fullcol)-1:
                            return j

    else:
        for z in range(len(evaltable)):
            count.append(evaltable[z])
        count.sort(reverse=True)
        for col in range(7): # 꽉차있는 col을 제외시키기 위한 것
            count3 = 0
            for row in range(6):
                if table[row][col] != 0:
                    count3 += 1
                if count3 == 6:
                    fullcol.append(col) #fullcol안에는 꽉차있는 행이 다 들어있다
                    count3 = 0
                    break
        for k in range(0, 7):
            for j in range(0, 7):
                if evaltable[j] == count[k]: #이미 큰것이 왼쪽으로 정리된 count에 0번 원소와 initialvalue가 일치한다면 값을 리턴! 하지만 선택된 col이 꽉차있다면
                    if fullcol == []:
                        return j
                    index = j
                for r in range(len(fullcol)):  # 꽉차있는 col과 놓으려는 col이 같다면 그 다음 높은 벨류를 선택한다
                    if index == fullcol[r]:
                        break
                    if r == len(fullcol) - 1:
                        return j



#represnts the table
def draw(a=[]):
    def tc(a):
        if a==0: return " "
        if a==1: return "X"
        if a==2: return "Y"

    print ("\n\n           --------------------------- ")
    print ("           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[5][0]),tc(a[5][1]),tc(a[5][2]),tc(a[5][3]),tc(a[5][4]),tc(a[5][5]),tc(a[5][6])))
    print ("           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[4][0]),tc(a[4][1]),tc(a[4][2]),tc(a[4][3]),tc(a[4][4]),tc(a[4][5]),tc(a[4][6])))
    print ("           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[3][0]),tc(a[3][1]),tc(a[3][2]),tc(a[3][3]),tc(a[3][4]),tc(a[3][5]),tc(a[3][6])))
    print ("           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[2][0]),tc(a[2][1]),tc(a[2][2]),tc(a[2][3]),tc(a[2][4]),tc(a[2][5]),tc(a[2][6])))
    print ("           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[1][0]),tc(a[1][1]),tc(a[1][2]),tc(a[1][3]),tc(a[1][4]),tc(a[1][5]),tc(a[1][6])))
    print ("           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[0][0]),tc(a[0][1]),tc(a[0][2]),tc(a[0][3]),tc(a[0][4]),tc(a[0][5]),tc(a[0][6])))
    print ("           --------------------------- ")
    print ("            1   2   3   4   5   6   7    \n\n")

#determines whether there is a winner
def win(intable=[]):
    w1=[1,1,1,1]
    w2=[2,2,2,2]

    #horizontal
    for i in range(6):
        for j in range(4):
            if [intable[i][j],intable[i][j+1],intable[i][j+2],intable[i][j+3]]==w1:
                return 1
            if [intable[i][j],intable[i][j+1],intable[i][j+2],intable[i][j+3]]==w2:
                return 2

    #vertical
    for i in range(7):
        for j in range(3):
            if [intable[j][i], intable[j+1][i], intable[j+2][i], intable[j+3][i]]==w1:
                return 1
            if [intable[j][i], intable[j+1][i], intable[j+2][i], intable[j+3][i]]==w2:
                return 2

    #left to right
    for j in range(3):
        for i in range(4):
            if [intable[j][i], intable[j+1][i+1], intable[j+2][i+2], intable[j+3][i+3]]==w1:
                return 1
            if [intable[j][i], intable[j+1][i+1], intable[j+2][i+2], intable[j+3][i+3]]==w2:
                return 2


    #right to left
    for j in range(3):
        for i in range(6,2,-1):
            if [intable[j][i], intable[j+1][i-1], intable[j+2][i-2], intable[j+3][i-3]]==w1:
                return 1
            if [intable[j][i], intable[j+1][i-1], intable[j+2][i-2], intable[j+3][i-3]]==w2:
                return 2

#simular to validMoves but with None if the move of that col in not valid
def humanMoves(intable=[]):
    cols=[]; rows=[]
    for col in range(7):
        for row in range(6):
            if intable[row][col]==0:
                cols.append(col)
                rows.append(row)
                break
    return cols, rows

isNum=re.compile("[^0-9]")
#human move for a given col
def hmove(intable, x):
    cols, rows = humanMoves(intable)
    if isNum.match(x)==None and x!='': x=int(x)-1
    while x not in cols:
        print ("INVALID MOVE!!!")
        x=input('n: ')
        if isNum.match(x)==None and x!='': x=int(x)-1
    intable[rows[cols.index(x)]][x]=2

def move(intable,x,who):
    val=availablemove(intable)
    intable[val[x][0]][val[x][1]]=who

def time(): return ((gmtime()[4])*60)+gmtime()[5]


##############GAME##########################
if __name__ == "__main__":

    table = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    table.reverse()

    # GAME
    agent = 0
    player = 0
    first = input("Do you want to play first? (y/n) >> ")
    # the player plays first
    if first == 'y' or first == 'Y':
        draw(table)
        while availablemove(table):
            n = input("n: ")
            hmove(table, n)
            draw(table)
            if win(table) == 2:
                player += 1
                draw(table)
                break

            cStart = time()
            print("Hmmm let me think ?!??!")
            move(table, rule_eval(table), 1)
            draw(table)
            print("After ", time() - cStart, " seconds thinking!")
            if win(table) == 1:
                agent += 1
                break

    # The AI agent plays first
    else:
        while availablemove(table):
            cStart = time()
            print("Hmmm let me think ?!??!")
            move(table, rule_eval(table), 1)
            draw(table)
            print("After ", time() - cStart, " seconds thinking!")
            if win(table) == 1:
                agent += 1
                break

            n = input("n: ")
            hmove(table, n)
            draw(table)
            if win(table) == 2:
                player += 1
                break

    if agent == player:
        print("DRAW")
    else:
        print("AI AGENT ", agent, " : ", player, " PLAYER")


