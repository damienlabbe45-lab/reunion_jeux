
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

def game_nime(liste_user : list[str], i: int,user: str) -> None:
    """fonction permettant de créé le jeu de nime"""
    matches = " "*21
    from utils import input_number_matches_user
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
    from utils import winner
    winner(liste_user[i  % 2])


def game_variation(liste_user : list[str], i: int ,user: str) -> None:
    """fonction permettant de créé le jeu de Marienbad"""
    list_matches = [" ", " " * 3, " " * 5, " " * 7]
    from utils import input_number_matches_user, input_numberheapmatches_user
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
    from utils import winner
    winner(liste_user[i  % 2])
