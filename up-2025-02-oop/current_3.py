books = [

    (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),

    (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни","O'Reily", 2002, 9.4),

    (3, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011, 135.9)

    ]
columns = ('identifier', 'title', 'subtitle', 'author', 'p_h', 'year', 'price')

def format_table(columns: tuple[str], data: list[tuple[str|int]]) -> str:
    all_data = [columns]
    all_data.extend(data)
    print(all_data)
    lengths = []
    for col in range(len(all_data[0])):
        maxlen = 0
        for row in range(len(all_data)):
            cell_data_len = len(str(all_data[row][col]))
            if cell_data_len > maxlen:
                maxlen = cell_data_len
        lengths.append(maxlen)
    print('Max lengths of columns:', lengths)

    result = '|'
    for col in range(len(columns)):
        result += f' {columns[col].center(lengths[col])} |'

    for row in range(len(data)):
        result += '\n|'
        for col in range(len(columns)):
            if type(data[row][col]) == str:
                result += f' {str(data[row][col]).ljust(lengths[col])} |'
            else:
                result += f' {str(data[row][col]).rjust(lengths[col])} |'

    result += '\n'
    return result

class Book:
    def __init__(self, identifier, title, subtitle, author, p_h, year, price):
        self.identifier = identifier
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.p_h = p_h
        self.year = year
        self.price = price
    def __str__(self):
        return f'Book(identifier: {self.identifier}, title:{self.title}, subtitle: {self.subtitle}, author: {self.author}, p_h: {self.p_h}, year: {self.year}, price: {self.price})'

def get_total_VAT(list_of_books):
    total_cost = 0
    for b in list_of_books:
        total_cost += b.price
    vat = total_cost * 20/100
    price_vat = total_cost + vat

    return total_cost,vat, price_vat


if __name__ == '__main__':
    print(books)
    print(format_table(columns, books))

    list_of_books = []

    for b in books:
        list_of_books.append(Book(b[0], b[1], b[2], b[3], b[4], b[5], b[6]))

    # for b in list_of_books:
    #     print(b)

    print(get_total_VAT(list_of_books))