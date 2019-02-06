# Kelas kartu

class Cards :

    index = 0
    gambar = "X"

    def __init__(self,index) :
        if ( index > 0 and index <= 13 ) :
            self.index = index + 1
            self.gambar = "Diamonds"
        elif ( index > 13 and index <= 26 ) :
            self.index = 27 - index + 1
            self.gambar = "Clubs"
        elif ( index > 26 and index <= 39 ) :
            self.index = 40 - index + 1
            self.gambar = "Hearts"
        elif ( index > 39 and index <= 52 ) :
            self.index = 53 - index + 1
            self.gambar = "S"
        else :
            pass

    def getValue(self) :
        if ((self.index < 11) and (self.index > 1)) :
            return self.index
        elif (self.index == 11):
            return "J"
        elif (self.index == 12):
            return "Q"
        elif (self.index == 13):
            return "K"
        elif (self.index ==14):
            return "A"

    def getSymbol(self) :
        return self.gambar[0]
