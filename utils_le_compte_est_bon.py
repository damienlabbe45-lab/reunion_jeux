def random_numbers() -> tuple[int, list[int]]:
    from secrets import SystemRandom
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