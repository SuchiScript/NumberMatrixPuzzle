import time

newline = "\n"
clrscr = "\033[2J"
rtrn_crsr_home = "\033[H"

print(f"{clrscr}{rtrn_crsr_home}NUMBER MATRIX PUZZLE GAME:{2 * newline}NOTE: Higher the edge length of square pattern more the difficulty level")
print(f"{5 * newline}")
n = int(input("Enter the edge length of square pattern you want to generate:"))

def creating_puzzle(n):
    n2 = n
    puz = [[0 for row in range(n)] for col in range(n)]
    for row in range(1,n+1):
        col = 0
        for col1 in range(row, 1, -1):
            puz[row - 1][col] = col1
            col += 1
        for col2 in range(1, n2+1):
            puz[row - 1][col] = col2
            col += 1
        n2 -= 1
    puz[n-1][n-1] = 0
    return puz

puzzle = creating_puzzle(n)

def display_puzzle():
    puzzle = creating_puzzle(n)
    print(f"{clrscr}{rtrn_crsr_home}Puzzle to solve:")
    for rows in puzzle:
        print(rows)
    time.sleep(5)

def findrow(pzl): # finds the row position of 0 (empty tile)
    for rows in range(len(pzl)):
        if 0 in pzl[rows]:
            return rows

def findcol(pzl): # finds the column position of 0 (empty tile)
    n = len(pzl)
    for rows in range(n):
        for cols in range(n):
            if pzl[rows][cols] == 0:
                return cols
            
def jumbling(pzz, sol):
    n = len(pzz)
    for i in range(n):
        r = findrow(pzz)
        c = findcol(pzz)
        if c != 0:
            pzz[r][c-1], pzz[r][c] = pzz[r][c], pzz[r][c-1]
            c = findcol(pzz)
            sol.append('a')
        if r != 0:
            pzz[r-1][c], pzz[r][c] = pzz[r][c], pzz[r-1][c]
            r = findrow(pzz)
            sol.append('w')
    for i in range(n):
        if c != (n-1):
            pzz[r][c+1], pzz[r][c] = pzz[r][c], pzz[r][c+1]
            c = findcol(pzz)
            sol.append('d')
    for i in range(n):
        if r != (n-1):
            pzz[r+1][c], pzz[r][c] = pzz[r][c], pzz[r+1][c]
            r = findrow(pzz)
            sol.append('s')
        if c != 0:
            pzz[r][c-1], pzz[r][c] = pzz[r][c], pzz[r][c-1]
            c = findcol(pzz)
            sol.append('a')
    for i in range(n):
        if r != 0:
            pzz[r-1][c], pzz[r][c] = pzz[r][c], pzz[r-1][c]
            r = findrow(pzz)
            if sol[-1] == 's':
                sol.pop(-1)
            else:
                sol.append('w')
        if c != (n-1):
            pzz[r][c+1], pzz[r][c] = pzz[r][c], pzz[r][c+1]
            c = findcol(pzz)
            sol.append('d')
        if r != (n-1):
            pzz[r+1][c], pzz[r][c] = pzz[r][c], pzz[r+1][c]
            r = findrow(pzz)
            if sol[-1] == 'w':
                sol.pop(-1)
            else:
                sol.append('s')
        if c != (n-1):
            pzz[r][c+1], pzz[r][c] = pzz[r][c], pzz[r][c+1]
            c = findcol(pzz)
            sol.append('d')
    return pzz
            
def playing(puzzle):
    sol = []
    pzz = jumbling(puzzle, sol) 
    n = len(pzz)
    trgt_puzz = creating_puzzle(n)
    print(f'{clrscr}')
    while pzz != trgt_puzz:
        print(f"{rtrn_crsr_home}Your current PUZZLE is:")
        for rows in pzz:
            print(rows)
        r = findrow(pzz)
        c = findcol(pzz)
        inp1 = input()
        if inp1 == 'w' and r != (n-1):
            pzz[r+1][c], pzz[r][c] = pzz[r][c], pzz[r+1][c]
            if sol[-1] == 'w':
                sol.pop(-1)
            else:
                sol.append('s')
        if inp1 == 's' and r != 0:
            pzz[r-1][c], pzz[r][c] = pzz[r][c], pzz[r-1][c]
            if sol[-1] == 's':
                sol.pop(-1)
            else:
                sol.append('w')
        if inp1 == 'a' and c != (n-1):
            pzz[r][c+1], pzz[r][c] = pzz[r][c], pzz[r][c+1]
            if sol[-1] == 'a':
                sol.pop(-1)
            else:
                sol.append('d')
        if inp1 == 'd' and c != 0:
            pzz[r][c-1], pzz[r][c] = pzz[r][c], pzz[r][c-1]
            if sol[-1] == 'd':
                sol.pop(-1)
            else:
                sol.append('a')
        if inp1 == 'h':
            display_puzzle()
        if inp1 == 'r':
            sol1 = []
            pzz = jumbling(creating_puzzle(n), sol1)
            sol = sol1
        if inp1 == 'k':
            print(f"{clrscr}{rtrn_crsr_home}The solution for the given Puzzle is:")
            print(sol[::-1])
            time.sleep(3.5)
        if inp1 == 'g':
            print(f"{clrscr}{rtrn_crsr_home}You have given up on solving PUZZLE GAME:")
            time.sleep(2)
            for key in sol[::-1]:
                r = findrow(pzz)
                c = findcol(pzz)
                print(f"{clrscr}{rtrn_crsr_home}COMPUTER SOLVING THE PUZZLE:")
                for rows in pzz:
                    print(rows)
                if key == 'w':
                    pzz[r+1][c], pzz[r][c] = pzz[r][c], pzz[r+1][c]
                elif key == 's':
                    pzz[r-1][c], pzz[r][c] = pzz[r][c], pzz[r-1][c]
                elif key == 'a':
                    pzz[r][c+1], pzz[r][c] = pzz[r][c], pzz[r][c+1]
                else:
                    pzz[r][c-1], pzz[r][c] = pzz[r][c], pzz[r][c-1]
                time.sleep(1.5)
            print(f"{clrscr}{rtrn_crsr_home}Your current PUZZLE is:")
            for rows in pzz:
                print(rows)    
            break
        if inp1 == 'q':
            print(f"{clrscr}{rtrn_crsr_home}You have quit the PUZZLE GAME")
            break
    if pzz == trgt_puzz:
        print(f"{clrscr}{rtrn_crsr_home}Your current PUZZLE is:")
        for rows in pzz:
            print(rows)
        time.sleep(3)
        print(f"{clrscr}{rtrn_crsr_home}The PUZZLE GAME is successfully solved.")


print(f"{clrscr}{rtrn_crsr_home}PUZZLE GAME : {newline}Rules to play:")
print("1. '0' is the empty tile in your puzzle")
print("2.  Press w to  move 0 downward")
print("3.  Press s to  move 0 upward")
print("4.  Press a to  move 0 rightward")
print("5.  Press d to  move 0 leftward")
print("6.  Press h to  show taget puzzle")
print("7.  Press r to  reset the puzzle")
print("8.  Press k to  view answer key of the puzzle")
print("9.  Press g to  give up and let computer solve the puzzle")
print("10. Press q to  quit the game")

print(f"{5*newline}")

inp = input("Enter c to continue or q to quit:")
if inp == "c":
    display_puzzle()
    playing(puzzle)
if inp == "q":
    print(f"{clrscr}{rtrn_crsr_home}You have quit the PUZZLE GAME")