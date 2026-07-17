def run_horse() -> None:
    """fonction servant à faire la course avec les chevaux"""
    from utils.utils_horse import generate_run, input_type_run, input_user, print_results
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
    from pandas import DataFrame
    from secrets import SystemRandom
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
