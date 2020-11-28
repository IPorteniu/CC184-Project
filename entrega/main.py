from Game import Game

players = 0
while players != 2 and players != 4:
    players = int(input("Ingrese cantidad de jugadores: "))

game = Game(players)
game.startgame()
