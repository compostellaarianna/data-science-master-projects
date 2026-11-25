# Birth Weight Analysis: Statistical Inference and Regression in R

**An educational R-based analysis of 2,500 birth records from three hospitals.**

This project presents an end-to-end statistical workflow: exploratory analysis, data-quality assessment, hypothesis testing, multiple linear regression, model selection, diagnostics, sensitivity analyses and an example of individual birth-weight prediction.

🌐 [**View the rendered HTML report**](https://compostellaarianna.github.io/data-science-master-projects/birth-weight-statistical-analysis/)

*The HTML report includes a table of contents and expandable R code.*

> **Course project context:** The assignment specifically required starting with a full explanatory regression model and documenting a progressive reduction before producing a prediction for a defined case. This explains the report's iterative structure. The [assignment brief](docs/assignment.md) documents the requirements and explains the report’s structure.

## Research questions

- Do caesarean delivery rates differ across three hospitals?
- Do average birth weight and length differ from the assignment's reference values of 3,300 g and 50 cm?
- Are neonatal anthropometric measurements associated with sex?
- Which measured characteristics are associated with birth weight after adjustment for other predictors?
- How uncertain is an individual prediction for a female newborn delivered at 39 weeks in her mother's third pregnancy?

## Workflow

1. **Data quality:** check types, missingness, distributions and unusual combinations of measurements; replace two impossible maternal ages with missing values while retaining the other observations in those records.
2. **Descriptive statistics and exploration:** summarise quantitative/categorical variables and inspect associations using plots and correlations.
3. **Hypothesis testing:** conduct chi-square tests, one-sample t-tests and two-group Welch t-tests, with effect magnitudes and confidence intervals.
4. **Explanatory regression:** begin with all predictors, compare nested models and BIC values, and retain a parsimonious model. Assess residuals, multicollinearity, influential points, possible nonlinear terms and interactions.
5. **Prediction:** fit a separate model based only on characteristics supplied for the requested case, compare linear and quadratic gestational-age specifications, and report a point prediction with a 95% prediction interval.
6. **Sensitivity analyses:** assess whether suspicious or influential observations materially change coefficient estimates or the applied prediction.

## Selected findings

| Result | Finding |
|---|---|
| Sample size | 2,500 births (2,498 used in the full explanatory model because of two missing maternal-age values) |
| Explanatory reduced model | R² ≈ **0.727** with previous pregnancies, gestational age, newborn length, head circumference and sex |
| Applied prediction model | Quadratic gestational-age specification, R² ≈ **0.392** |
| Example prediction | **3,249 g** for a female newborn at 39 weeks, mother in her third pregnancy |
| 95% prediction interval | **2,445–4,053 g** |

These findings are **associations and in-sample model summaries**. The predictive model has **not been externally validated**, its residual diagnostics reveal some assumption violations, and its wide prediction interval limits individual-level precision. It must not be used for clinical decisions.

## Files

```text
03-birth-weight-statistical-analysis/
├── README.md                     # Project overview and selected findings
├── birth_weight_analysis.Rmd     # Reproducible English analysis and R code
├── birth_weight_analysis.html    # Rendered analytical report
├── neonati.csv                   # Original course dataset
├── docs/
│   ├── assignment.md             # Assignment brief (Markdown)
│   ├── assignment.html           # HTML version of the assignment brief
│   └── data_dictionary.md        # Variable definitions and caveats
└── .gitignore
```

The report is also published in the portfolio's GitHub Pages area at
[`docs/birth-weight-statistical-analysis/index.html`](../docs/birth-weight-statistical-analysis/index.html).
The site is served from the repository's **`main` branch, `/docs` folder**, as
for the Texas Real Estate project; no separate Pages configuration is needed.

## Reproduce the analysis

1. Clone or download this repository. The course dataset `neonati.csv` is already included alongside `birth_weight_analysis.Rmd`.
2. Install R, RStudio (optional), and the necessary packages:

   ```r
   install.packages(c("rmarkdown", "knitr", "dplyr", "ggplot2", "moments", "lmtest"))
   ```

3. Open `birth_weight_analysis.Rmd` and run **Knit to HTML**, or execute:

   ```r
   rmarkdown::render("birth_weight_analysis.Rmd", output_format = "html_document")
   ```

The script retains the dataset's original Italian column names so the existing R code and formula references remain compatible. All narrative explanations and output labels are presented in English.

## Methods and limitations

- **Explanatory vs predictive modelling:** The explanatory regression uses variables measured at or after birth, including neonatal length and head circumference; it should not be interpreted as an operational prenatal predictor. The separate prediction model uses only gestational age, number of previous pregnancies and sex, i.e., the variables supplied for the assignment's prediction case.
- **Data quality:** Suspicious combinations of measurements are retained rather than being automatically discarded, and sensitivity analyses assess their influence. Two impossible maternal-age values are set to `NA`.
- **Inference:** Model assumptions are not perfectly satisfied (notably residual heteroscedasticity in the explanatory model), and the data do not establish causal effects.
- **Generalisation:** There is no independent or external validation, so the reported in-sample fit should not be mistaken for out-of-sample performance.
- **Reference values:** The birth-weight and length benchmarks were supplied by the course brief and are *assignment reference values*, not independently sourced clinical norms.

## Tools

**R**, **R Markdown**, `dplyr`, `ggplot2`, `moments`, `lmtest`, `knitr`.

## Project attribution

Individual course project completed for an Inferential Statistics module in a Data Science master's programme. The original assignment was in Italian; this portfolio version is in English. The report preserves the analytical workflow and findings of the original submission.
