from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def task1(tovar=None):
    in_path = BASE_DIR / "tovar_input.txt"
    out_path = BASE_DIR / "tovar_output.txt"

    if tovar is None:
        tovar = input("Введите товар: ")

    total_sum = 0
    country = []

    with open(in_path, "r", encoding="utf-8") as Fin:
        for s in Fin:
            p = s.split()
            if len(p) >= 3 and p[0] == tovar:
                total_sum += int(p[2])
                if p[1] not in country:
                    country.append(p[1])

    print(total_sum)
    print(country)

    with open(out_path, "w", encoding="utf-8") as Fout:
        Fout.write(str(total_sum) + "\n")
        Fout.write(" ".join(country))


if __name__ == "__main__":
    task1()
