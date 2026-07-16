def game_setup() -> None:
    """prépare les variables ainsi que les configurations si c'est pour jouer contre l'ordi ou pas"""
    from secrets import choice
    from horse import run_horse
    from le_compte_est_bon import game
    from nimes_et_variation import game_nime, game_variation
    from utils_main import input_name_user, choice_game_user, input_number_user
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
        run_horse()
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
