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
![](https://github.com/Emechebe/EverydayStruggle/blob/master/Views.png?raw=true)

### Monthly dislikes of show with or without Joe
![](https://github.com/Emechebe/EverydayStruggle/blob/master/Dislikes.png?raw=true)

## Conclusions : Seemed like my intution was somewhat correct. With Joe, the show grossed a monthly viewership of 425,000 while without Joe it grossed 225,000. So the difference is about 200,000. Thats a pretty big difference. In terms of the number of dislikes, with Joe the number of dislikes were about 1,000 while without Joe the numbers rose up to 2,500 dislikes per month. 

## Caveats : There is an argument to be made that I am not comparing the same distribution. The Joes episode have been out longer than episodes without Joe and so just because of that ,Joe's episodes would have garnered more views. Thats fair ; however, the number of dislikes argues against that. Although Joe's episodes have been out longer, episodes without Joe have managed to garner more dislikes. I only plotted the raw number of dislikes. There might be a better way of doing this eg normalizing the number of dislikes to the total number of views. I think this would even lead to a greater difference since the number of views were more for Joe. Finally, there is no statistical test. But all in all, there is pretty strong preliminary evidence to suggest that Joe leaving did hurt the show at least in terms of number of views and number of dislikes. 