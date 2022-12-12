##### Notes
#
### Initial Setup of Software, Outside of 1st Run
# 1. Required to produce save copy of existing live TCIS AMPL such that when tool is run, future extracts of live TCIS AMPL can be checked against the copy.
# 2. Have to do initial, manual scrub/analysis of lots of data. In other words, redo
#
### Contents of Live TCIS copy
# 1. Exact copy of what is in TCIS
# 2. Meta-data information
#  a) Key [Concatenation of specific columns]
#  b) Value [Concatenation of specific columns]
#  c) Date of last information refresh [Date the table was last checked against live TCIS]
#  d) Date of last change in TCIS live [Date of last variance between TCIS live and local table]
#  e) Miscellaneous notes [Free-form filled in by users]
### Contents of Modified TCIS copy
# 1. Duplicate of what is in TCIS, with manual modifications by local CE
# 2. Meta-data information
#  a) Key
#  a) Value
#  c) Date of last information refresh [Date the table was last checked against live TCIS copy]
#  d) Date of last change in modified TCIS [Date of last variance between live TCIS copy and local modified table]
#  e) Applied rule number for variance, if applicable otherwise "N/A" string
#  f) Type of variant rule (Unacceptable MFR, Component not FFF to other Sources,
#  g) Explanation of applied rule for variance [Non-free-form. Standardized text based on Rule number]
#  h) Variance Notes [Required if no Variance rule provided. Free-form filled by users]
#  i) LTB Date
#  j) Possible Alternates [Manufacturer P/Ns]
#  k) Possible Alternates, Manufacturers [One per Possible Alternate]
#  l) Alternate notes
#  m) Documentation/File Type
#  n) File name
#  o) Link to documentation
#  p) Documentation notes
### Modified TCIS which would be exported for Jabil
# 1. Duplicate of what is in TCIS, with manual modifications by local CE
# 2. Meta-data information
#  i) LTB Date
#  j) Possible Alternates [Manufacturer P/Ns]
#  k) Possible Alternates, Manufacturers [One per Possible Alternate]
#  l) Alternate notes

### FAQ May 3, 2020
#
# Q1) What if a 92xxxx number appears on a BOM?
# A1) Consider two options, either force Contract Manufacturers to use the single-source, or manually determine alternates
#     If forcing CM to use single-source, lots of noise will be raised.
#     If manual multi-source, large manual effort initially.. and may hide issue of 92xxxx numbers on BOM.
#     Case-by-Case fix for now
#
# Q2) What is the "Key" to keep track of a material from one file/time to another?
# A2) Part ID looks to be a unique identifier, but bugs/errors can exist in such a large data base.
#     Should combine - "Thales P/N on BOM", "Part ID",
#
##### Program Explanation
