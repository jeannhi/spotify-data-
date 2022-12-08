# Project name: Spotify Data and Analysis

### Names: Jeannie Bui and Kyle Jurkowski

### Project Task

Our goal for this project is to showcase the Million Song Dataset by finding the top 100 songs of all time and creating data visualizations for it. These classes help us to do so:

class Song: The class Song is the basis to reading in all of the information in the csv file. This then allows us to sort all of the songs by "SongHotness" with 1 being the highest and 0 being the lowest, printing the top 100 songs out in a csv file.


### List of Python packages

- numpy 1.21.5
- pandas 1.4.2
- matplotlib 3.5.1
- csv 

### Detailed description of the demo file
##### This includes detailed instructions on how to run it, what output one should expect to see, and any explanations or interpretations of the result. There should be at least 2 figures embedded in this section. It can be screenshots of your game, or plots generated by your data visualization code. Make sure these figures have appropriate titles and captions, and are sufficiently explained in your text.

The csv. file used was used from a previous class and had been pre-cleaned and a subset of 10,000 tracks from the original 1,000,000 track dataset.

### Retreiving data of the top 100 songs in the data set

The modules that needed to be imported to do this were: 
1) pandas: to be able to do data analysis manipulations and techniques on the the dataset
2) csv: to be able to write to and print out a new csv file

We imported from spotify.py to get the read_song_data() and top_hundred_song() functions. The read_song_data() function was to be able to read in all of the information provided by the Million Song Dataset csv. From there, we were finally able to manipulate the data to the desired way. 

We created the function top_hundred_song() which sorted the top songs by "SongHotness," with 1 being the highest and 0 being the lowest. The function writes into a new csv file called spotifytophundred.csv and prints out the top 100 songs by that measurement. Here are some screenshots to depict it:

To show that it was accurately printed in ascending order, here are the top ten songs in spotifytophundred.csv:

<img width="718" alt="image" src="https://user-images.githubusercontent.com/114253265/206319882-c7ccf59b-6ccd-48dc-bd4c-12820a408b49.png">

And here are the last ten songs:

<img width="717" alt="image" src="https://user-images.githubusercontent.com/114253265/206319981-02708660-2df4-45f5-9a25-f9742c848c62.png">

Thus, confirming that the top_hundred_song() function works as it should.

### Scope and limitations
##### Including ethical implications, accessibility concerns, and ideas for potential extensions.

1. In the dataset, there were a good amount of missing data. For example, there were a lot of 0's in "Year." In addition, there were a lot of blanks in "SongHotness" and 0.0's, unsure of whether the SongHotness score was an accurate 0.0 or was a mistake.
2. The function top_hundred_song() sorts the top 100 songs from the whole dataset by measuring "SongHotness," with 1 being the highest and 0 as the lowest. Because the "SongHotness" data column had a lot of blank spaces or 0.0's, this is a potential bias that skews the top one hundred songs, in that some of the songs with blank spaces could have been in the top one hundred, or the 0.0's could have potentially been a mistake and also a part of the top one hundred songs. 

### References and acknowledgement.
Data Visualization: https://github.com/lindseymardona/msd-exploration/blob/main/data_visuals_class.py \
Cleaned Data: https://github.com/lindseymardona/msd-exploration/blob/main/msd_cleaned.csv

### Background and source of the dataset
##### (If appropriate)
The original Million Song Dataset (MSD) is a set of 1,000,000 song tracks, characterized with musical features such as tempo, duration, key signature, time signature, and more. The dataset consists of songs mainly from 1922 to 2011. The current dataset used features 10,000 tracks from the Million Song Dataset and further cleaned so that the only existing columns are as follows: SongNumber,	SongID,	AlbumID,	AlbumName,	ArtistID,	ArtistName,	Duration,	KeySignature,	Tempo,	TimeSignature,	Title	Year,	SongHotness.

Link to the Cleaned Data: https://github.com/lindseymardona/msd-exploration/blob/main/msd_cleaned.csv

### Links to any tutorials you used
##### (If appropriate) At least 3 specific things you implemented that differentiates your project from what’s already in the tutorial.

### IMPORTANT NOTE
##### Your demo has to be completely reproducible by people outside of your team. If I follow your code and instructions but can’t reproduce your results, there may be a penalty.
We might need to address or clarify something about a bug I found in the code:\
When creating an instantiation of the `data_visualizations` class, we need to have this before the following line in the Jupiter Notebook:
```
spotify = spotify[["AlbumName", "ArtistName", "Duration", "KeySignature", "Tempo", "TimeSignature", "Title", "Year", "SongHotness"]]
```
If we call the data_visualizations after this line, we run into an error because the above line transforms `spotify` from a **dataframe** to a **module** (not sure what a module is exactly)


In the function read_song_data(), we did "next(f)" which essentially doesn't read the titles of each column in the csv so that our __str__ function would be able to run. As so, this messes up top_hundred_song() as it instead prints the first song into where the title is. Therefore, we add a row with the appropriate headers before the for loop in the code.

``` 
top_hundred_data.writerow(['AlbumName', 'ArtistName', 'Duration', 'KeySignature', 'Tempo', 'TimeSignature', 'Title', 'Year', 'SongHotness'])
```
By doing this however, the function is unique and can only be used both in this instance and dataset.
