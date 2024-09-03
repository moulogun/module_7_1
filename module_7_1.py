from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}.')

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        product_file = open(self.__file_name, 'r')
        product_list = str(product_file.read())
        product_file.close()
        return product_list

    def add(self, *products):
        file_check = open(self.__file_name, 'r')
        read_file = file_check.read()
        for product in products:
            if read_file.find(product.name) == -1:
                add_to_file = open(self.__file_name, 'a')
                add_to_file.write(product.name + ' ')
                add_to_file.write(str(product.weight) + ' ')
                add_to_file.write(product.category + '\n')
                add_to_file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')
        file_check.close()





s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

