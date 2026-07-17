def game() -> None:
    """cette fonction sert pour jouer au compte est bon."""
    from utils.utils_le_compte_est_bon import random_numbers, user_break, input_numbers, input_operator, arithmetic_operation
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