l4 = {}
old_l4 = {}

for line in open("./eval/4ki.txt"):
    state, key = line.split()
    l4[state] = int(key)

for line in open("./eval/old_4ki.txt"):
    state, key = line.split()
    old_l4[state] = int(key)

for state in l4:
    for o_state in old_l4:
        if state == o_state:
            print(l4[state],type(l4[state]))
            print(old_l4[o_state], type(old_l4[o_state]))
            print((l4[state] + old_l4[o_state]) / 2)
            l4[state] = int((l4[state] + old_l4[o_state]) / 2)

f = open('./eval/new_4ki.txt','w')
for state in l4:
    f.write(state+' ')
    f.write(str(l4[state])+'\n')