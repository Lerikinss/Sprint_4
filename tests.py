from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод !!!!!!!!! get_books_rating - у нас нет такого метода, исправила на get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name', ['Что делать, если ваш кот хочет вас убить.', ''])
    def test_add_new_book_more_than_40_letters_and_blank_not_added(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self, collector):
        collector.add_new_book('Чижик')
        collector.add_new_book('Чижик')
        assert len(collector.get_books_genre()) == 1
        

    def test_set_book_genre_valid_book_and_genre_set(self, collector):
        collector.add_new_book('Таня Гроттер')
        collector.set_book_genre('Таня Гроттер', 'Фантастика')
        assert collector.get_book_genre('Таня Гроттер') == 'Фантастика'

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Роман')
        assert collector.get_book_genre('Война и мир') == ''

    def test_set_book_genre_book_not_in_collection_not_set(self, collector):
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert 'Гарри Поттер' not in collector.get_books_genre()

    def test_get_book_genre_valid_genre_set(self, collector):
        collector.add_new_book('Царевна лягушка')
        collector.set_book_genre('Царевна лягушка', 'Мультфильмы')
        assert collector.get_book_genre('Царевна лягушка') == 'Мультфильмы'

    def test_get_books_with_specific_genre_add_two_books(self, collector):
        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('50 оттенков серого')
        collector.set_book_genre('Преступление и наказание', 'Ужасы')
        collector.set_book_genre('50 оттенков серого', 'Комедии')
        assert collector.get_books_with_specific_genre('Комедии') == ['50 оттенков серого']

    def test_get_books_genre_blank_dic(self, collector):
        assert collector.get_books_genre() == {}

    def test_get_books_for_children_receive_books_in_age_rating(self, collector):
        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('50 оттенков серого')
        collector.set_book_genre('Преступление и наказание', 'Ужасы')
        collector.set_book_genre('50 оттенков серого', 'Комедии')
        assert collector.get_books_for_children() == ['50 оттенков серого']

    def test_add_book_in_favorites_added_to_list(self, collector):
        collector.add_new_book('Укрытие')
        collector.add_book_in_favorites('Укрытие')
        assert 'Укрытие' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_already_added_to_list(self, collector):
        collector.add_new_book('Укрытие')
        collector.add_book_in_favorites('Укрытие')
        collector.add_book_in_favorites('Укрытие')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_deleted(self, collector):
        collector.add_new_book('Сила киски')
        collector.add_book_in_favorites('Сила киски')
        collector.delete_book_from_favorites('Сила киски')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_added(self, collector):
        collector.add_new_book('Сила киски')
        collector.add_new_book('Сила собаки')
        collector.add_book_in_favorites('Сила киски')
        collector.add_book_in_favorites('Сила собаки')
        assert len(collector.get_list_of_favorites_books()) == 2