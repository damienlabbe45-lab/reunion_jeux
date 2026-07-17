from pandas import DataFrame


def main():
    from creation import battleship, generate_grille, create_matrice
    from game import game
    matrice: DataFrame = battleship(create_matrice())
    grille_ship = generate_grille(matrice.copy())
    game(grille_ship, matrice)
    print("merci d'avoir jouer")


def user():
    gaming = None
    while gaming is None:
        main()
        gaming = input("Voulez-vous rejouer?\n")
        if gaming == "":
            gaming = None
        else:
            print("à une prochaine fois ^^.")


if __name__ == "__main__":
    user()
