def winner(winner:str) -> None:
    if winner == "\n":
        winner = "Ordinateur"
    print(f"{winner} est le grand vainqueur.")


def input_numberheapmatches_user() -> int:
    """demander à l'utilisateur de dire quel tas d'allumette il va utiliser"""
    number = None
    while number is None:
        number = input("Veuillez indiquer le tas que vous allez prendre entre 1 et 4\n")
        if number in ["1", "2", "3", "4"]:
            number =int(number) - 1
        else:
            number = None
    return number


def input_number_matches_user() -> int:
    """demander à l'utilisateur de dire combien d'allumette il enlève"""
    number = None
    while number is None:
        number = input("Veuillez indiquer le nombre d'allumette que vous prenez entre 1 et 4\n")
        if number in ["1", "2", "3", "4"]:
            number =int(number)
        else:
            number = None
    return number