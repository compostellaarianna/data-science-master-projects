# Data dictionary

The raw CSV uses the **original Italian column names**. These are intentionally preserved in the R code to ensure reproducibility.

| CSV column | English description | Unit / levels |
|---|---|---|
| `Anni.madre` | Maternal age | Years; two impossible entries (0 and 1) are treated as missing |
| `N.gravidanze` | Number of previous pregnancies | Count; a mother in her third pregnancy has `N.gravidanze = 2` |
| `Fumatrici` | Maternal smoking status | 0 = non-smoker; 1 = smoker |
| `Gestazione` | Gestational age | Completed weeks, as recorded |
| `Peso` | Birth weight | Grams |
| `Lunghezza` | Newborn length | Millimetres |
| `Cranio` | Neonatal head measurement | Millimetres |
| `Tipo.parto` | Delivery type | `Nat` (vaginal/natural), `Ces` (caesarean) |
| `Ospedale` | Hospital | `osp1`, `osp2`, `osp3` |
| `Sesso` | Newborn sex | `F` (female), `M` (male) |

**Measurement terminology caveat:** The original assignment describes `Cranio` as *cranial diameter*, while the submitted statistical report calls the measurement *head circumference*. The precise clinical definition should be confirmed against the dataset documentation; this English portfolio preserves the report's terminology without claiming independent verification of the measurement protocol.

**Timing caveat:** Newborn length and head measurements in this dataset are recorded at birth. These values should not be assumed to equal prenatal ultrasound estimates. The applied prediction model therefore does not rely on them.
