from pandas import DataFrame


def main():
    from creation import battleship, generate_grille, create_matrice
    from game import game
    matrice: DataFrame = battleship(create_matrice())
    grille_ship = generate_grille(matrice.copy())
    game(grille_ship, matrice)
    