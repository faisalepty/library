import csv
import random
# from main.models import Book

with open('books_1.Best_Books_Ever.csv', 'r', newline='', encoding='utf-8') as file:

    data = csv.DictReader(file)
    i = 0
    for line in data:
        if i < 50:
            title = line['title']
            print(title)
            author = line['author']
            description = line['description']
            language = line['language']
            genres = f'{line["genres"].split(",")[2][2:-1]}, {line["genres"].split(",")[3][2:-1]}, {line["genres"].split(",")[4][2:-1]}, {line["genres"].split(",")[5][2:-1]}'
            edition = line['edition']
            pages = line['pages']
            publisher = line['publisher']
            publish_date = f'{line["publishDate"][0:2]}, {line["publishDate"][3:5]}, {line["publishDate"][6:8]}'
            if int(line["publishDate"][6:8]) > 24:
                publish_date = f'19{line["publishDate"][6:8]}-{line["publishDate"][0:2]}-{line["publishDate"][3:5]}'
            else:
                publish_date = f'20{line["publishDate"][6:8]}-{line["publishDate"][0:2]}-{line["publishDate"][3:5]}'
            img_url = line['coverImg']
            quantity = random.randint(1, 10)
            fee = random.randint(150, 300)
            print(f" 'title': {title}, \n 'author': {author}, \n 'description': {description}, \n 'language': {language}, \n  'category': {genres}, \n 'edition': {edition}, \n 'pages': {pages}, \n  'publisher': {publisher}, \n 'publish_date': {publish_date}, \n 'img_url': {img_url}, \n 'quantity'{quantity}, \n 'fee': {fee} \n \n")
            # Book.objects.create(title=title, author=author, description=description, language=language, category=genres, edition=edition, pages=pages, publisher=publisher, publish_date=publish_date, img_url=img_url, quantity=quantity, fee=fee)
            i = i + 1