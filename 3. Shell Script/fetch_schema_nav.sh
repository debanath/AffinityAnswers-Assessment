#!/bin/bash

curl -sL "https://www.amfiindia.com/spages/NAVAll.txt"\
| awk -F ';' 'NF == 6 { print $4 "\t" $5 }' > "schema_nav.tsv"