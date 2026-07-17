def game_setup() -> None:
    """prépare les variables ainsi que les configurations si c'est pour jouer contre l'ordi ou pas"""
    from secrets import choice
    from jeux.horse import run_horse
    from jeux.le_compte_est_bon import game
    from jeux.bataille_navale import war_ship
    from jeux.nimes_et_variation import game_nime, game_variation
    from utils.utils_main import input_name_user, choice_game_user, input_number_user
    from asyncio import run
    from jeux.creation_gratteciel import bulding
    game_choice = choice_game_user()
    number_user = input_number_user(2, "Veuillez indiquer le nombre de joueurs (1 ou 2)\n" , False)
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
    elif game_choice == "le compte est bon":
        game()
    elif game_choice == "bataille navale":
        war_ship()
    elif game_choice == "gratteciel":
        run(bulding())
    print("Merci d'avoir joué")


def main() -> None:
    user = None
    while user is None:
        game_setup()
        user = input(
            "voulez vous recommencer à jouer? si oui tapez sur la touche entrée sinon tapez sur n'importe quel touche "
            "du clavier")
        if user == "":
            user = None
    print("à une prochaine fois ^^.")


if __name__ == '__main__':
    main()
