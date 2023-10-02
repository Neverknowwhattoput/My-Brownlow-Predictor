# My Brownlow Predictor
 A personal project to apply what I have learnt at university to a particular task of interest. 
 The project aims to predict the Brownlow Medallist for the AFL 2023 season.

## Installation
### Code
This project uses R to source AFL data using the Fryzigg package.

Python is used to source any remaining data and conduct cleaning, visualisation and machine learning.

### Packages
* **General Purpose:** os, tqdm, pyarrow
* **Data Manipulation:** pandas, numpy
* **Data Visualisation:** seaborn, matplotlib
* **Machine Learning:** statsmodels, scikit-learn

## Data
### Source Data
1. fitzRoy API: https://jimmyday12.github.io/fitzRoy/index.html
* AFL website: https://www.afl.com.au/
* footywire: https://www.footywire.com/
* afltables: https://afltables.com/afl/afl_index.html
2. Wikipedia: https://en.wikipedia.org/wiki/2012_AFL_season
3. Wheeloratings: https://www.wheeloratings.com/afl_brownlow.html

### Data Acquisition
The data sourced from wheeloratings is included in this repository as the download could not be automated

Data from Wikipedia is obtained within the notebooks using pandas as it is simply reading a table on the page

The remaining data is sourced via R, one can simply run the R file found in the folder named R

### Data Preprocessing
Data sourced using the fryzigg package was already fairly clean, just needed to drop columns that were irrelevant, many of which also contained N/A values.
There were many supercoach scores that were n/a, so they were sourced from footywire.

Some matches' data was not recorded properly so that was dropped. Where possible the AFL website was accessed and the data was changed manually.

Footytables was used to source brownlow votes for 2022 as they had not been added to the fryzigg source.

Where data was sourced from different websites, there was no common player_id and some names were represented differently, hence I had to get creative to be able to merge them properly. (e.g. Tom Stewart vs, Thomas Stewart)

I took the first letter of the first name paired with the second name, transformed the capitals to lowercase, and removed puncuation such as apostrophes. This paired with the player's team (since there were 2 Tom Lynch's for example) was a successful unique key for most players, and 1 or 2 were edited by hand (names like Ian Hill vs. Bobby Hill).

For the coaches votes names were represented as (name (team)) hence regex needed to be used to seperate the player name and team, then it could be merged with the main dataframe.

Similarly captains data sourced from wikipedia, regex needed to be used to extract players names, where some had reference attached to them (player[1])

Column names for data sourced from the AFL website were very messy so they all had to be renamed, the player statistics dataset did not include the team scores so that also needed to be sourced, cleaned and merged.

## Code Structure

All of the cleaning/preprocessing, model building and simulation is done within the notebooks found in the notebooks folder, seperated by function and numbered in the order they need to be run. Where a file begins with 1, this is past seasons data, and beginning with a 2 is current season (2023) data.

There is a single main.py script that runs all of the preprocessing and build model notebooks at once, so there is no need to open and close each file.

Once the script has been run, the simulation can be run, given how many simulations are to be run, I have included a progress bar from TQDM so that one can track it's progress.

The notebooks in the prediction folder can be run seperately to get the model's prediction for the 2023 season.

## Results and Evaluation

As can be seen below, when testing the model Clayton Oliver was the predicted winner, with the actual winner Patrick Cripps coming 5th (although just about equal 4th with Christian Petracca). 

Given the Monte Carlo Simulation method, it is expected that predicted votes will generally under estimate compared to the actual votes. Since players towards the bottom of the list that in reality will poll 0 votes, mind end up with 0.05 votes when averaged out. The sum of these votes decrease the total votes predicted at the top of the list.

Generally the model does a good job of assigning votes to players deserving of them, since it correctly predicts 8 of the actual top 10 players, albeit in the wrong order.

Most noteworthy for concern is how drastically the model underpredicts Cripps and Brayshaw while over predicting Laird and Walsh. I have listed reasons for why I think this might be in the future improvements section at the bottom.

### Model Testing Results for 2022

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>player</th>
      <th>player_team</th>
      <th>predicted_votes</th>
      <th>brownlow_votes</th>
      <th>error</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C. Oliver</td>
      <td>Melbourne</td>
      <td>28.0323</td>
      <td>25.0</td>
      <td>3.0323</td>
    </tr>
    <tr>
      <td>T. Miller</td>
      <td>Gold Coast</td>
      <td>25.9869</td>
      <td>27.0</td>
      <td>-1.0131</td>
    </tr>
    <tr>
      <td>L. Neale</td>
      <td>Brisbane Lions</td>
      <td>23.2338</td>
      <td>28.0</td>
      <td>-4.7662</td>
    </tr>
    <tr>
      <td>C. Petracca</td>
      <td>Melbourne</td>
      <td>21.7239</td>
      <td>24.0</td>
      <td>-2.2761</td>
    </tr>
    <tr>
      <td>P. Cripps</td>
      <td>Carlton</td>
      <td>21.5412</td>
      <td>29.0</td>
      <td>-7.4588</td>
    </tr>
    <tr>
      <td>S. Walsh</td>
      <td>Carlton</td>
      <td>19.2183</td>
      <td>14.0</td>
      <td>5.2183</td>
    </tr>
    <tr>
      <td>A. Brayshaw</td>
      <td>Fremantle</td>
      <td>19.1724</td>
      <td>25.0</td>
      <td>-5.8276</td>
    </tr>
    <tr>
      <td>C. Mills</td>
      <td>Sydney</td>
      <td>18.9243</td>
      <td>21.0</td>
      <td>-2.0757</td>
    </tr>
    <tr>
      <td>R. Laird</td>
      <td>Adelaide</td>
      <td>17.6607</td>
      <td>10.0</td>
      <td>7.6607</td>
    </tr>
    <tr>
      <td>J. Cameron</td>
      <td>Geelong</td>
      <td>15.8229</td>
      <td>19.0</td>
      <td>-3.1771</td>
    </tr>
  </tbody>
</table>

### Top 5 predictions for 2023

![Sample Image](https://github.com/Neverknowwhattoput/My-Brownlow-Predictor/blob/main/plots/top_5_predictions_2023.png?raw=true)


## Future Improvements

## References