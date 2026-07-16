def input_name_user() -> str:
    """fonction servant à demander à l'utilisateur de mettre un nom"""
    return input("entrez votre nom")


def choice_game_user() -> str:
    """permet de savoir quel jeu ce sera"""
    game = None
    while game is None:
        game = input("Veuillez indiquer le jeu (nime ou Marienbad ou pmu ou le compte est bon)\n")
        if game not in ["nime", "Marienbad", "pmu", "le compte est bon"] :
            game = None
    return game


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


def game_setup() -> None:
    """prépare les variables ainsi que les configurations si c'est pour jouer contre l'ordi ou pas"""
    from secrets import choice
    from horse import generate_run
    from le_compte_est_bon import game
    from nimes_et_variation import game_nime, game_variation
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
