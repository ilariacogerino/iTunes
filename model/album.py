from dataclasses import dataclass


@dataclass
class Album():
    AlbumId: int
    Title: str
    ArtistId: int
    Time: float

    def __hash__(self):
        return hash(self.AlbumId)

    def __eq__(self, other):
        return self.AlbumId == other.AlbumId