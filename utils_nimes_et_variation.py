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


def choice_computer_matches(number_matches: int) -> int:
    """choix de l'ordinateur pour les allumettes"""
    if number_matches % 5 != 1 and number_matches > 5:
        number = 5 - number_matches % 5 
    elif 1 < number_matches <= 5:
        number = number_matches - 1
    else:
        from secrets import choice
        number = choice(list(range(1, min(5, number_matches + 1))))
    return number


def choice_computer_heap_matches(list_heap_matches:list[str]) -> int :
    """fonction permettant à l'ordinateur de choisir le tas d'allumette"""
    heap_matches = [heap for heap in list_heap_matches if len(heap)> 1]
    if len(heap_matches) > 1:
        from secrets import choice
        heap = list_heap_matches.index(choice(heap_matches))
    elif len(heap_matches) == 1:
        heap = list_heap_matches.index(heap_matches[0])
    else:
        heap = 0
    return heap