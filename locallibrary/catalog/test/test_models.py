from catalog.models import Author, Book
from django.test import TestCase


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1/')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, "date of birth")

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create()

    """
    the fields are in Book models are: title(200), author, isbn(13)(h) -> ISBN , summary(1000)(h), genre(h), language 
    """

    def test_title_field_label(self):
        book = Book.objects.get(id=1)
        title = book._meta.get_field("title").verbose_name
        self.assertEqual(title, "title")

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)

    def test_author_field_label(self):
        book = Book.objects.get(id=1)
        author = book._meta.get_field("author").verbose_name
        self.assertEqual(author, "author")

    def test_isbn_field_label(self):
        book = Book.objects.get(id=1)
        isbn = book._meta.get_field("isbn").verbose_name
        self.assertEqual(isbn, "ISBN")

    def test_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("isbn").max_length
        self.assertEqual(max_length, 13)

    def test_isbn_help_text(self):
        book = Book.objects.get(id=1)
        help_text = book._meta.get_field("isbn").help_text
        self.assertEqual(help_text, '13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                    '">ISBN number</a>')

    def test_summary_field_label(self):
        book = Book.objects.get(id=1)
        summary = book._meta.get_field("summary").verbose_name
        self.assertEqual(summary, "summary")

    def test_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("summary").max_length
        self.assertEqual(max_length, 1000)

    def test_summary_help_text(self):
        book = Book.objects.get(id=1)
        help_text = book._meta.get_field("summary").help_text
        self.assertEqual(help_text, "Enter a brief description of the book")

    def test_genre_field_name(self):
        book = Book.objects.get(id=1)
        genre = book._meta.get_field("genre").verbose_name
        self.assertEqual(genre, "genre")

    def test_genre_help_text(self):
        book = Book.objects.get(id=1)
        help_text = book._meta.get_field("genre").help_text
        self.assertEqual(help_text, "Select a genre for this book")
