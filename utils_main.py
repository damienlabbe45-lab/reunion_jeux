def input_name_user() -> str:
    """fonction servant à demander à l'utilisateur de mettre un nom"""
    return input("entrez votre nom")


def choice_game_user() -> str:
    """permet de savoir quel jeu ce sera"""
    game = None
    while game is None:
        game = input("Veuillez indiquer le jeu (nime ou Marienbad ou pmu ou le compte est bon)\n")
        if game not in ["nime", "Marienbad", "pmu", "le compte est bon", "bataille navale", "gratteciel"] :
            game = None
    return game


def input_number_user(number_use: int, prompt: str, boole_ind: bool) -> int:
    """demander à l'utilisateur de dire quel nombre il va utiliser"""
    number = None
    while number is None:
        number = input(prompt)
        if number in [str(i) for i in range(1, number_use + 1)]:
            if boole_ind:
                number =int(number) - 1
            else:
                number =int(number)
        else:
            number = None
    return number