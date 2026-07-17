from pandas import DataFrame
from typing import Any


def create_matrice() -> DataFrame:
    """On cree la grille"""
    from numpy import eye
    return DataFrame(eye(10))


def battleship(matrice: DataFrame) -> DataFrame:
    """On fait en sorte que les lignes commecent à 1 et les colonnes par A"""
    from string import ascii_uppercase
    matrice.columns = list(ascii_uppercase[0:10])
    matrice.index = list(range(1, 11))
    matrice = matrice.astype(str)
    matrice[:] = ""
    return matrice


def verif_coor(coor: list[tuple[Any, Any]], coors_dangerous: list[tuple[Any, Any]], n: int) -> list[tuple[Any, Any]]:
    """filtre les coordonnées donnant à des situtations impossibles à résoudre"""
    dict_string_number = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
    cols_letter = list(dict_string_number.keys())
    valid_coor = []
    for coords in coor:
        col: str = coords[1]
        row: int = coords[0]
        col_num = dict_string_number[col]
        ok_rigth = (col_num + n - 1 <= 10) and all((row, cols_letter[col_num + i - 1]) not in coors_dangerous for i in
                                                   range(n))
        ok_left = (col_num - n + 1 >= 1) and all((row, cols_letter[col_num - i - 1]) not in coors_dangerous for i in
                                                  range(n))
        ok_bottom = (row + n - 1 <= 10) and all((row - i, col) not in coors_dangerous for i in range(n))
        ok_top = (row - n + 1 >= 1) and all((row - i, col) not in coors_dangerous for i in range(n))
        if ok_bottom or ok_left or ok_rigth or ok_top:
            valid_coor.append((row, col))
    return valid_coor


def assign_value(matrice: DataFrame, coor: list[tuple[Any, Any]], value: str) -> DataFrame:
    """met la valeur à toutes les coordonnées dans le dataframe"""
    for row, col in coor:
        if row in matrice.index and col in matrice.columns:
            matrice.loc[row, col] = value
    return matrice


def generate_grille(matrix: DataFrame) -> DataFrame:
    """on choisit aléatoirement les coordonnées de la grille"""
    from secrets import choice
    from utils import find_coor, find_not_coor
    from utils_creation_bataille_navale import append_coor, verify_coor
    list_dir = ["haut", "bas", "droite", "gauche"]
    for length_ship in zip([2, 3, 3, 4, 4, 5],range(1,6)):
        coor = find_coor(matrix, "")
        coords_dangerous = find_not_coor(matrix, "")
        coor = verify_coor(coor, coords_dangerous, 3)
        coor_value: tuple[str, int] = choice(coor)
        list_ship = list_dir[:]
        choose_dir = choice(list_ship)
        coor_values = append_coor(coor_value, coords_dangerous, choose_dir, length_ship[0]-1)
        matrix = assign_value(matrix, coor_values, str(length_ship[1]))
    return matrix