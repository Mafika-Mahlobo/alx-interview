#!/usr/bin/pytho3

"""
Prime Game implementation
"""


def isWinner(x, nums):

    """
    Returns name of player to most rounds of prime game (Ben or Maria)
    """

    if x <= 0 or not nums:
        return None

    # Precompute primes up to the maximum number in nums
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Calculate the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(primes[2:n + 1])
        # Maria wins if the number of primes is odd, otherwise Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
