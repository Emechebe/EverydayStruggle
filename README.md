# EverydayStruggle

## A favorite show of mine is called EverydayStruggle, a show where current hip hop events are discussed. The show initially started with three hosts Nadeska, Joe and Dj Akademiks. Nadeska served as the moderator with Joe and Dj Akademiks as opinion commentators. Joe was the most controversial character of the show and in my opinion , his antics boosted the viewership of the show. However, Joe's tenure lasted from 2017-04-10 to 2017-12-20 as his contract was not renewed for the next season. Joe was replaced by another flamboyant character Dj Star and then later on by Wayno.

## Since I had the opinion that Joe was instrumental to the show's take off, I hypothesized that Joe leaving the show might hurt the ratings of the show. So I decided to test that hypothesis using the average monthly views as well as dislikes of the show with or without Joe.

## Getting and storing data in database
### Wrote a script to get the appropriate data of each episode from the Youtube channel of EverydayStruggle
### For ones with Joe the file is called EverydayStruggleWithJoe/Get_data_with_Joe.py
### For ones without Joe the file is called EverydayStruggleWithoutJoe/Get_data_without_Joe.py
### From a python terminal, run each script. Eg python Get_data_without_Joe.py. This script will connect to the Everyday Youtube channel and download some relevant information of episodes that include number of views as well as number of dislikes for each episodes. Data for Joe or without Joe are stored in a sqlite database

## Data Analysis
### The python notebook called DataAbalysis.ipynb contains code that connects to both databases (with or without Joe), integrated both data sets, resampled data to monthly frequency and calculated the mean of view and dislikes for each month. Then plotted this information. 

## Results
### Monthly views of show with or without Joe
![]("https://github.com/Emechebe/EverydayStruggle/blob/master/Views.png?raw=true")
### Monthly dislikes of show with or without Joe


# First I need to get the data of the all the shows from 2017-04 to 2017-12. I wrote a python script to 

# The youtube search api only returns a maximum of 50 results every request. So I decided to put this in a loop 
# using a start date and a last date. After the first iteration, the last date is updated for the next iteration. However, I
# didnt bother with the start date, so thats constant. However data is not duplicated since sqlite will not add data that is already
# in database..so it will always find the last date and start from there. 