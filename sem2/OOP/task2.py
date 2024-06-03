class Song:

    def __init__(self, title, artist, release_year) -> None:
        self.title = title
        self.artist = artist
        self.release_year = release_year

    def get_into(self):
        info = {"title":self.title,
                "artist":self.artist,
                "release_year":self.release_year}
        return info
        

some_song= Song('Some song', 'Somebody', 2024)
print(some_song.get_info())