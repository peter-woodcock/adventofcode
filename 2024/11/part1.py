from itertools import chain

test_input = [125, 17]
puzzle_input = [3935565, 31753, 437818, 7697, 5, 38, 0, 123]

stones = puzzle_input
number_of_blinks = 25


def update_stone(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        first_half = int(str(stone)[:len(str(stone))//2])
        second_half = int(str(stone)[len(str(stone))//2:])
        return [first_half, second_half]
    else:
        return [stone * 2024]


for _ in range(number_of_blinks):
    stones = [update_stone(stone) for stone in stones]
    stones = list(chain.from_iterable(stones))


print(len(stones))
