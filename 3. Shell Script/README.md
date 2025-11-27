## Script Breakdown
```bash
#!/bin/bash

curl -sL "https://www.amfiindia.com/spages/NAVAll.txt"\
| awk -F ';' 'NF == 6 { print $4 "\t" $5 }' > "schema_nav.tsv"
```

### Components

`#!/bin/bash`
- Shebang line that specifies the script should be executed using the Bash shell

`curl -sL "https://www.amfiindia.com/spages/NAVAll.txt"`
- Downloads the NAV data file from AMFI India
- `-s`: Silent mode (no progress bar)
- `-L`: Follow redirects if any

`awk -F ';' 'NF == 6 { print $4 "\t" $5 }'`
- `-F ';'`: Sets the field separator to semicolon
- `NF == 6`: Filters only lines with exactly 6 fields
- `$4` and `$5`: Extracts the 4th and 5th fields (Scheme Name and Net Asset Value)
- `"\t"`: Separates output fields with a tab character

`> "schema_nav.tsv"`
- Redirects the output to a TSV (Tab-Separated Values) file

## Data Format

The source file has the following structure with 6 semicolon-separated fields:
```
Scheme Code;ISIN Div Payout/ ISIN Growth;ISIN Div Reinvestment;Scheme Name;Net Asset Value;Date
 
Open Ended Schemes(Debt Scheme - Banking and PSU Fund)
 
Aditya Birla Sun Life Mutual Fund
 
119551;INF209KA12Z1;INF209KA13Z9;Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - IDCW;110.2743;27-Nov-2025
119552;INF209K01YM2;-;Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - MONTHLY IDCW;118.0845;27-Nov-2025
119553;INF209K01YO8;-;Aditya Birla Sun Life Banking & PSU Debt Fund  - Direct - Quarterly IDCW;105.7815;27-Nov-2025
108272;INF209K01LX6;INF209KA11Z3;Aditya Birla Sun Life Banking & PSU Debt Fund  - REGULAR - IDCW;154.6852;27-Nov-2025
110282;INF209K01LU2;-;Aditya Birla Sun Life Banking & PSU Debt Fund  - REGULAR - MONTHLY IDCW;113.6669;27-Nov-2025
108274;INF209K01LN7;-;Aditya Birla Sun Life Banking & PSU Debt Fund  - REGULAR - Quarterly IDCW;103.5714;27-Nov-2025
110490;INF209K01LR8;-;Aditya Birla Sun Life Banking & PSU Debt Fund  - retail - monthly IDCW;114.253;27-Nov-2025
106157;INF209K01LS6;-;Aditya Birla Sun Life Banking & PSU Debt Fund  - retail - quarterly IDCW;104.7275;27-Nov-2025
108273;INF209K01LV0;-;Aditya Birla Sun Life Banking & PSU Debt Fund - Regular Plan-Growth;376.6026;27-Nov-2025
103176;INF209K01LT4;-;Aditya Birla Sun Life Banking & PSU Debt Fund - Retail Plan-Growth;565.3318;27-Nov-2025
119550;INF209K01YN0;-;Aditya Birla Sun Life Banking & PSU Debt Fund- Direct Plan-Growth;391.4095;27-Nov-2025
```

### Field Breakdown
- **Field 1**: Scheme Code
- **Field 2**: ISIN Div Payout/ISIN Growth
- **Field 3**: ISIN Div Reinvestment
- **Field 4**: Scheme Name (extracted)
- **Field 5**: Net Asset Value (extracted)
- **Field 6**: Date

The script extracts **Field 4 (Scheme Name)** and **Field 5 (Net Asset Value)** from lines with exactly 6 fields, filtering out header rows and category labels that don't match this format.

## Result
The script creates `schema_nav.tsv` containing two tab-separated columns:
1. Scheme Name
2. Net Asset Value

Example output:
```
Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - IDCW	110.2743
Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - MONTHLY IDCW	118.0845
```