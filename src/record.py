from song import *

class Record:
    
    all=[]

    def __init__(self,title,artist,year):
        self.title=title
        self.artist=artist
        self.year=year
        self.songs=[]
        Record.all.append(self)

    def get_title(self):
        return self.title.title()
    
    def get_year(self):
        return self.year
    
    def get_artist(self):
        return self.artist
    
    @classmethod
    def get_all(cls):
        return cls.all
    
    def get_songs(self):
        return self.songs
    
    def total_runtime(self):
        return sum([song.runtime for song in self.get_songs()])
                   
    def has_song(self,song):
        return song in self.get_songs()

    def get_longest_song(self):
        songs=self.get_songs()
        longest_song=songs[0]
        
        for i in range(1,len(songs)):
            if(songs[i].get_runtime()>longest_song.get_runtime()):
                longest_song=songs[i]
        
        return longest_song