# converts Rezwan vai style #INCLUDE to score_type_parameters

import sys

def to_id(i):
    s = str(i)
    while len(s) < 3: s = '0'+s
    return '('+s+')'

if __name__ == '__main__':
    gen = open(sys.argv[1]).read().split('\n')

    cur_test = 0
    subtasks = []
    subtask = 0

    for line in gen:
        if line.startswith("#ST:"):
            subtasks.append([int(line[4:]), []])
        elif line.startswith("#INCLUDE:"):
            d = int(line[len("#INCLUDE:"):])
            for test in subtasks[d-1][1]:
                subtasks[-1][1].append(test)
        elif len(line) != 0:
            subtasks[-1][1].append(cur_test)
            cur_test+=1
        
    for s in subtasks:
        s[1] = list(set(s[1]))
        s[1] = '|'.join([to_id(x) for x in s[1]])

    
    print('score_type_parameters: ', subtasks)
    
