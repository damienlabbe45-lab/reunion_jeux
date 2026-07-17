from pandas import DataFrame
from typing import Any


def find_coor(matrice: DataFrame, chaine: str) -> list[tuple[Any, Any]]:
    """donne les coordonnées ayant les valeurs de la chaîne"""
    return [(row, col) for row in range(1, 11) for col in "ABCDEFGHIJ" if row in matrice.index and
             col in matrice.columns and matrice.loc[row, col] == chaine]


def find_not_coor(matrice: DataFrame, chaine: str) -> list[tuple[Any, Any]]:
    """donne les coordonnées n'ayant pas la valeur de la chaîne"""
    return [(row, col) for row in range(1, 11) for col in "ABCDEFGHIJ" if row in matrice.index and
             col in matrice.columns and matrice.loc[row, col] != chaine]

