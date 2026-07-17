from asyncio import run
from asyncio import gather
from creation import generate_solution, combination, create_matrice, suppr_data, intialize
from game import game


async def main() -> None:
    number = intialize()
    matrice = generate_solution(await gather(create_matrice(number), combination(number)))
    matrice_game = suppr_data(matrice.copy(), number)
    game(matrice_game, matrice, number)
    print("Merci d'avoir jouer")


if __name__ == '__main__':
    run(main())
