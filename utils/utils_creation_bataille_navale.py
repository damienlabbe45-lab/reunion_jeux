from typing import Any


def append_coor(coor: tuple[Any, Any], coors_dangerous: list[tuple[Any, Any]], direction: str, n: int #NOSONAR
                ) -> list[tuple[Any, Any]]: # pyright: ignore[reportReturnType]
    """Prend toutes les coordonnées d'un bateau en fonction de sa taille sans jamais la modifier"""
    dict_string_number = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
    cols_letter = list(dict_string_number.keys())
    start_row, start_col = coor[0], coor[1]
    start_col_idx = cols_letter.index(start_col)
    directions_test = [direction] + [d for d in ["droite", "gauche", "haut", "bas"] if d != direction]
    for d in directions_test:
        candidate_path = [coor]
        est_valide = True
        for i in range(1, n + 1):
            if d == "droite":
                next_row = start_row
                next_col_idx = start_col_idx + i
            elif d == "gauche":
                next_row = start_row
                next_col_idx = start_col_idx - i
            elif d == "bas":
                next_row = start_row + i
                next_col_idx = start_col_idx
            elif d == "haut":
                next_row = start_row - i
                next_col_idx = start_col_idx
            if next_row < 1 or next_row > 10 or next_col_idx < 0 or next_col_idx >= 10:
                est_valide = False
                break
            next_coor = (next_row, cols_letter[next_col_idx])
            if next_coor in coors_dangerous:
                est_valide = False
                break
            candidate_path.append(next_coor)
        if est_valide:
            return candidate_path


def verify_coor(coor: list[tuple[Any, Any]], coors_dangerous: list[tuple[Any, Any]], n: int) -> list[tuple[Any, Any]]:
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