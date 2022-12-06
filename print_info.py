from matplotlib import pyplot as plt
import random
import pandas as pd

spotify = pd.read_csv("msd_cleaned.csv")

def to_print(song_title):
    row_index_temp = spotify[spotify["Title"] == song_title].index.values
    row_index = row_index_temp[0]
    
    
    
    title_str = "More About " + song_title
    

    return (title_str + ":\n\nThis song, by " + str(spotify.at[row_index, "ArtistName"])
            + ", was made in " + str(spotify.at[row_index, "Year"]) + " and came on the album " + str(spotify.at[row_index, "AlbumName"])  + ".\n"
            "For some quantatative info, the song has a tempo of " + str(spotify.at[row_index, "Tempo"]) + " bpm and a duration of " + str(spotify.at[row_index, "Duration"]) + " seconds.")