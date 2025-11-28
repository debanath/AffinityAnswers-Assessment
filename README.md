# Affinity Answers - Take-Home Assessment

This repository contains the solutions for the take-home assessment as part of the recruitment process for Affinity Answers.

## The Challenge

The assessment consists of three questions designed to test skills in web scraping, database interaction (SQL), and shell scripting.

---

### Question 1: OLX Web Scraper

> I am searching for a “Car Cover” on OLX - using this URL https://www.olx.in/items/q-car-cover?isSearchCall=true; I need a python program that gives me the search results parameters - like title of the ad, description and price. Print the results in table format. Don’t bother about the image. Place the code in Github and share the link.

**Solution:**
The Python script for this task can be found in the `1. OLX Scraper/` directory.

---

### Question 2: SQL Database Queries

> The following questions test your aptitude for interacting with databases. The questions are based off the following public SQL DB: https://docs.rfam.org/en/latest/database.html
>
> a) How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)
> b) Find all the columns that can be used to connect the tables in the given database.
> c) Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)
> d) We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)

**Solution:**
The SQL queries and detailed explanations for each question are located in the `2. SQL Queries/explanation.md` file.

---

### Question 3: Shell Script for Data Extraction

> This question is to test your aptitude for writing small shell scripts on Unix. You are given this URL https://www.amfiindia.com/spages/NAVAll.txt. Write a shell script that extracts the Scheme Name and Asset Value fields only and saves them in a tsv file. And ever wondered if this data should not be stored in JSON?

**Solution:**
The shell script (`fetch_schema_nav.sh`) and the resulting `schema_nav.tsv` file are in the `3. Shell Script/` directory. A `README.md` inside this directory provides more details on the script and the question about JSON.

---
