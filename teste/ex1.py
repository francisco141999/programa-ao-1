def print_board():
    print "     |     |     "
    print " "+board[1]+" | "+board[2]+" | "+board[3]+" "
    print "     |     |     "
    print " ----|-----|-----"
    print "     |     |     "
    print " "+board[4]+" | "+board[5]+" | "+board[6]+" "
    print "     |     |     "
    print " ----|-----|-----"
    print "     |     |     "
    print " "+board[7]+" | "+board[8]+" | "+board[9]+" "
    print "     |     |     "

while True:
    os.system("Clear")
    print_header()
    print_board()    
    
    choice = raw_input("Please choose an empty space for X")
    choice =int(choice)
    
    board[choice] = "X"
