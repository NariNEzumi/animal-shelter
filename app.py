from flask import Flask, render_template

app = Flask(__name__)

# -----------------------------
# ЖИВОТНЫЕ (10 собак + 10 кошек)
# -----------------------------
animals_data = {

# ================= DOGS =================

1: {
    "name": "Пельмень",
    "type": "dog",
    "breed": "Хаски",
    "img": "https://images.dog.ceo/breeds/husky/n02110185_1469.jpg",
    "arrived": "2025-02-14",
    "desc": "Пельмень — энергичный и добрый пёс, который любит людей.",
    "story": "Пельмён был найден зимой у дороги. Он дрожал от холода и не отходил от людей, будто боялся снова остаться один. Сейчас он снова учится доверять человеку."
},

2: {
    "name": "Шарик",
    "type": "dog",
    "breed": "Бигль",
    "img": "https://images.dog.ceo/breeds/beagle/n02088364_11136.jpg",
    "arrived": "2025-09-03",
    "desc": "Шарик — добрый и любопытный пёс.",
    "story": "Шарик долго жил возле заброшенного дома и каждый день смотрел на дорогу, словно ждал кого-то, кто уже не вернётся."
},

3: {
    "name": "Котлета",
    "type": "dog",
    "breed": "Английский бульдог",
    "img": "https://images.dog.ceo/breeds/bulldog-english/jager-1.jpg",
    "arrived": "2026-01-22",
    "desc": "Спокойный и ласковый пёс.",
    "story": "Котлету оставили после переезда. Он долго сидел у двери квартиры, не понимая, почему его больше не зовут домой."
},

# ================= CATS =================

11: {
    "name": "Барсик-Босс",
    "type": "cat",
    "breed": "Британская короткошёрстная",
    "img": "https://cdn2.thecatapi.com/images/ozEvzdVM-.jpg",
    "arrived": "2025-03-10",
    "desc": "Спокойный и важный кот.",
    "story": "Барсик жил в подъезде офисного здания, где его подкармливали, но он всё равно ждал своего человека у двери."
},

12: {
    "name": "Мурзилка",
    "type": "cat",
    "breed": "Мейн-кун",
    "img": "https://cdn2.thecatapi.com/images/6kq.jpg",
    "arrived": "2025-06-18",
    "desc": "Большой и добрый кот.",
    "story": "Мурзилку нашли под дождём. Он прятался под машинами и боялся каждого громкого звука."
},

13: {
    "name": "Сырок",
    "type": "cat",
    "breed": "Сиамская",
    "img": "https://cdn2.thecatapi.com/images/ai6.jpg",
    "arrived": "2025-01-05",
    "desc": "Очень общительная кошка.",
    "story": "Сырок пришёл к магазину с травмированной лапкой и всё равно просил помощи у людей взглядом."
},

14: {
    "name": "Снежок Пушистик",
    "type": "cat",
    "breed": "Персидская",
    "img": "https://cdn2.thecatapi.com/images/3lo.jpg",
    "arrived": "2026-02-12",
    "desc": "Спокойный домашний кот.",
    "story": "Снежок жил один в подъезде зимой и выходил только ночью, когда становилось тихо."
},

15: {
    "name": "Тигрёнок",
    "type": "cat",
    "breed": "Бенгальская",
    "img": "https://cdn2.thecatapi.com/images/bpc.jpg",
    "arrived": "2025-08-09",
    "desc": "Игривый и активный кот.",
    "story": "Тигрёнка оставили на дачах после окончания сезона, и он долго ждал у ворот, что хозяева вернутся."
},

16: {
    "name": "Голый Вася",
    "type": "cat",
    "breed": "Сфинкс",
    "img": "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg",
    "arrived": "2026-03-01",
    "desc": "Очень ласковый и теплолюбивый кот.",
    "story": "Вася дрожал от холода на улице и сам подходил к людям, будто просил спасти его."
},

17: {
    "name": "Ушастик",
    "type": "cat",
    "breed": "Шотландская вислоухая",
    "img": "https://cdn2.thecatapi.com/images/ozEvzdVM-.jpg",
    "arrived": "2025-11-20",
    "desc": "Тихий и осторожный кот.",
    "story": "Ушастик долго не доверял людям, пока не понял, что его больше не обидят."
},

18: {
    "name": "Пушинка",
    "type": "cat",
    "breed": "Рэгдолл",
    "img": "https://cdn2.thecatapi.com/images/b1.jpg",
    "arrived": "2026-04-14",
    "desc": "Нежная и доверчивая кошка.",
    "story": "Пушинка сидела у магазина несколько дней, ожидая, что хозяин за ней вернётся."
},

19: {
    "name": "Мяу-Мия",
    "type": "cat",
    "breed": "Абиссинская",
    "img": "https://cdn2.thecatapi.com/images/ai5.jpg",
    "arrived": "2025-07-30",
    "desc": "Умная и активная кошка.",
    "story": "Мяу-Мия осталась одна после дачного сезона и начала искать еду среди мусора."
}

}

# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/animals")
def animals():
    return render_template("animals.html", animals=animals_data)


@app.route("/animals/dogs")
def dogs():
    dogs = {i: a for i, a in animals_data.items() if a["type"] == "dog"}
    return render_template("animals.html", animals=dogs)


@app.route("/animals/cats")
def cats():
    cats = {i: a for i, a in animals_data.items() if a["type"] == "cat"}
    return render_template("animals.html", animals=cats)


@app.route("/animal/<int:id>")
def animal(id):
    return render_template("animal.html", animal=animals_data[id])


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    print("Flask запущен")
    app.run(debug=True)
@app.route("/animal/<int:animal_id>")
def animal_page(animal_id):
    animal = animals_data.get(animal_id)
    return render_template("animal.html", animal=animal)
@app.route("/animal/<int:animal_id>")
def animal_page(animal_id):
    animal = animals_data.get(animal_id)
    return render_template("animal.html", animal=animal)
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
