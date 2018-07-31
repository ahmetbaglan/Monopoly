class Board:
    TILE_NAME = [
        "Başlangıç",
        "Kasımpaşa",
        "Kamu Fonu",
        "Dolapdere",
        "Gelir Vergiis",
        "Haydarpaşa İstasyonu",
        "Sultanahmet",
        "Şans",
        "Sirkeci",
        "Karaköy",
        "Ziyaretçi",
        "Hapis",
        "Beyoğlu",
        "Elektrik İdaresi",
        "Beşiktaş",
        "Taksim",
        "Kadıköy İskelesi",
        "Harbiye",
        "Kamu Fonu",
        "Şişli",
        "Mecidiyeköy",
        "Bedava Park",
        "Bostancı",
        "Şans",
        "Erenköy",
        "Caddebostan",
        "Kabataş Vapur İskelesi",
        "Nişantaşı",
        "Teşvikiye",
        "Sular İdaresi",
        "Maçka",
        "Kodsese Git",
        "Levent",
        "Etiler",
        "Kamu Fonu",
        "Bebek",
        "Sirkeci Tren İstasyonu",
        "Şans",
        "Tarabya ",
        "Lüx Vergisi",
        "Yeniköy"
    ]

    color = [
        "Go",
        "Brown",
        "Community",
        "Brown",
        "Tax",
        "Station",
        "Light Blue",
        "Chance",
        "Light Blue",
        "Light Blue",
        "Just Visiting",
        "In Jail",
        "Purple",
        "Community Building",
        "Purple",
        "Purple",
        "Station",
        "Orange",
        "Community",
        "Orange",
        "Orange",
        "Free Parking",
        "Red",
        "Chance",
        "Red",
        "Red",
        "Station",
        "Yellow",
        "Yellow",
        "Community Building",
        "Yellow",
        "Go To Jail",
        "Green",
        "Green",
        "Community",
        "Green",
        "Station",
        "Chance",
        "Dark Blue",
        "Tax",
        "Dark Blue"
    ]

    fiyat = [None, 60, None, 60, None, 200, 100, None, 100, 120, None, None,  140, 150, 140, 160, 200, 180, None, 180, 200,  None,
             220, None, 220, 240, 200, 260,260, 150, 280, None, 300, 300, None, 320, 200, None, 350, None, 400]

    ev = [None, 50, None, 50, None, None, 50, None, 50,50, None, None,  100, None, 100, 100, None, 100, None, 100, 100, None, 150,
          None, 150, 150, None, 150, 150, None, 150, None, 200, 200, None, 200, None, None, 200, None,  200]

    kira0 = [None, 2, None, 4, None, None, 6, None, 6, 8, None, None, 10, None, 10, 12, None, 14, None, 14, 16, None, 18, None,
             18,20, None, 22, 22, None, 24, None, 26, 26, None, 28, None, None, 35, None, 50]

    kira1 = [None, 10, None, 20, None, None, 30, None, 30, 40, None, None, 50, None, 50, 60, None, 70, None, 70, 80, None,
             90, None,  90, 100, None, 110, 110, None, 120, None, 130, 130, None, 150, None, None, 175, None, 200]

    kira2 = [None, 30, None, 60, None, None, 90, None, 90, 100, None, None, 150, None, 150, 180, None, 200, None, 200,
             220, None, 250, None, 250, 300, None, 330, 330, None, 360, None, 390, 390, None, 450, None, None, 500,
             None, 600]

    kira3 = [None, 90, None, 180, None, None, 270, None, 270, 300, None, None, 450, None, 450, 500, None, 550, None, 550,
             600,
             None, 700, None, 700, 750, None, 800, 800, None, 850, None, 900, 900, None, 1000, None, None, 1100, None,
             1400]
    kira4 = [None, 160, None, 320, None, None, 400, None, 400, 350, None, None, 625, None, 625, 700, None, 750, None,
             750,
             800,
             None, 875, None, 875, 925, None, 975, 975, None, 1025, None, 1100, 1100, None, 1200, None, None, 1300, None,
             1700]

    kiraOtel =  [None, 250, None, 450, None, None, 550, None, 550, 600, None, None, 750, None, 750, 900, None, 950, None,
             950,
             1000,
             None, 1050, None, 1050, 1100, None, 1150, 1150, None, 1200, None, 1275, 1275, None, 1400, None, None, 1500, None,
             2000]



    TILES_REAL_ESTATE = [
        1, 3, 6, 8, 9, 12, 14, 15, 17, 19, 20, 22, 24, 25, 27, 28, 30, 32, 33, 35, 38, 40]
    TILES_CHANCE = [7, 23, 37]
    TILES_COMMUNITY = [2, 18, 34]
    TILES_UTILITIES = [13, 29]
    TILES_TRANSPORT = [5, 16, 26, 36]
    TILES_TAX = [4, 39]
    TILES_NONE = [10, 21]
    TILES_JAIL = [11]
    TILES_GO_TO_JAIL = [31]
    TILES_GO = [0]

    def __init__(self):
        # Check if total amount of tiles is correct
        tilesCount = self.getSize()
        if tilesCount != 41:
            print("Game board consists of {0} tiles, instead of 41!".format(tilesCount))

        # Setup array to keep track of times a player had landed on a tile
        self.hits = [0] * 41

    def getTileType(self, tile):
        # Return a string of the type of tile corresponding with the index given
        if tile in Board.TILES_REAL_ESTATE:
            return "realestate"
        elif tile in Board.TILES_CHANCE:
            return "chance"
        elif tile in Board.TILES_COMMUNITY:
            return "community"
        elif tile in Board.TILES_UTILITIES:
            return "utitlities"
        elif tile in Board.TILES_TRANSPORT:
            return "transport"
        elif tile in Board.TILES_TAX:
            return "tax"
        elif tile in Board.TILES_JAIL:
            return "jail"
        elif tile in Board.TILES_GO_TO_JAIL:
            return "gotojail"
        elif tile in Board.TILES_GO:
            return "go"
        else:
            return "none"

    def hit(self, tile):
        # Increment tile hit count in array
        self.hits[tile] += 1

    def getSize(self):
        return (len(Board.TILES_REAL_ESTATE) + len(Board.TILES_CHANCE) +
                len(Board.TILES_COMMUNITY) + len(Board.TILES_UTILITIES) +
                len(Board.TILES_TRANSPORT) + len(Board.TILES_TAX) +
                len(Board.TILES_NONE) + len(Board.TILES_JAIL) +
                len(Board.TILES_GO_TO_JAIL) + len(Board.TILES_GO))
