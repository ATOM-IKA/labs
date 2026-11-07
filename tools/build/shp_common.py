from common import build


def words(rows):
    return ("table", [3300, 6055], [["Слово или конструкция", "Что делает"]] + [list(r) for r in rows])


def qa(pairs):
    out = []
    for q, a in pairs:
        out.append(("p", "**" + q + "**"))
        out.append(("p", a))
    return out


def make(folder, number_title, topic, blocks):
    head = [("title", "Шпаргалка"), ("title", number_title), ("caption", topic)]
    build(head + blocks, f"/root/labs/labs/{folder}/shpargalka.docx", frame=False)
    print("ok", folder)
