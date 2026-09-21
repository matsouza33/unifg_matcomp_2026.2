from itertools import product


def alarme(a: int, b: int, c: int) -> int:
    return int((c and not b) or (a and b))


def main() -> None:
    print(f"{'A':<3}{'B':<3}{'C':<3}{'S':<3}")
    minitermos = []

    for a, b, c in product((0, 1), repeat=3):
        s = alarme(a, b, c)
        print(f"{a:<3}{b:<3}{c:<3}{s:<3}")
        if s == 1:
            indice = a * 4 + b * 2 + c
            minitermos.append((indice, a, b, c))

    print("\nMinitermos onde S = 1:")
    for indice, a, b, c in minitermos:
        print(f"m{indice} -> A={a} B={b} C={c}")

    print("\nS = C.B' + A.B")


if __name__ == "__main__":
    main()