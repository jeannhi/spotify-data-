import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import csv

spotify = pd.read_csv("msd_cleaned.csv")

class Song: 
    def __init__(self, album_name, artist_name, duration, key_signature, tempo, time_signature, title, year, song_hotness): 
        self.album_name = album_name
        self.artist_name = artist_name
        self.duration = duration
        self.key_signature = key_signature
        self.tempo = tempo
        self.time_signature = time_signature
        self.title = title
        self.year = year
        self.song_hotness = song_hotness
        
    def __str__(self):
        title_str = f"More About \"{self.title.capitalize()}\""
        duration = float(self.duration)
        return (title_str + "\n" + 
               "This song, by " + self.artist_name + ", was made in " + self.year + " and came on the album " + self.album_name  + ".\n"
               "For some muscial information about it, the song has a tempo of " + self.tempo + " and a duration of {:.2f}.".format(duration))
    
    def to_list(self):
        return [self.album_name, self.artist_name, self.duration, self.key_signature, self.tempo, self.time_signature, self.title, self.year, self.song_hotness]
    
def read_song_data():
    song_objects = []
    
    try:
        with open("msd_cleaned.csv", "r") as f:
            next(f)
            for line in f.readlines():
                song_info = line.split(",")
                song_objects.append(Song(song_info[3], song_info[5], song_info[6], song_info[7], song_info[8], song_info[9], song_info[10], song_info[11], song_info[12]))                    
        return song_objects
    
    except: 
        print("File does not exist.")


def top_hundred_song():
    
    data = read_song_data()
    
    data.sort(key = lambda x: x.song_hotness, reverse = True)

    try:
        with open('spotifytophundred.csv', 'w') as file:
            top_hundred_data = csv.writer(file)
            for x in range(101):

                top_hundred_data.writerow(data[x].to_list())

        return top_hundred_data
                    
    except:
        print("Problem writing to the file")


 
