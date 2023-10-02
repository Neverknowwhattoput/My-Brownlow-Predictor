# My Brownlow Predictor
 A personal project to apply what I have learnt at university to a particular task of interest. 
 The project aims to predict the Brownlow Medallist for the AFL 2023 season.

## Installation
### Code
This project uses R to source AFL data using the Fryzigg package.

Python is used to source any remaining data and conduct cleaning, visualisation and machine learning.

### Packages
* **General Purpose:** os, tqdm
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

## Table of Predictions when testing the model on the 2022 season

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

## Top 5 predictions for 2023

![Sample Image](https://github.com/Neverknowwhattoput/My-Brownlow-Predictor/blob/main/plots/top_5_predictions_2023.png?raw=true)