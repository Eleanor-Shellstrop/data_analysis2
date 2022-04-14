# About

This is a repo to apply machine learning tools of linear regression with multiple features to recent home sales. 

**Methods**

JavaScript was run in the console on the Zillow website to obtain data from house sales in Crestwood, KY in the last six months. The console log was copied and pasted into a CSV. 

Note that while I normally write a Python script for my web scrapers, Zillows website is dynamic and therefore data gathered in this way doesn't return anything of value. Since I was working with a small amount of data on a single page, JavaScript was quicker than creating a scraper with Selenium. 

Data was cleaned in the CSV file (`datasets/NewCrestwood.csv`) and through pandas in the `Crestwood.ipynb` file, which then created a new CSV with the cleaned data, `datasets/updated_crestwood.csv`. 

In `Cost Function.ipynb`, Scikit-Learn used the actual sales from the cleaned data CSV as a training set and a list of hypothetical homes from file `datasets/test_housing.csv` as a test set. Using linear regression with multiple features, the program found estimated prices for the test set, which were then stored in a new dataset, `datasets/estimated.csv`.

# Running the Program

## Requirements
This program runs on Jupyter Notebook and uses `pandas` and `Scikit-Learn` libraries. If you have Anaconda installed, you can run a notebook without any further downloads. [Learn more about Anaconda here.](https://docs.anaconda.com) 

If you do not have Anaconda and don't wish to download it, before opening the repo, run from your command line:

```
pip install pandas
pip install jupyter
pip install -U scikit-learn
```

## Instructions

1. Clone or download the repo, save to location of your choice.
2. Open command line and type `jupyter notebook`, or open from start menu.
3. In the notebook console, navigate to the location of the saved file in your computer.
4. Open the file `Cost Function.ipynb`.
5. Run all the cells.

Recommended for the first time running, go to `Kernel` tab and click `Restart & Run All`.

## Tableau

The data was plotted in Tableau for a visual comparison. [Click here to view.](https://public.tableau.com/app/profile/anne.ensign/viz/Housing_16443422067740/MLDashboard_1)