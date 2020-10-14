import numpy as np

h=8 #по горизонтали
v=8 #по вертикали
#'p': -1, 'r': -2, 'n': -3, 'b': -4, 'q': -5, 'k': -6
figuresw = {1: 'wp', 2: 'wr', 3: 'wn', 4: 'wb', 5: 'wq', 6: 'wk'}
figuresb = {1: 'bp', 2: 'br', 3: 'bn', 4: 'bb', 5: 'bq', 6: 'bk'}

def create_board(h,v):
    bo = np.zeros((h,v)) #board
    for i in range(h):
        bo[i][j] = 0
        #for j in range(v):
            #ch[i][j] = np.zeros(2)
        #    if (i+j)%2==0:
        #        bo[i][j] = 1 #w
        #    else:
        #        bo[i][j] = 0 #b    
    return bo

def ret_col_cell(i,j):
    if (i+j)%2==0:
        return 1 #w
    else:
        return = 0 #b   



bo = create_board(h,v)
fig = np.array([1,2,3])
fig2 = np.array([4,5,6])
qw = [1,2,3]

def create_figures(bo, *params):
    if params[0]=='norm':
        for i in range(8):
            bo[1] = figuresb['p']
            bo[v-1-1] = figuresw['p']
        for i in range(3):
            bo[ 0 ][i] = bo[ 0 ][h-i] = i+1
            bo[v-1][i] = bo[v-1][h-i] = -(i+1)
        bo[ 0 ][3] = -bo[h-1][3] = -5
        bo[ 0 ][4] = -bo[h-1][4] = -6

def sign(a):
    if a>0:
        return 1
    elif a<0:
        return -1
    else:
        return 0

def avail_move(coor,fig, bo):
    s=sign(fig)
    if abs(fig)==1:
        first_step=0
        trans_avail=0 #возможность превратиться
        if ( ((s*coor[0]>0)or(s<0 and coor[0]<v-1)) and (coor[0]-sign(fig)) )==0: #если есть пространство для хода

            if fig>0:
                if coor[0]==v-2:
                    first_step=1
                if coor[0]==1:
                    trans_avail=1
            else:
                if coor[0]==1:
                    first_step=1
                if coor[0]==v-2:
                    trans_avail=1
        
        if coor[1]

        return [(-1,0)]
    if abs(fig)==2:
        return [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]
    if abs(fig)==3:
        return []


def check_avail_fig(bo, color):
    for i in range(h):
        for j in  range(2):
            if color:


def step(bo, fig, cost, init, fin):
    fig = [init, fin, cost ]


                        

for i in range(3):
    print(i)
            
        

