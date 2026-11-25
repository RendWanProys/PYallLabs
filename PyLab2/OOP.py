import numpy as np


class Product:
    def __init__(self, price, quantity):
        self.price = float(price)
        self.quantity = int(quantity)

    def get_info(self):
        return f"Цена: {self.price}, Количество: {self.quantity}"

    def get_total_cost(self):
        return self.price * self.quantity


class Date:
    def __init__(self, day=1, month=1, year=2024):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def __del__(self):
        pass

    def is_same_day_month(self):
        return self.day == self.month

    def add_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1

    def get_info(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"


class ProductWithAge(Product):
    def __init__(self, price, quantity, year):
        super().__init__(price, quantity)
        self.year = int(year)

    def get_age(self, current_year=2024):
        return current_year - self.year

    def get_info(self):
        return f"{super().get_info()}, Год выпуска: {self.year}"


class Medicine(Date):
    def __init__(self, name, day, month, year, company):
        super().__init__(day, month, year)
        self.name = str(name)
        self.company = str(company)

    def __del__(self):
        pass

    def days_since_manufacture(self):
        m_date = np.datetime64(f"{self.year:04d}-{self.month:02d}-{self.day:02d}")
        today = np.datetime64("today")
        return int((today - m_date).astype(int))

    def get_info(self):
        return f"Лекарство: {self.name}, Фирма: {self.company}, Дата выпуска: {super().get_info()}"


class WarehouseProduct:
    def __init__(self, name, price, quantity):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)

    def quality(self):
        if self.quantity == 0:
            return 0.0
        return self.price / self.quantity

    def get_info(self):
        return f"Товар: {self.name}, Цена: {self.price}, Количество: {self.quantity}, Качество Q: {self.quality():.2f}"


class WarehouseProductWithYear(WarehouseProduct):
    def __init__(self, name, price, quantity, p):
        super().__init__(name, price, quantity)
        self.p = int(p)

    def quality(self, current_year=2024):
        if hasattr(current_year, "year"):
            current_year = current_year.year
        q = super().quality()
        return q + 0.5 * (int(current_year) - self.p)

    def get_info(self, current_year=2024):
        if hasattr(current_year, "year"):
            current_year = current_year.year
        return f"Товар: {self.name}, Цена: {self.price}, Количество: {self.quantity}, Год P: {self.p}, Качество Qp: {self.quality(current_year):.2f}"


def run_task1():
    print("--- Задание 1 ---")
    p1 = Product(150.5, 10)
    print(p1.get_info())
    print("Общая стоимость:", p1.get_total_cost())


def run_task2():
    print("\n--- Задание 2 ---")
    d_const = Date(12, 12, 2026)
    print("Константа:", d_const.get_info())
    print("Совпадают ли день и месяц:", d_const.is_same_day_month())
    d_const.add_month()
    print("После добавления месяца:", d_const.get_info())

    d_input = Date(5, 10, 2022)
    print("Объект 2:", d_input.get_info())
    print("Совпадают ли день и месяц:", d_input.is_same_day_month())


def run_task3():
    print("\n--- Задание 3 ---")
    parent_prod = Product(500, 4)
    child_prod = ProductWithAge(500, 4, 2020)
    print("Родитель:", parent_prod.get_info())
    print("Потомок:", child_prod.get_info())
    print("Возраст товара:", child_prod.get_age())


def run_task4():
    print("\n--- Задание 4 ---")
    d_base = Date(15, 3, 2026)
    med = Medicine("Аспирин", 15, 3, 2026, "Байер")
    print("Родитель (Дата):", d_base.get_info())
    print("Потомок (Лекарство):", med.get_info())
    print("Прошло дней:", med.days_since_manufacture())
    return d_base


def run_task5(date_obj=None):
    print("\n--- Задание 5 ---")
    t_year = date_obj.year if date_obj is not None else 2026
    wp1 = WarehouseProduct("Стол", 12000, 4)
    wp2 = WarehouseProductWithYear("Стол", 12000, 4, 2021)
    print("Уровень 1:", wp1.get_info())
    print("Уровень 2:", wp2.get_info(t_year))


def main():
    run_task1()
    run_task2()
    run_task3()
    d_base = run_task4()
    run_task5(d_base)


if __name__ == "__main__":
    main()