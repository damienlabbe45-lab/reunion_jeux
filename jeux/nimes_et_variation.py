def game_nime(liste_user : list[str], i: int,user: str) -> None:
    """fonction permettant de créé le jeu de nime"""
    matches = " "*21
    from utils.utils_nimes_et_variation import choice_computer_matches
    from utils.utils_main import input_number_user
    while len(matches) > 0:
        print(f"il reste {len(matches)} allumettes")
        if user != "\n":
            print(f"{user} , c'est à vous de jouer")
            number_matches = input_number_user(4,"Veuillez indiquer le nombre d'allumette que vous prenez entre 1 et 4\n" , False)
        else:
            print("Ordinateur, c'est à vous de jouer")
            number_matches = choice_computer_matches(len(matches))
        if len(matches) >= number_matches:
            matches = matches[number_matches:]
            i +=1
        user = liste_user[i % 2]
    from utils.utils_nimes_et_variation import winner
    winner(liste_user[i  % 2])


def game_variation(liste_user : list[str], i: int ,user: str) -> None:
    """fonction permettant de créé le jeu de Marienbad"""
    list_matches = [" ", " " * 3, " " * 5, " " * 7]
    from utils.utils_nimes_et_variation import  choice_computer_matches, choice_computer_heap_matches
    from utils.utils_main import input_number_user
    while all(len(heap) >0 for heap in list_matches):
        for heap in range(1,5):
            print(f" le tas numéro  {heap} a {len(list_matches[heap - 1])}")
        if user != "\n":
            print(f"{user} , c'est à vous de jouer")
            heap_matches = input_number_user(4, "Veuillez indiquer le tas que vous allez prendre entre 1 et 4\n", True)
            number_matches = input_number_user(4,"Veuillez indiquer le nombre d'allumette que vous prenez entre 1 et 4\n" , False)
        else:
            print("Ordinateur, c'est à vous de jouer")
            heap_matches = choice_computer_heap_matches(list_matches)
            number_matches = choice_computer_matches(len(list_matches[heap_matches]))
        if len(list_matches[heap_matches]) >= number_matches:
            list_matches[heap_matches] = list_matches[heap_matches][number_matches:]
            i +=1
        user = liste_user[i % 2]
    from utils.utils_nimes_et_variation import winner
    winner(liste_user[i  % 2])
