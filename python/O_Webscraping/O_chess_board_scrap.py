from selenium import webdriver

#URL
chess_com_play = 'https://www.chess.com/play'
driver = webdriver.Firefox(executable_path=r'geckodriver.exe')

#Objects
colors = ('White', 'Black')
ranks = {'Pawn':1, 'Knight':3, 'Bishop':3, 'Rook':5, 'Queen':9, 'King':0 }


class chess_pieces:
    def __init__(self,color,rank,pieces):
        self.color = color
        self.rank = rank
        self.pieces = []
        for color in colors:
            for rank in ranks:
                piece = chess_pieces(color,rank)
                self.pieces.append(piece)
                
    def __str__(self):
        return self.rank + " of " + self.suit
        
class chess_board:
    def __init__(self):
        self.board = []
        vertical_y = ['A','B','C','D','E','F','G','H']
        horizontal_x = ['1','2','3','4','5','6','7','8']
        for x in horizontal_x:
            for y in vertical_y:
                self.board.append(y + x)

print(chess_board())


def chess_com(chess_com_play):
    driver.get(chess_com_play)

def get_board():
    pass



def main():
    Run = True
    while Run:
        
        chess_com(chess_com_play)
        commands = True
        while commands:
            #Wyjście
            input("Press any key to exit...")
            if input:
                Run = False
                driver.close()
                
if __name__ == '__main__':
    main()
    
# https://medium.com/analytics-vidhya/analyzing-chess-positions-with-python-26d73b7c892