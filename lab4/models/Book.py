class Book:
    @property
    def library(self) -> None:
        return self._library

    @property
    def publication_date(self) -> None:
        return self._publication_date

    @property
    def author_name(self) -> None:
        return self._author_name

    @property
    def author_surname(self) -> None:
        return self._author_surname

    @property
    def number_of_pages(self) -> None:
        return self._number_of_pages

    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Book is located in library: {self._library}. \
            Book information:\n- publication date: {self._publication_date}\n\
                - author name: {self._author_name}\n- author surname: \
                    {self._author_surname}\n- number of pages: \
                        {self._number_of_pages}"
