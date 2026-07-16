def print_results(results_run: list[str], type_run: int) -> None:
    """la fonction sert juste à afficher dans l'ordre les chevaux en fonction du type de course"""
    for i, horse in enumerate(results_run[:type_run]):
        if i == 0:
            print(f"en 1er, on a {horse} !!!!")
        else:
            print(f" en {i + 1}ème , on a {horse}")


def input_number_horse() -> int:  # pyright: ignore[reportReturnType]
    """cette fonction permet de connaître le nombre de chevaux souhaités par l'utilisateur"""
    number_horse = None
    while number_horse is None:
        input_user = input("Veillez indiquer s'il vous plaît un nombre de chevaux entre 12 et 20")
        if input_user.isdigit():
            input_user = int(input_user)
            if 12 <= input_user <= 20:
                number_horse = input_user
    if isinstance(number_horse, int):
        return number_horse


def input_type_run() -> int:  # pyright: ignore[reportReturnType]
    """cette fonction permet de connaître le type de course souhaités par l'utilisateur"""
    type_run = None
    while type_run is None:
        input_user = input(
            "Veillez indiquer s'il vous plaît le type de course en mettant 3 pour un tiercé, 4 pour un quarté et 5 "
            "pour un quinté")
        if input_user in ["3", "4", "5"]:
            type_run = int(input_user)
    if isinstance(type_run, int):
        return type_run


def input_user() -> None:
    """fonction servant juste à avancer la course de 10 secondes pour l'utilisateur"""
    input("veillez appuyer pour faire avancer de 10 secondes la course")


def generate_run() -> dict[str, list[int]]:
    """fonction générant un dictionnaire ou la clé est un cheval (horse en aglais signifie cheval) associé 
    à sa distance (la valeur indice 0 en python) et à sa vitesse (valeur indice 1 en python)"""
    number_horse = input_number_horse()
    dict_horse = {}
    for horse in range(1, number_horse + 1):
        dict_horse[f"horse {horse}"] = [0, 0]
    return dict_horse
