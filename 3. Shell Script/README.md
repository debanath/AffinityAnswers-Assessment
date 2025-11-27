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
- `$4` and `$5`: Extracts the 4th and 5th fields
- `"\t"`: Separates output fields with a tab character

`> "schema_nav.tsv"`
- Redirects the output to a TSV (Tab-Separated Values) file

## Result
The script creates `schema_nav.tsv` containing only the 4th and 5th columns from lines that have exactly 6 semicolon-separated fields.