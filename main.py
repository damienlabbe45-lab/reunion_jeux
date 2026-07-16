from secrets import choice, SystemRandom
from pandas import DataFrame


def input_name_user() -> str:
    """fonction servant à demander à l'utilisateur de mettre un nom"""
    return input("entrez votre nom")


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


def input_number_user() -> int:
    """permet de savoir combien de joueurs il aura"""
    number = None
    while number is None:
        number = input("Veuillez indiquer le nombre de joueurs (1 ou 2)\n")
        if number in ["1", "2"]:
            number =int(number)
        else:
            number = None
    return number


def choice_computer_matches(number_matches: int) -> int:
    """choix de l'ordinateur"""
    if number_matches % 5 != 1 and number_matches > 5:
        number = 5 - number_matches % 5 
    elif 1 < number_matches <= 5:
        number = number_matches - 1
    else:
        number = choice(list(range(1, min(5, number_matches + 1))))
    return number


def choice_computer_heap_matches(list_heap_matches:list[str]) -> int :
    """fonction permettant à l'ordinateur de choisir le tas d'allumette"""
    heap_matches = [heap for heap in list_heap_matches if len(heap)> 1]
    if len(heap_matches) > 1:
        heap = list_heap_matches.index(choice(heap_matches))
    elif len(heap_matches) == 1:
        heap = list_heap_matches.index(heap_matches[0])
    else:
        heap = 0
    return heap


def choice_game_user() -> str:
    """permet de savoir quel jeu ce sera"""
    game = None
    while game is None:
        game = input("Veuillez indiquer le jeu (nime ou Marienbad ou pmu ou le compte est bon)\n")
        if game not in ["nime", "Marienbad", "pmu", "le compte est bon"] :
            game = None
    return game


def game_setup() -> None:
    """prépare les variables ainsi que les configurations si c'est pour jouer contre l'ordi ou pas"""
    game_choice = choice_game_user()
    number_user = input_number_user()
    liste_user = []
    for _ in range(number_user):
        liste_user.append(input_name_user())
    if number_user == 1:
        liste_user.append("\n")
    user = choice(liste_user)
    i = liste_user.index(user)
    if game_choice == "nime":
       game_nime(liste_user, i ,  user)
    elif game_choice == "Marienbad":
        game_variation(liste_user, i , user)
    elif game_choice == "pmu":
        generate_run()
    else:
        game()


def game_nime(liste_user : list[str], i: int,user: str) -> None:
    """fonction permettant de créé le jeu de nime"""
    matches = " "*21
    while len(matches) > 0:
        print(f"il reste {len(matches)} allumettes")
        if user != "\n":
            print(f"{user} , c'est à vous de jouer")
            number_matches = input_number_matches_user()
        else:
            print("Ordinateur, c'est à vous de jouer")
            number_matches = choice_computer_matches(len(matches))
        if len(matches) >= number_matches:
            matches = matches[number_matches:]
            i +=1
        user = liste_user[i % 2]
    winner(liste_user[i  % 2])


def game_variation(liste_user : list[str], i: int ,user: str) -> None:
    """fonction permettant de créé le jeu de Marienbad"""
    list_matches = [" ", " " * 3, " " * 5, " " * 7]
    while all(len(heap) >0 for heap in list_matches):
        for heap in range(1,5):
            print(f" le tas numéro  {heap} a {len(list_matches[heap - 1])}")
        if user != "\n":
            print(f"{user} , c'est à vous de jouer")
            heap_matches = input_numberheapmatches_user()
            number_matches = input_number_matches_user()
        else:
            print("Ordinateur, c'est à vous de jouer")
            heap_matches = choice_computer_heap_matches(list_matches)
            number_matches = choice_computer_matches(len(list_matches[heap_matches]))
        if len(list_matches[heap_matches]) >= number_matches:
            list_matches[heap_matches] = list_matches[heap_matches][number_matches:]
            i +=1
        user = liste_user[i % 2]
    winner(liste_user[i  % 2])


def winner(winner:str) -> None:
    if winner == "\n":
        winner = "Ordinateur"
    print(f"{winner} est le grand vainqueur.")


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


def run_horse() -> None:
    """fonction servant à faire la course avec les chevaux"""
    dict_horse = generate_run()
    type_run = input_type_run()
    results_run = []
    while dict_horse is not None and len(dict_horse) > 0:
        input_user()
        dict_horse, results_run = secrets_run_horse(dict_horse.copy(), results_run)
    print_results(results_run, type_run)


def secrets_run_horse(dict_horse: dict[str, list[int]], results_run: list[str]):
    """c'est dans cette fonction qu'on décide de la vitesse d'un cheval et si il est dq ou pas. mais chut,
    ca doit rester secret"""
    results_speed = DataFrame(data=[[0, 1, 1, 1, 2, 2], [0, 0, 1, 1, 1, 2], [0, 0, 1, 1, 1, 2], [-1, 0, 0, 1, 1, 1],
                                [-1, 0, 0, 0, 1, 1], [-2, -1, 0, 0, 0, 1], [-2, -1, 0, 0, 0, "DQ"]],
                          columns=list(range(1, 7)))
    speed_horse = [0, 23, 46, 69, 92, 115, 138]
    dict_horse_copy = dict_horse.copy()
    for horse in dict_horse:
        value = SystemRandom().randint(1, 6)  #NOSONAR
        value_speed = results_speed.loc[dict_horse_copy[horse][1], value]
        if not isinstance(value_speed, str):
            dict_horse_copy[horse][1] += int(value_speed) # pyright: ignore[reportArgumentType]
            dict_horse_copy[horse][0] += speed_horse[dict_horse_copy[horse][1]]
            print(f'{horse:<10} vient de parcourir {dict_horse_copy[horse][0]} mètres !!!!!!!!!!!!!!!!!!!')
            position = min(int(dict_horse_copy[horse][0] / 2400 * 40), 40)
            inside_track = "=" * position + ">" + "-" * (40 - position)
            print(f"{horse:<10} {inside_track}")
            print()
            if dict_horse_copy[horse][0] >= 2400:
                print(f"{horse} vient de franchir la ligne d'arrivée !!!!!!!!!!!!!")
                results_run.append(horse)
                del dict_horse_copy[horse]
        else:
            del dict_horse_copy[horse]
            print(f"{horse} a été dq car il est au galop.")
    return dict_horse_copy, results_run


def print_results(results_run: list[str], type_run: int) -> None:
    """la fonction sert juste à afficher dans l'ordre les chevaux en fonction du type de course"""
    for i, horse in enumerate(results_run[:type_run]):
        if i == 0:
            print(f"en 1er, on a {horse} !!!!")
        else:
            print(f" en {i + 1}ème , on a {horse}")


def random_numbers() -> tuple[int, list[int]]:
    return (SystemRandom().randint(101, 999),  #NOSONAR
            [SystemRandom().randint(1, 10) for _ in range(2)] + [25, 50, 75, 100])  #NOSONAR


def input_numbers(numbers: list[int]) -> list[int]:
    """cette fonction permet de connaître les nombres souhaités par l'utilisateur 
    le {', '.join(f'{i}' for i in number_list )}} provient de {', '.join(f':r{i}' for i in range(len(roles)))}
    (vient de mon projet personnel)"""
    numbers_user: list[int] = []
    while len(numbers_user) != 2:
        number_list = [i for i in numbers if i not in numbers_user]
        input_user = input(f"Veuillez indiquer un nombre parmi ceux-ci : {', '.join(f'{i}' for i in number_list)} \n")
        if input_user.isdigit():
            input_user = int(input_user)
            if input_user in number_list:
                numbers_user.append(input_user)
    return numbers_user


def input_operator() -> str:
    """cette fonction renvoie l'opération souhaitée par l'utilisateur"""
    operator_input = None
    while operator_input is None:
        operator_input = input("Veuillez mettre + ou - ou * ou / \n")
        if operator_input not in ["+", "-", "*", "/"]:
            operator_input = None
    return operator_input


def user_break(list_numbers: list[int]) -> None | int:
    """cette fonction demande à l'utilisateur si il veut s'arrêter ou pas et si il s'arrête quel nombre il choisit"""
    number = None
    if input("Voulez vous continuer ? si oui taper y ou Y sinon appuyez ailleurs sur d'autres touches."
             " et appuier sur entrée dans tout les cas à la fin").upper() != "Y":
        while number is None:
            input_user = input(
                f"Veuillez indiquer un nombre parmis ceux-ci : {', '.join(f'{i}' for i in list_numbers)} \n")
            if input_user.isdigit():
                input_user = int(input_user)
            if input_user in list_numbers:
                number = input_user
    return number


def arithmetic_operation(numbers: list[int], operation: str) -> int:
    number = 0
    if operation == "+":
        number = sum(numbers)
    elif operation == "*":
        number = numbers[0] * numbers[1]
    elif operation == "-":
        number = numbers[0] - numbers[1]
    elif operation == "/":
        number = int(numbers[0] / numbers[1])
    return number


def game() -> None:
    """cette fonction sert pour jouer au compte est bon."""
    number_choice, liste_number = random_numbers()
    number_user = None
    while number_user is None:
        print(number_choice)
        print(liste_number)
        number_user = user_break(liste_number)
        if number_user is None:
            numbers = input_numbers(liste_number)
            operator = input_operator()
            list(map(liste_number.remove,numbers))
            liste_number.append(arithmetic_operation(numbers, operator))
            if len(liste_number) == 1:
                number_user = liste_number[0]
    if number_choice == number_user:
        print("le compte est bon")
    else:
        print("vous n'avez fait que vous approcher du résultat du nombre")


def main() -> None:
    user = None
    while user is None:
        game_setup()
        user = input(
            "voulez vous recommencer à jouer? si oui tapez sur la touche entrée sinon tapez sur n'importe quel touche "
            "du clavier")
        if user == "":
            user = None
    print("Merci d'avoir joué")


if __name__ == '__main__':
    main()
