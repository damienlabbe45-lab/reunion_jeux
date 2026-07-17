from pandas import DataFrame
from utils.utils_gratteciel import print_gratte_ciel2, log_to_file


def logique_ligne(matrice: DataFrame, ind_ligne: list[tuple[str, str]], number: int, liste_number: list[int],
                  solution: DataFrame) -> DataFrame:
    log_to_file("on regarde les lignes")
    for i, ligne in enumerate(ind_ligne):
        if ligne[0] == str(number):
            matrice.iloc[i, :] = liste_number
            print_gratte_ciel2(matrice, solution)
        elif ligne[1] == str(number):
            matrice.iloc[i, :] = list(reversed(liste_number))
            print_gratte_ciel2(matrice, solution)
        elif ligne[0] == '1':
            matrice.iloc[i, 0] = number
            print_gratte_ciel2(matrice, solution)
        elif ligne[1] == '1':
            matrice.iloc[i, number - 1] = number
            print_gratte_ciel2(matrice, solution)
        elif ligne[0] == str(liste_number[-2]):
            matrice.iloc[i, number - 2] = number
            print_gratte_ciel2(matrice, solution)
        elif ligne[1] == str(liste_number[-2]):
            matrice.iloc[i, 1] = number
            print_gratte_ciel2(matrice, solution)
    return matrice


def logique_col(matrice: DataFrame, ind_col: list[tuple[str, str]], number: int, liste_number: list[int],
                solution: DataFrame) -> DataFrame:
    log_to_file("on regarde les colonnes")
    for i, col in enumerate(ind_col):
        if col[0] == str(number):
            matrice.iloc[:, i] = liste_number
            print_gratte_ciel2(matrice, solution)
        elif col[1] == str(number):
            matrice.iloc[:, i] = list(reversed(liste_number))
            print_gratte_ciel2(matrice, solution)
        elif col[0] == '1':
            matrice.iloc[0, i] = number
            print_gratte_ciel2(matrice, solution)
        elif col[1] == '1':
            matrice.iloc[number - 1, i] = number
            print_gratte_ciel2(matrice, solution)
        elif col[0] == str(liste_number[-2]):
            matrice.iloc[number - 2, i] = number
            print_gratte_ciel2(matrice, solution)
        elif col[1] == str(liste_number[-2]):
            matrice.iloc[1, i] = number
            print_gratte_ciel2(matrice, solution)
    return matrice


def auto_resolp2(matrice: DataFrame, solution: DataFrame, possibilites: dict[tuple[int, int], set[int]],
                 ind_ligne: list[tuple[str, str]], ind_col: list[tuple[str, str]]) -> DataFrame | None:
    from utils.utils_gratteciel import logic, list_max
    from itertools import permutations
    number = len(matrice)
    n: bool = True
    log_to_file("on fait les déductions")
    while n:
        n = False
        for i in matrice.columns:
            idx_col = int(i)
            col_data = list(matrice[i])
            chiffres_presents = {int(x) for x in col_data if x != ""}
            chiffres_manquants = [x for x in range(1, number + 1) if x not in chiffres_presents]
            if len(chiffres_manquants) > 8:
                continue
            perms_valides = []
            for p in permutations(chiffres_manquants):
                it = iter(p)
                tentative = [int(x) if x != "" else next(it) for x in col_data]
                if list_max(tentative, False) == int(ind_col[idx_col][0]) and list_max(tentative, True) == int(ind_col[idx_col][1]):
                    perms_valides.append(tentative)
            if not perms_valides and "" in col_data:
                return None 
            for r in range(number):
                if matrice.iloc[r, idx_col] == "":
                    valeurs_perm = {p[r] for p in perms_valides}
                    possibilites[(r, idx_col)] = possibilites[(r, idx_col)].intersection(valeurs_perm)
                    if not possibilites[(r, idx_col)]:
                        return None
            matrice, n = logic(matrice.copy(), solution, idx_col, None, possibilites, n, number)
        for i in matrice.index:
            idx_row = int(i)
            row_data = list(matrice.iloc[idx_row, :])
            chiffres_presents = {int(x) for x in row_data if x != ""}
            chiffres_manquants = [x for x in range(1, number + 1) if x not in chiffres_presents]
            if len(chiffres_manquants) > 8:
                continue
            perms_valides = []
            for p in permutations(chiffres_manquants):
                it = iter(p)
                tentative = [int(x) if x != "" else next(it) for x in row_data]
                if list_max(tentative, False) == int(ind_ligne[idx_row][0]) and list_max(tentative, True) == int(ind_ligne[idx_row][1]):
                    perms_valides.append(tentative)
            if not perms_valides and "" in row_data:
                return None
            for c in range(number):
                if matrice.iloc[idx_row, c] == "":
                    valeurs_perm = {p[c] for p in perms_valides}
                    possibilites[(idx_row, c)] = possibilites[(idx_row, c)].intersection(valeurs_perm)
                    if not possibilites[(idx_row, c)]:
                        return None
            matrice, n = logic(matrice.copy(), solution, None, idx_row, possibilites, n, number)
    return matrice


def run_hypothesis(matrix: DataFrame, solution: DataFrame, combinations: dict[tuple[int, int], set[int]],
                   tested_hypotheses: dict[tuple[int, int], list[int]],
                   row_indicators: list[tuple[str, str]], col_indicators: list[tuple[str, str]]) -> DataFrame:
    from secrets import choice
    from utils.utils_gratteciel import find_coor, print_gratte_ciel, print_gratte_ciel2, print_solution, log_to_file
    from jeux.auto_resolution_gratteciel import auto_resolp2
    from copy import deepcopy
    matrix_copy = matrix.copy()
    grid_size = len(matrix)
    possibilites = deepcopy(combinations)
    hist_matrix = []
    hypo_counter = 0
    tested_hypotheses = deepcopy(tested_hypotheses)
    while (matrix_copy != solution).any().any():
        empty_cells = find_coor(matrix_copy, "")
        if not empty_cells:
            log_to_file("Grille pleine mais incorrecte. Backtracking...")
            matrix_copy, possibilites, tested_hypotheses = hist_matrix.pop()
            print_gratte_ciel2(matrix_copy, solution)
            continue
        selected_cell = None
        min_candidates_count = float('inf')
        for cell in empty_cells:
            if cell in possibilites:
                candidates = [v for v in possibilites[cell] if cell not in tested_hypotheses or v not in tested_hypotheses[cell]]
                options_count = len(candidates)
                if options_count == 0:
                    min_candidates_count = 0
                    selected_cell = None
                    break
                if options_count < min_candidates_count:
                    min_candidates_count = options_count
                    selected_cell = cell
        if selected_cell is None or min_candidates_count == 0:
            log_to_file("Aucune option valide trouvée pour les cases restantes (Impasse). Backtracking...")
            matrix_copy, possibilites, tested_hypotheses = hist_matrix.pop()
            print_gratte_ciel2(matrix_copy, solution)
            continue
        row_idx, col_idx = selected_cell
        candidate_values = [v for v in possibilites[selected_cell] if selected_cell not in tested_hypotheses or v not in 
                            tested_hypotheses[selected_cell]]
        if len(candidate_values) > 1:
            chosen_value = choice(candidate_values)
        elif len(candidate_values) == 1:
            chosen_value = candidate_values[0]
        else:
            log_to_file("Impasse sur les valeurs candidates. Reset...")
            matrix_copy,possibilites, tested_hypotheses = hist_matrix.pop()
            print_gratte_ciel2(matrix_copy, solution)
            continue
        if selected_cell not in tested_hypotheses:
            tested_hypotheses[selected_cell] = [chosen_value]
        else:
            tested_hypotheses[selected_cell].append(chosen_value)
        hist_matrix.append((matrix_copy.copy(), deepcopy(possibilites), deepcopy(tested_hypotheses)))
        matrix_copy.iloc[selected_cell] = chosen_value
        del possibilites[selected_cell]
        for i in range(grid_size):
            if (row_idx, i) in possibilites: 
                possibilites[(row_idx, i)].discard(chosen_value)
            if (i, col_idx) in possibilites: 
                possibilites[(i, col_idx)].discard(chosen_value)
        log_to_file(f"Hypothèse ciblée sur ({row_idx + 1}, {col_idx + 1}) : {chosen_value} ({min_candidates_count} choix possibles).")
        print_gratte_ciel2(matrix_copy, solution)
        dico_copie = deepcopy(possibilites)
        next_matrix = auto_resolp2(matrix_copy.copy(), solution, dico_copie, row_indicators, col_indicators)
        if next_matrix is None:
            log_to_file("Impasse logique détectée juste après l'hypothèse. Backtracking...")
            matrix_copy, possibilites, tested_hypotheses = hist_matrix.pop()
            print_gratte_ciel2(matrix_copy, solution)
            continue 
        matrix_copy = next_matrix
        possibilites = dico_copie
        hypo_counter += 1
        if hypo_counter % 50 == 0:
            print_gratte_ciel(matrix_copy, solution)
            print_solution(solution)
    return matrix_copy