from pandas import DataFrame


async def bulding() -> None:
    from asyncio import gather
    from jeux.game_gratteciel import game
    number = intialize()
    matrice = generate_solution(await gather(create_matrice(number), combination(number)))
    matrice_game = suppr_data(matrice.copy(), number)
    game(matrice_game, matrice, number)


def intialize2() -> int:
    from secrets import choice
    return choice(range(4,7))


def intialize() -> int:
    number = None
    while number is None:
        number = input("Entrez un nombre\n")
        if not (number == '4' or number == '5' or number == '6'
                or number == '7' or number == '8' or number == '9'
                or number == '10' or number == '3' or number == '2' 
                or number == '1' or number == '11'):
            number = None
            print("vous méritez un bon raise.")
        else:
            number = int(number)
    return number


def suppr_data(matrice: DataFrame, number: int) -> DataFrame:
    for j in range(len(matrice)):
        matrice[j] = [""] * number
    matrice = matrice.astype(object)
    return matrice


async def create_matrice(number: int) -> DataFrame:
    from numpy import eye
    from asyncio import to_thread
    return await to_thread(lambda: DataFrame(eye(number)))


async def combination(number: int) -> list[tuple[int, ...]]:
    from itertools import permutations
    from asyncio import to_thread
    return await to_thread(lambda: list(permutations(range(1, number + 1), number)))


def generate_solution(list_gather) -> DataFrame:
    # vrai type list_gather est list[DataFrame,list[tuple[int,...]]] mais mets qu'il y a trop de type
    from secrets import choice
    matrice: DataFrame = list_gather[0]
    combinations: list[tuple[int, ...]] = list_gather[1]
    for i in range(len(matrice)):
        choose = choice(combinations)
        matrice[i] = choose
        combinations = [t for t in combinations if all(a != b for a, b in zip(t, choose))]
    return matrice
