
l5 = {}
tmp_l = {}
#5ki_full.txt 6ki_full,txt 7ki_full.txt
for line in open("./과거 eval/old_7ki.txt"):
    state, key = line.split()
    l5[state] = key

four_2 = ['2222']
three_2  = ['0222','2220','2202','2022','02220']
two_2 = ['02020','00220','02200']

four_1 = ['1111']
three_1 = ['0111', '1110', '1101','1011','01110']
two_1 = ['01010','00110','01100']

for key in l5:
    tmp_l[key] = l5[key]

for state in tmp_l:
    for key in two_2:
        if key in state:
            l5[state] = -200
            if key == '02020':
                tmp_state = state.replace('02020','02320')
                if key not in tmp_state:
                    l5[tmp_state] = -10000
                tmp_state = state.replace('02020','32320')
                if key not in tmp_state:
                    l5[tmp_state] = -10000
                tmp_state = state.replace('02020','32323')
                if key not in tmp_state:
                    l5[tmp_state] = -10000
            elif key == '02200' or key == '00220':
                tmp_state = state.replace('02200','32233')
                if key not in tmp_state:
                    l5[tmp_state] = -10000
                tmp_state = state.replace('00220','33223')
                if key not in tmp_state: #02200, 00220이 아닌거면 바꿀 필요 없으니
                    l5[tmp_state] = -10000
    for key in three_2:
        if key in state:
            l5[state] = -200
            tmp_state = state.replace('02220','32220')
            if key not in tmp_state:
                l5[tmp_state] = -10000
            tmp_state = state.replace('02220','02223')
            if key not in tmp_state:
                l5[tmp_state] = -10000
            tmp_state = state.replace('02220','32223')
            if key not in tmp_state:
                l5[tmp_state] = -10000
            tmp_state = state.replace('0222','3222')
            if key not in tmp_state:
                l5[tmp_state] = -10000
            tmp_state = state.replace('2220','2223')
            if key not in tmp_state:
                l5[tmp_state] = -10000
            tmp_state = state.replace('2202','2232')
            if key not in tmp_state:
                l5[tmp_state] = -10000
            tmp_state = state.replace('2022','2322')
            if key not in tmp_state:
                l5[tmp_state] = -10000
    for key in four_2:
        if key in state:
            l5[state] = -10000

for state in tmp_l:
    for key in two_1:
        if key in state:
            l5[state] = 200
            if key == '01010':
                tmp_state = state.replace('01010','01310')
                if key not in tmp_state:
                    l5[tmp_state] = 30
                tmp_state = state.replace('01010','31310')
                if key not in tmp_state:
                    l5[tmp_state] = 40
                tmp_state = state.replace('01010','31313')
                if key not in tmp_state:
                    l5[tmp_state] = 40
            elif key == '01100' or key == '00110':
                tmp_state = state.replace('01100','31133')
                if key not in tmp_state:
                    l5[tmp_state] = 50
                tmp_state = state.replace('00110','33113')
                if key not in tmp_state: #02200, 00220이 아닌거면 바꿀 필요 없으니
                    l5[tmp_state] = 50
    for key in three_1:
        if key in state:
            l5[state] = 200
            tmp_state = state.replace('01110','31110')
            if key not in tmp_state:
                l5[tmp_state] = 50
            tmp_state = state.replace('01110','01113')
            if key not in tmp_state:
                l5[tmp_state] = 50
            tmp_state = state.replace('01110','31113')
            if key not in tmp_state:
                l5[tmp_state] = 10000
            tmp_state = state.replace('0111','3111')
            if key not in tmp_state:
                l5[tmp_state] = 20
            tmp_state = state.replace('1110','1113')
            if key not in tmp_state:
                l5[tmp_state] = 40
            tmp_state = state.replace('1101','1131')
            if key not in tmp_state:
                l5[tmp_state] = 30
            tmp_state = state.replace('1011','1311')
            if key not in tmp_state:
                l5[tmp_state] = 30
    for key in four_1:
        if key in state:
            l5[state] = 10000

#new_l5.txt new_l6.txt, new_l7.txt
f = open('./7ki.txt','w')
for key in l5:
    f.write(key+' ')
    f.write(str(l5[key])+'\n')
