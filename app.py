from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'tamga-demo-secret'

TELEGRAM_LINK = 'https://t.me/'  # TODO: replace with your bot link

YURTS = [
    {
        'type': 'Бюджет',
        'tag': 'ЮРТА · БЮДЖЕТ',
        'title': 'Юрта для спокойного отдыха',
        'subtitle': 'Тёплая атмосфера и базовый комфорт',
        'description': 'Уютная юрта для спокойного отдыха вдвоём.',
        'guests': '2 гостя',
        'price': 'от 6200 ₽ / ночь',
        'feature': 'уютный интерьер',
        'image': 'images/yurt-budget.png',
    },
    {
        'type': 'Стандарт',
        'tag': 'ЮРТА · СТАНДАРТ',
        'title': 'Юрты в едином стиле',
        'subtitle': 'Простор и ощущение тишины',
        'description': 'Просторная юрта с тёплым интерьером.',
        'guests': '2–3 гостя',
        'price': 'от 9200 ₽ / ночь',
        'feature': 'отдельная терраса',
        'image': 'images/yurt-standard.png',
    },
    {
        'type': 'Люкс',
        'tag': 'ЮРТА · ЛЮКС',
        'title': 'Максимум комфорта в традиционном формате',
        'subtitle': 'Больше пространства и деталей',
        'description': 'Комфортная юрта повышенного уровня.',
        'guests': '3–4 гостя',
        'price': 'от 12500 ₽ / ночь',
        'feature': 'улучшенная зона отдыха',
        'image': 'images/yurt-lux.png',
    },
]

ACTIVITIES = [
    ('1. Конные прогулки', 'Прогулки верхом по природным маршрутам с инструкторами.'),
    ('Стрельба из лука', 'Знакомство с традиционным оружием и обучение основам.'),
    ('Вечера у костра', 'Живая атмосфера, огонь и спокойный отдых на природе.'),
    ('Проживание в юртах', 'Комфортный отдых в аутентичных юртах с современными удобствами.'),
    ('Чайные традиции', 'Травяные сборы, кумыс и традиционные напитки.'),
    ('Мастер-классы', 'Гончарное дело, ремесла и создание сувениров.'),
]

MENU_ITEMS = [
    {
        'name': 'Бешбармак с кониной',
        'price': '690 ₽',
        'weight': '350 г',
        'description': 'Классическое блюдо башкирской кухни: домашняя лапша, мясо и насыщенный бульон.',
        'image': 'dish-1.png.png',
    },
    {
        'name': 'Кыстыбый с картофелем',
        'price': '320 ₽',
        'weight': '220 г',
        'description': 'Тёплая лепёшка с нежной начинкой, которую подают как сытную закуску.',
        'image': 'dish-2.png',
    },
    {
        'name': 'Домашняя колбаса',
        'price': '540 ₽',
        'weight': '240 г',
        'description': 'Плотная мясная закуска по традиционному рецепту с пряным ароматом.',
        'image': 'dish-3.png',
    },
    {
        'name': 'Баурсак и чайный сет',
        'price': '390 ₽',
        'weight': '280 г',
        'description': 'Воздушные баурсаки, башкирский чай и домашние сладости для неспешного чаепития.',
        'image': 'dish-4.png',
    },
    {
        'name': 'Шурпа на открытом огне',
        'price': '480 ₽',
        'weight': '320 г',
        'description': 'Сытный суп с мясом и овощами, приготовленный в живом огне.',
        'image': 'dish-5.png',
    },
    {
        'name': 'Чак-чак с мёдом',
        'price': '280 ₽',
        'weight': '180 г',
        'description': 'Традиционный десерт башкирской кухни с мягкой сладостью и медовым ароматом.',
        'image': 'dish-6.png',
    },
]

REVIEWS = [
    {
        'name': 'Зайнуллин Данил',
        'text': 'Очень атмосферное место. Юрты уютные, внутри тепло и комфортно, а вокруг — тишина и природа. Отдых получился действительно особенным.',
        'image': 'images/review-1.png',
    },
    {
        'name': 'Абдулаева Ясмина',
        'text': 'Больше всего запомнился ресторан и вечера у огня. Всё сделано с уважением к традициям, но при этом отдыхать очень удобно.',
        'image': 'images/review-2.png',
    },
    {
        'name': 'Юлия Санина',
        'text': 'Понравилось, что здесь можно по-настоящему отключиться от городской суеты. Конные прогулки, спокойствие и красивая территория — хочется вернуться снова.',
        'image': 'images/review-3.png',
    },
    {
        'name': 'Назарова Полина',
        'text': 'Очень тёплое и продуманное место. Видно, что в проект вложена идея: не просто проживание, а целая атмосфера отдыха и культуры.',
        'image': 'images/review-4.png',
    },
]

@app.context_processor
def inject_globals():
    return {'telegram_link': TELEGRAM_LINK}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', activities=ACTIVITIES)

@app.route('/yurts')
def yurts():
    return render_template('yurts.html', yurts=YURTS)

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html', menu_items=MENU_ITEMS)

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        flash('Форма временно работает в демо-режиме. Позже сюда можно подключить отправку на почту.', 'info')
    return render_template('contacts.html', reviews=REVIEWS)

if __name__ == '__main__':
    app.run(debug=True)
