class Link:
    @property
    def id(self):
        return self._id

    @property
    def imdbId(self):
        return self._imdbId

    @property
    def tmdbId(self):
        return self._tmdbId

    def __init__(self, id: int, imdbId: float, tmdbId: float):
        self._id = id
        self._imdbId = imdbId
        self._tmdbId = tmdbId

    def __str__(self):
        return f'"id": {self._id},"title": "{self._imdbId}", \
            "genres": "{self._tmdbId}"'

    def __dict__(self):
        return {
            "id": self._id,
            "imdbId": self._imdbId,
            "tmdbId": self._tmdbId,
        }
