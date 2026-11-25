# Course assignment: Birth Weight Analysis Across 2,500 Records from Three Hospitals

> **Source.** English adaptation of the original Italian course assignment. The analytical requirements are preserved. Population reference values are taken from the assignment and are not independently sourced clinical norms.

## Background

Birth weight is an informative indicator of neonatal health. Estimating it before delivery using information available during pregnancy may be relevant for anticipating neonatal care needs. The statistical analysis also aims to identify factors associated with birth weight and assess whether observations from the three hospitals are comparable.

## Data

A dataset of **2,500 birth records** from three hospitals is provided. Each record includes:

- Maternal age
- Number of previous pregnancies
- Maternal smoking status (0 = non-smoker; 1 = smoker)
- Gestational age in weeks
- Birth weight in grams
- Newborn length and head measurement
- Delivery type (vaginal/natural or caesarean)
- Hospital of birth (three hospitals)
- Newborn sex

The original brief notes that length and cranial measurements can also be assessed during pregnancy through ultrasound and may therefore potentially be available before delivery. **For this particular dataset, birth measurements and prenatal estimates must not be assumed to be identical.**

## Required work

### 1. Data exploration and quality assessment

Conduct descriptive exploration of all variables, including distributions, anomalous or clinically implausible values, and missing data. Assess which columns can be trusted and explain any data-cleaning decisions.

### 2. Three hypothesis-testing questions

Investigate:

- Whether the frequency of caesarean deliveries differs among the three hospitals.
- Whether the sample mean birth weight and mean length are compatible with the Italian-population reference values specified in the assignment (**3,300 g** and **50 cm**).
- Whether anthropometric measurements differ between male and female newborns.

For each question, state the null and alternative hypotheses, identify the test used and explain the rationale for choosing it.

### 3. Multiple linear regression

Develop a multiple linear regression model for birth weight, **starting with the complete set of predictors** and obtaining a simpler specification containing the most relevant variables. If appropriate, investigate interaction terms and nonlinear relationships, explaining the decisions.

### 4. Diagnostics of the final model

Assess model fit, residuals and observations with disproportionate influence on coefficient estimates. Report whether and how these observations alter the conclusions.

### 5. Applied prediction

Estimate birth weight for **a female newborn whose mother is in her third pregnancy and who is delivered at 39 weeks of gestation**. Explain how the prediction should be interpreted.

### 6. Clinically readable figures

Create figures communicating the main relationships to a medical audience; for example, the relationship of predicted birth weight with gestational age and maternal smoking.

## Communication expectations

The intended readers are midwives and neonatologists rather than statisticians. Accompany coefficients and p-values with an accessible interpretation of what they mean. Report uncertainty and model limitations rather than presenting unwarrantedly reassuring conclusions.

## Detailed methodological guidance from the brief

### Examine the data before modelling

Create histograms and boxplots of continuous variables and frequency tables for categorical variables. A birth weight of **200 g** or a gestation of **60 weeks**, for example, should be treated as an apparent data-entry error rather than an ordinary clinical observation. Decide how to handle such values and document the decision in the report.

### Formulate hypotheses before running each test

For each of the three clinical questions, state the null and alternative hypotheses before choosing the statistical tool. Distinguish between a one-sample comparison with a specified population value, a comparison of two group means, and a test of independence in a frequency table. Test selection depends on the quantity and groups being compared.

### A p-value is not an effect size

With 2,500 observations, even small differences may be statistically significant. Report the difference between means or a confidence interval alongside the p-value, and discuss whether the effect may be clinically meaningful.

### Explore pairwise relationships

Before regression, draw scatterplots of birth weight against continuous predictors and compute correlations. Inspect both relationships with birth weight and correlations between predictors, for instance between length and head measurements, which may carry overlapping information.

### Check for nonlinear patterns

A low correlation does not imply that two variables are unrelated: a curved relationship may not be captured by Pearson's linear correlation. Inspect the figure rather than relying only on the coefficient.

### Progress from the full model to a parsimonious model

Begin with every predictor and progressively remove nonsignificant variables, comparing successive models. **Document each step:** which predictor was removed, by what criterion and how model fit changed. A model with fewer, interpretable predictors can be more useful than one with many terms.

### Handle categorical predictors correctly

Include sex, delivery type and hospital as factors in R. Interpret coefficients as differences relative to the reference category and explain the chosen reference categories in the report.

### Treat diagnostics as substantive evidence

Inspect residuals against fitted values to evaluate whether residual variation is approximately constant and assess their distribution. Report unexpected patterns and discuss possible reasons; do not present the model as perfect.

### Show prediction uncertainty

Report a suitable interval as well as the point prediction for the requested case. An individual clinical prediction without uncertainty can be misleading.

### Design figures for their readers

Use meaningful axis labels, measurement units and informative titles instead of raw variable names. A figure showing predicted weight by gestational week, distinguishing smokers and non-smokers, may communicate more than a large table.


---

*Educational assignment; not an operational clinical protocol.*
