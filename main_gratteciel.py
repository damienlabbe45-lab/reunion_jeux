from asyncio import run
from asyncio import gather
from creation_gratteciel import generate_solution, combination, create_matrice, suppr_data, intialize
from game_gratteciel import game


async def bulding() -> None:
    number = intialize()
    matrice = generate_solution(await gather(create_matrice(number), combination(number)))
    matrice_game = suppr_data(matrice.copy(), number)
    game(matrice_game, matrice, number)
    print("Merci d'avoir jouer")
