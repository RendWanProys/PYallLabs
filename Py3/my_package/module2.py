from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def task2():
    in_path = BASE_DIR / "text_input.txt"
    out_path = BASE_DIR / "text_output.txt"

    words = []
    with open(in_path, "r", encoding="utf-8") as Fin:
        for s in Fin:
            for ch in '.,!?:;"()[]-—«»1234567890':
                s = s.replace(ch, " ")
            for w in s.split():
                words.append(w.lower())

    if words:
        min_len = min(len(w) for w in words)
        count = 0
        min_words = []
        for w in words:
            if len(w) == min_len:
                count += 1
                if w not in min_words:
                    min_words.append(w)
    else:
        count = 0
        min_words = []

    print("Самые короткие слова:", ", ".join(min_words))
    print("Встречаются раз:", count)

    with open(out_path, "w", encoding="utf-8") as Fout:
        Fout.write(f"Слова: {', '.join(min_words)}\n")
        Fout.write(f"Количество: {count}\n")


if __name__ == "__main__":
    task2()
