from pandas import DataFrame
from typing import Any


def list_max(liste: list[Any], reversed_bool: bool) -> int:
    # type: ignore
    if reversed_bool:
        liste = list(reversed(liste))
    liste_cons = []
    for i in liste:
        if len(liste_cons) != 0:
            if int(i) > liste_cons[-1]:
                liste_cons.append(int(i))
        else:
            liste_cons.append(int(i))
    return len(liste_cons)


def generate_indice(matrice: DataFrame, solution: DataFrame) -> DataFrame:
    matrice_copie = matrice.copy()
    matrice_copie.columns = [str(list_max(list(solution[i]), False)) for i in matrice.columns]
    matrice_copie.index = [str(list_max(list(solution.loc[i]), False)) for i in matrice.index]
    matrice_copie[''] = [str(list_max(list(solution.loc[i]), True)) for i in matrice.index]
    matrice_copie.loc[""] = [str(list_max(list(solution[i]), True)) for i in matrice] + [""]
    return matrice_copie.copy()


def print_gratte_ciel(matrice: DataFrame, solution: DataFrame) -> None:
    print("\n\n")
    print(generate_indice(matrice, solution))


def print_solution(solution :DataFrame) ->None:
    print("\n\n")
    print(generate_indice(solution, solution))


def input_resolve() -> bool:
    resolution = input("voulez vous la résolution automatique?si oui mettez Y sinon appuyez sur entrée\n").upper()
    return True if resolution == "Y" else False


def log_to_file(chaine: str) -> None:
    """Écrit n'importe quel texte ou message directement dans le fichier de log."""
    #with open("suivi_resolution.txt", "a", encoding="utf-8") as f:
    #    f.write(chaine + "\n")


def print_gratte_ciel2(matrice: DataFrame, solution: DataFrame) -> None:
    """Redirige l'affichage de la grille intermédiaire directement dans le fichier."""
    log_to_file("\n" + generate_indice(matrice, solution).to_string() + "\n")


def print_solution2(solution :DataFrame) ->None:
   log_to_file("\n" + generate_indice(solution, solution).to_string() + "\n")


def find_coor(matrice: DataFrame, chaine: Any) -> list[tuple[int, int]]:
    """Donne les coordonnées (ligne, colonne) ayant la valeur recherchée"""
    grid_size = len(matrice)
    return [
        (row, col) 
        for row in range(grid_size) 
        for col in range(grid_size) 
        if matrice.iloc[row, col] == chaine]


def logic(matrice: DataFrame, solution: DataFrame, col: int | None, index: int | None,
          possibilites: dict[tuple[int, int], set[int]], n: bool, number: int) -> tuple[DataFrame, bool]:
    matrice_copie = matrice.copy()
    coordonnees = []
    for j in range(number):
        r, c = (j, col) if col is not None else (index, j)
        if matrice.iloc[r, c] == "":
            coordonnees.append((r, c))
    for r, c in coordonnees:
        if (r, c) in possibilites and len(possibilites[(r, c)]) == 1:
            target_value = list(possibilites[(r, c)])[0] 
            if len(find_coor(matrice_copie, target_value)) != number:
                matrice_copie.iloc[r, c] = target_value
                del possibilites[(r, c)]
                for i in range(number):
                    if (r, i) in possibilites: possibilites[(r, i)].discard(target_value)
                    if (i, c) in possibilites: potrivit = possibilites[(i, c)].discard(target_value)
                print_gratte_ciel2(matrice_copie, solution)
    coordonnees = [(r, c) for (r, c) in coordonnees if matrice_copie.iloc[r, c] == ""]
    for val in range(1, number + 1):
        cases_possibles = [(r, c) for (r, c) in coordonnees if (r, c) in possibilites and val in possibilites[(r, c)]]
        if len(cases_possibles) == 1:
            r, c = cases_possibles[0]
            if len(find_coor(matrice_copie, val)) != number:
                matrice_copie.iloc[r, c] = val
                del possibilites[(r, c)]
                for i in range(number):
                    if (r, i) in possibilites: possibilites[(r, i)].discard(val)
                    if (i, c) in possibilites: possibilites[(i, c)].discard(val)
                print_gratte_ciel2(matrice_copie, solution)
                
    if (matrice != matrice_copie).any().any():
        n = True
        matrice = matrice_copie.copy()
    return matrice, n


def initialiser_possibilites(matrice: DataFrame, number: int) -> dict[tuple[int, int], set[int]]:
    possibilites = {}
    for r in range(number):
        for c in range(number):
            if matrice.iloc[r, c] == "":
                possibilites[(r, c)] = set(range(1, number + 1))
    for r in range(number):
        for c in range(number):
            valeur = matrice.iloc[r, c]
            if valeur != "":
                valeur_int = int(valeur)
                for i in range(number):
                    if (r, i) in possibilites:
                        possibilites[(r, i)].discard(valeur_int)
                    if (i, c) in possibilites:
                        possibilites[(i, c)].discard(valeur_int)
    return possibilites
