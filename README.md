# Project name: Spotify Data and Analysis

### Names: Jeannie Bui and Kyle Jurkowski

### Project Task

Our goal for this project is to showcase the Million Song Dataset by finding the top 100 songs of all time and creating some data visualizations based on the dataset. These classes help us to do so:

class Song: The class Song is the basis to reading in all of the information in the csv file. 

class data_visualizations: The class data_visualizations allows for different information about songs like duration, year, etc. to be pulled into an object, where we can call a function to create a graph to visually compare the correlation of things like "Year" and "Duration."


### List of Python packages

- numpy 1.21.5
- pandas 1.4.2
- matplotlib 3.5.1
- csv 5.0.1

### Demo file

The csv. file used was used from a previous class and had been pre-cleaned and a subset of 10,000 tracks from the original 1,000,000 track dataset.

### Data Visualization

The modules that needed to be imported to do this were: 
1) pandas: to be able to do data analysis manipulations and techniques on the the dataset
2) csv: to be able to write to and print out a new csv file

We imported from data_visualizations.py to get the compare_variables() function. This function takes a data_visualizations object and uses it to plot a scatter plot. To show that this funciton works as desired, we plotted the song hotness score vs the year, after dropping the songs with empty hotness scores or an unknown year.

Here's the visualization that was outputted:

<img width="1228" alt="SongHotness_vs_Year" src="https://user-images.githubusercontent.com/114253082/206884526-7e79db28-ccf9-4893-b93a-348dce9ad58a.png">

### Retreiving data of the top 100 songs in the data set

We imported from spotify.py to get the read_song_data() and top_hundred_song() functions. The read_song_data() function was to be able to read in all of the information provided by the Million Song Dataset csv. From there, we were finally able to manipulate the data to the desired way. 

We created the function top_hundred_song() which sorted the top songs by "SongHotness," with 1 being the highest and 0 being the lowest. The function writes into a new csv file called spotifytophundred.csv and prints out the top 100 songs by that measurement. Here are some screenshots to depict it:

To show that it was accurately printed in ascending order, here are the top ten songs in spotifytophundred.csv:

<img width="718" alt="image" src="https://user-images.githubusercontent.com/114253265/206319882-c7ccf59b-6ccd-48dc-bd4c-12820a408b49.png">

And here are the last ten songs:

<img width="717" alt="image" src="https://user-images.githubusercontent.com/114253265/206319981-02708660-2df4-45f5-9a25-f9742c848c62.png">

Thus, confirming that the top_hundred_song() function works as it should.

### Scope and limitations

1. In the dataset, there were a good amount of missing data. For example, there were a lot of 0's in "Year." In addition, there were a lot of blanks in "SongHotness" and 0.0's, unsure of whether the SongHotness score was an accurate 0.0 or was a mistake.
2. The function top_hundred_song() sorts the top 100 songs from the whole dataset by measuring "SongHotness," with 1 being the highest and 0 as the lowest. Because the "SongHotness" data column had a lot of blank spaces or 0.0's, this is a potential bias that skews the top one hundred songs, in that some of the songs with blank spaces could have been in the top one hundred, or the 0.0's could have potentially been a mistake and also a part of the top one hundred songs. 

### References and acknowledgement.
Data Visualization: https://github.com/lindseymardona/msd-exploration/blob/main/data_visuals_class.py \
Cleaned Data: https://github.com/lindseymardona/msd-exploration/blob/main/msd_cleaned.csv

### Background and source of the dataset

The original Million Song Dataset (MSD) is a set of 1,000,000 song tracks, characterized with musical features such as tempo, duration, key signature, time signature, and more. The dataset consists of songs mainly from 1922 to 2011. The current dataset used features 10,000 tracks from the Million Song Dataset and further cleaned so that the only existing columns are as follows: SongNumber,	SongID,	AlbumID,	AlbumName,	ArtistID,	ArtistName,	Duration,	KeySignature,	Tempo,	TimeSignature,	Title	Year,	SongHotness.

Link to the Cleaned Data: https://github.com/lindseymardona/msd-exploration/blob/main/msd_cleaned.csv

### Bugs and Troubleshooting

We need to create instantiations of the `data_visualizations` class before the following line in the Jupiter Notebook:
```
spotify = spotify[["AlbumName", "ArtistName", "Duration", "KeySignature", "Tempo", "TimeSignature", "Title", "Year", "SongHotness"]]
```
If we call the data_visualizations after this line, we run into an error because the above line transforms `spotify` from a **dataframe** to a **module**


In the function read_song_data(), we wrote the code 
```
"next(f)"
```
which essentially doesn't read the titles of each column in the csv so that our __str__ function would be able to run. As so, this messes up top_hundred_song() as it instead prints the first song into where the title is. Therefore, we add a row with the appropriate headers before the for loop in the code.

``` 
top_hundred_data.writerow(['AlbumName', 'ArtistName', 'Duration', 'KeySignature', 'Tempo', 'TimeSignature', 'Title', 'Year', 'SongHotness'])
```
By doing this however, the function is unique and can only be used both in this instance and dataset.
