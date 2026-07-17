from pandas import DataFrame


def war_ship():
    from creation import battleship, generate_grille, create_matrice
    matrice: DataFrame = battleship(create_matrice())
    grille_ship = generate_grille(matrice.copy())
    game(grille_ship, matrice)


def input_resolve(columns: list[str]) -> tuple[str, int]:
    """fonction servant à avoir les inputs du joueur jusqu'à qu'il met des coordonnées valides"""
    number = None
    while number is None:
        user = input("veillez indiquer les coordonnées pour tirer\n").upper()
        if user[0] not in columns:
            print("veillez mettre A, B , C, D, E, F, G, H, I, J, au tout début. ce sera le nom de colonne")
        elif user[1:].isdigit():
            number = int(user[1:])
            if not (0 < number < 11):
                number = None
                print("Veillez mettre un nombre entre 1 et 10 après les colonnes")
    return user[0], number


def game(matrice: DataFrame, matrice_user: DataFrame) -> None:
    """fonction pour faire tourner le jeu jusqu'à qu'on gagne"""
    from utils_bataille_navale import find_coor, find_not_coor
    while find_not_coor(matrice, "") != find_coor(matrice_user, "x"):
        print(matrice_user)
        col, row = input_resolve(list(matrice_user.columns))
        if matrice.loc[row, col] != "":
            matrice_user.loc[row, col] = "x"
            print("touché")
        else:
            matrice_user.loc[row, col] = "#"
            print("loupé")
