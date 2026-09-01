# Texas Real Estate Market Analysis

An exploratory analysis of historical real estate market data from selected cities in Texas,
developed in **R** as part of my
[**professional Master's program in Data Science at ProfessionAI**](https://profession.ai/corsi/master-data-science).

🌐 [View the rendered HTML report](https://compostellaarianna.github.io/data-science-master-projects/texas-real-estate-analysis/)

*The rendered report includes a **Show All Code / Hide All Code** toggle for inspecting the underlying R code.*

## Overview

This project explores geographical, temporal, and seasonal patterns in the Texas
real estate market between **2010 and 2014**.

The analysis examines key market indicators including:

- sales
- sales volume
- median property prices
- active listings
- months of inventory

The project focuses on descriptive statistics, variability and distribution shape,
comparisons across cities and time periods, and graphical exploration of market trends.

## Analysis workflow

The project includes:

- data preparation and quality checks
- statistical classification of variables
- descriptive statistics and measures of variability
- skewness and kurtosis analysis
- categorical heterogeneity analysis
- grouped frequency distributions
- empirical probability calculations
- comparisons across cities, years, and months
- seasonal and historical trend analysis
- data visualization with `ggplot2`
- construction and interpretation of a derived **listing effectiveness** indicator
- follow-up analysis of market dynamics in Bryan–College Station

## Key findings

The analysis identifies substantial geographical, temporal, and seasonal differences
across the four Texas markets included in the dataset.

Sales generally increase through spring, reach their highest levels during late spring
and summer, and decline during autumn and winter. The later years of the dataset also
show stronger market activity and higher median property prices.

Among the quantitative variables, sales volume shows the greatest relative variability.

A derived **listing effectiveness** indicator highlights a particularly strong increase
for Bryan–College Station. Follow-up analysis suggests that this pattern is associated
with stronger sales activity together with a declining stock of active listings.

## Tools and skills

**R · R Markdown · dplyr · ggplot2 · moments · Descriptive Statistics ·
Data Quality Checks · Exploratory Data Analysis · Data Visualization ·
Statistical Interpretation**

## Files

- `texas_real_estate_analysis.Rmd` — reproducible R Markdown analysis
- `texas_real_estate_analysis.html` — rendered analytical report
- `realestate_texas.csv` — dataset used in the analysis

## Reproducing the analysis

Open `texas_real_estate_analysis.Rmd` in RStudio and knit the document to HTML.
The dataset should remain in the same directory as the `.Rmd` file.

Required R packages:

```r
install.packages(c("dplyr", "ggplot2", "moments"))
```

## Context

This project was developed as a hands-on exercise in descriptive statistics and exploratory data analysis.

The analysis is descriptive and is not intended to establish causal relationships.
