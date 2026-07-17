from pandas import DataFrame


def user(number: int, liste_number: list[str]) -> tuple[int | str, int | str, int | str]:
    user_col = input(f"veillez indiquer la colonne (de 1 à {number} à partir de la gauche)")
    if user_col in liste_number:
        user_col = int(user_col) - 1
    user_ligne = input(f"veillez indiquer la ligne (de 1 à {number} à partir du haut)")
    if user_ligne in liste_number:
        user_ligne = int(user_ligne) - 1
    user_state = input(f"veillez indiquer le nombre d'étages (de 1 à {number})")
    if user_state in liste_number:
        user_state = int(user_state)
    return user_col, user_ligne, user_state


async def game(matrice: DataFrame, solution: DataFrame, number: int) -> None:
    from utils.utils_gratteciel import print_gratte_ciel, input_resolve
    resolution = True
    while (matrice != solution).any().any():
        print_gratte_ciel(matrice, solution)
        if resolution:
            if input_resolve():
                resolution = False
            else:
                liste_number = [str(i) for i in range(1, number + 1)]
                user_col, user_ligne, user_state = user(number, liste_number)
                if user_col in matrice.columns.values and user_ligne in list(matrice.index) and isinstance(user_state,
                                                                                                           int):
                    matrice.iloc[user_ligne, user_col] = user_state  # type: ignore
        else:
            matrice = auto_resolution(matrice, solution, number)


def auto_resolution(matrice: DataFrame, solution: DataFrame, number: int) -> DataFrame:
    from jeux.auto_resolution_gratteciel import logique_ligne, logique_col, auto_resolp2
    from jeux.creation_gratteciel import  suppr_data
    from utils.utils_gratteciel import generate_indice, print_solution2, initialiser_possibilites, log_to_file
    log_to_file("la solution est:")
    print_solution2(solution)
    log_to_file("voici comment faire:")
    matrice = suppr_data(matrice, number)
    comb = initialiser_possibilites(matrice, number)
    indice_auto = generate_indice(matrice, solution)
    ind_ligne = list(zip(list(indice_auto.index)[:-1], list(indice_auto[''])[:-1]))
    ind_col = list(zip(list(indice_auto.columns)[:-1],
                       list(indice_auto.loc[""])[:-1]))
    liste_number = [int(i) for i in range(1, number + 1)]
    matrice = logique_ligne(matrice.copy(), list(zip(list(indice_auto.index)[:-1],
                                                     list(indice_auto[''])[:-1])),
                            number, liste_number, solution)
    matrice = logique_col(matrice.copy(), list(zip(list(indice_auto.columns)[:-1],
                                                   list(indice_auto.loc[""])[:-1])),  # type: ignore
                          number, liste_number, solution)
    matrice = auto_resolp2(matrice.copy(), solution, comb, ind_ligne, ind_col)  # type: ignore
    if (matrice != solution).any().any():
        from jeux.auto_resolution_gratteciel import run_hypothesis
        from utils.utils_gratteciel import print_gratte_ciel2
        matrice = run_hypothesis(matrice.copy(), solution, comb, {},
                             ind_ligne, ind_col)  # type: ignore
        print_gratte_ciel2(matrice,solution)
        
    return matrice
