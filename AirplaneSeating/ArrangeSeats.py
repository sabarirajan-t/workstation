#initialize all the seats
def construct(seatsGrid):
    seats = []
    for i in seatsGrid:
        rows = i[1]
        cols = i[0]
        mat = []
        for i in range( rows ):
            mat.append( [-1] * cols )
        seats.append( mat )
    return seats
#for printing the seats
def printSeats(seats):
    blksize = len( str( number ) )
    rows = [x[1] for x in seatsGrid]
    cols = [x[0] for x in seatsGrid]
    maximum = max( rows )
    top = True
    for i in range( maximum ):
        rowlist = []
        rowlistl = []
        for j in range( length ):
            row = ' '
            rowl = ' '
            if len( seats[j] ) <= i:
                for k in range( cols[j] ):
                    row += ' ' * blksize
                    rowl += ' ' * blksize
                    row += ' '
                    rowl += ' '
            else:
                row = ''
                rowl = ''
                for k in seats[j][i]:
                    if k == -1:
                        row += ' ' * blksize
                        rowl += ' ' * blksize
                        row += ' '
                        rowl += ' '
                    else:
                        row += str( k ) + (' ' * (blksize - len( str( k ) )))
                        rowl += ' ' * blksize
                        row += ' '
                        rowl += ' '
        
            rowlist.append( row )
        rowlistl.append( rowl )
        if top:
            print( '    '.join( rowlistl ) )
            top = False
        print( '    '.join( rowlist ) )
        print( '    '.join( rowlistl ) )
#filling aisle seats
def fill_aisle_seats():
    global filled
    row = 0
    tempFilled = -1
    while filled < number and filled != tempFilled:
        tempFilled = filled
        for i in range( length ):
            if seatsGrid[i][1] > row:
                if i == 0 and seatsGrid[i][0] > 1:
                    filled += 1
                    aisleCol = seatsGrid[i][0] - 1
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                elif i == length - 1 and seatsGrid[i][0] > 1:
                    filled += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                else:
                    filled += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                    if seatsGrid[i][0] > 1:
                        filled += 1
                        aisleCol = seatsGrid[i][0] - 1
                        seats[i][row][aisleCol] = filled
                        if filled >= number:
                            break
        row += 1
#filling window seats
def fill_window_seats():
    row = 0
    global filled
    global number
    tempFilled = 0
    while filled < number and filled != tempFilled:
        tempFilled = filled
        if seatsGrid[0][1] > row:
            filled += 1
            window = 0
            seats[0][row][window] = filled
            if filled >= number:
                break
        if seatsGrid[length - 1][1] > row:
            filled += 1
            window = seatsGrid[length - 1][0] - 1
            seats[length - 1][row][window] = filled
            if filled >= number:
                break
        row += 1
#filling middle seats
def fill_middle_seats():
    row = 0
    tempFilled = 0
    global filled
    while filled < number and filled != tempFilled:
        tempFilled = filled
        for i in range( length ):
            if seatsGrid[i][1] > row:
                if seatsGrid[i][0] > 2:
                    for col in range( 1, seatsGrid[i][0] - 1 ):
                        filled += 1
                        if filled<=number:
                            seats[i][row][col] = filled
                        if filled >= number:
                            break
        row += 1

#number of blocks or sets of seats
way=int(input("Enter the number of blocks of seats: "))
filled = 0
row = 0
tempFilled = -1
seatsGrid=[ ]
#getting size of each block
for i in range(way):
    s=[]
    print("\n")
    s.append(int(input( "Enter the row value:")))
    s.append(int(input("Enter the column value:")))
    seatsGrid.append(s)
#seatsGrid = [[3, 2], [4, 3], [2, 3], [3, 4]] sample seat-grid given in the problem document

#getting number of passengers to assign
number = int(input("Enter the number of passengers:"))
seats = construct( seatsGrid )
length = len( seatsGrid )
#filling aisle seats
fill_aisle_seats()
#filling window seats
fill_window_seats()
#filling center seats
row = 0
tempFilled = 0
fill_middle_seats()
#printing the filled seats
printSeats( seats )
