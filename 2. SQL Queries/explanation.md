# Task 2: Rfam Database SQL Queries - Answers

## Database Connection Information
```bash
# Connect using:
mysql --user rfamro --host mysql-rfam-public.ebi.ac.uk --port 4497 --database Rfam
```

---

## Question 2a: Tigers in Taxonomy Table

### Question:
How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger?

### SQL Query:
```sql
SELECT ncbi_id, species 
FROM taxonomy 
WHERE species LIKE '%panthera tigris%';
```

### Results:
```
+---------+----------------------------------------------+
| ncbi_id | species                                      |
+---------+----------------------------------------------+
|    9694 | Panthera tigris (tiger)                      |
|   74533 | Panthera tigris altaica (Amur tiger)         |
|  253258 | Panthera tigris amoyensis (Amoy tiger)       |
|   74534 | Panthera tigris corbetti (Indochinese tiger) |
|  419130 | Panthera tigris jacksoni (Malayan tiger)     |
|  644771 | Panthera tigris sondaica (Javan tiger)       |
|    9695 | Panthera tigris sumatrae (Sumatran tiger)    |
|   74535 | Panthera tigris tigris (Bengal tiger)        |
+---------+----------------------------------------------+
8 rows in set (2.953 sec)
```

### Answer:
Number of tiger types: 8

Sumatran Tiger (Panthera tigris sumatrae) ncbi_id: 9695

---

## Question 2b: Columns Used to Connect Tables

### Question:
Find all the columns that can be used to connect the tables in the given database.

### Approach:
To comprehensively answer this question, I queried the database schema using two methods:
1. **Foreign Key Relationships** - Shows the explicitly defined table relationships in the database
2. **Common Column Names** - Identifies columns that appear across multiple tables and could potentially be used for joins


### SQL Query 1 - Foreign Key Relationships (Primary Answer):
```sql
SELECT 
  TABLE_NAME,
  COLUMN_NAME,
  CONSTRAINT_NAME,
  REFERENCED_TABLE_NAME,
  REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE 
  REFERENCED_TABLE_SCHEMA = 'Rfam' 
  AND REFERENCED_TABLE_NAME IS NOT NULL
ORDER BY TABLE_NAME, COLUMN_NAME;
```

**Results:**
```
+-----------------------------+--------------+------------------------------------------------------+-----------------------+------------------------+
| TABLE_NAME                  | COLUMN_NAME  | CONSTRAINT_NAME                                      | REFERENCED_TABLE_NAME | REFERENCED_COLUMN_NAME |
+-----------------------------+--------------+------------------------------------------------------+-----------------------+------------------------+
| _family_file                | rfam_acc     | fk_table1_family1                                    | family                | rfam_acc               |
| _overlap_membership         | auto_overlap | fk_overlap_membership_overlap1                       | _overlap              | auto_overlap           |
| _overlap_membership         | rfam_acc     | fk_overlap_membership_family1                        | family                | rfam_acc               |
| _post_process               | rfam_acc     | fk_table1_family2                                    | family                | rfam_acc               |
| alignment_and_tree          | rfam_acc     | fk_alignments_and_trees_family1                      | family                | rfam_acc               |
| clan_database_link          | clan_acc     | fk_clan_database_links_clan1                         | clan                  | clan_acc               |
| clan_literature_reference   | clan_acc     | fk_clan_literature_references_clan1                  | clan                  | clan_acc               |
| clan_literature_reference   | pmid         | fk_clan_literature_references_literature_reference1  | literature_reference  | pmid                   |
| clan_membership             | clan_acc     | fk_clan_membership_clan1                             | clan                  | clan_acc               |
| clan_membership             | rfam_acc     | fk_clan_membership_family1                           | family                | rfam_acc               |
| database_link               | rfam_acc     | fk_rfam_database_link_family1                        | family                | rfam_acc               |
| family                      | auto_wiki    | fk_family_wikitext1                                  | wikitext              | auto_wiki              |
| family_literature_reference | pmid         | fk_family_literature_reference_literature_reference1 | literature_reference  | pmid                   |
| family_literature_reference | rfam_acc     | fk_family_literature_reference_family1               | family                | rfam_acc               |
| family_long                 | rfam_acc     | fk_family_long_family1                               | family                | rfam_acc               |
| family_ncbi                 | ncbi_id      | fk_family_ncbi_taxonomy1                             | taxonomy              | ncbi_id                |
| family_ncbi                 | rfam_acc     | fk_rfam_ncbi_family1                                 | family                | rfam_acc               |
| features                    | rfamseq_acc  | fk_features_rfamseq1                                 | rfamseq               | rfamseq_acc            |
| full_region                 | rfam_acc     | fk_full_region_family_cascade                        | family                | rfam_acc               |
| full_region                 | rfamseq_acc  | fk_full_region_rfamseq1_cascase                      | rfamseq               | rfamseq_acc            |
| html_alignment              | rfam_acc     | fk_html_alignments_family1                           | family                | rfam_acc               |
| matches_and_fasta           | rfam_acc     | fk_matches_and_fasta_family1                         | family                | rfam_acc               |
| motif_database_link         | motif_acc    | motif_database_link_ibfk_1                           | motif                 | motif_acc              |
| motif_family_stats          | motif_acc    | motif_family_stats_motif_acc                         | motif_old             | motif_acc              |
| motif_family_stats          | rfam_acc     | motif_family_stats_rfam_acc                          | family                | rfam_acc               |
| motif_file                  | motif_acc    | fk_motif_file_motif                                  | motif                 | motif_acc              |
| motif_literature            | motif_acc    | motif_literature_motif_acc                           | motif_old             | motif_acc              |
| motif_literature            | pmid         | motif_literature_pmid                                | literature_reference  | pmid                   |
| motif_matches               | motif_acc    | motif_match_motif_acc                                | motif_old             | motif_acc              |
| motif_matches               | rfam_acc     | motif_match_rfam_acc                                 | family                | rfam_acc               |
| motif_matches               | rfamseq_acc  | motif_match_rfamseq_acc                              | rfamseq               | rfamseq_acc            |
| motif_pdb                   | motif_acc    | motif_pdb_motif_acc                                  | motif_old             | motif_acc              |
| motif_ss_image              | motif_acc    | fk_motif_ss_images_motif1                            | motif_old             | motif_acc              |
| motif_ss_image              | rfam_acc     | fk_motif_ss_images_family1                           | family                | rfam_acc               |
| pdb_rfam_reg                | pdb_id       | fk_pdb_rfam_reg_pdb1                                 | pdb                   | pdb_id                 |
| pdb_rfam_reg                | pdb_seq      | fk_pdb_rfam_reg_pdb_sequence1                        | pdb_sequence          | pdb_seq                |
| pdb_rfam_reg                | rfam_acc     | fk_pdb_rfam_reg_family1                              | family                | rfam_acc               |
| pdb_rfam_reg                | rfamseq_acc  | fk_pdb_rfam_reg_rfamseq1                             | rfamseq               | rfamseq_acc            |
| pdb_sequence                | pdb_id       | fk_pdb_sequence_pdb1                                 | pdb                   | pdb_id                 |
| processed_data              | rfam_acc     | fk_rfam_CM_family1                                   | family                | rfam_acc               |
| pseudoknot                  | rfam_acc     | fk_family_pseudoknot                                 | family                | rfam_acc               |
| refseq_full_region          | refseq_acc   | fk_refseq_full_region_refseq1                        | refseq                | refseq_acc             |
| refseq_full_region          | rfam_acc     | fk_full_region_family1                               | family                | rfam_acc               |
| rfamseq                     | ncbi_id      | fk_rfamseq_taxonomy1                                 | taxonomy              | ncbi_id                |
| secondary_structure_image   | rfam_acc     | fk_secondary_structure_images_family1                | family                | rfam_acc               |
| seed_region                 | rfam_acc     | fk_rfam_reg_seed_family1                             | family                | rfam_acc               |
| seed_region                 | rfamseq_acc  | fk_rfam_reg_seed_rfamseq1                            | rfamseq               | rfamseq_acc            |
| sunburst                    | rfam_acc     | fk_table1_family3                                    | family                | rfam_acc               |
+-----------------------------+--------------+------------------------------------------------------+-----------------------+------------------------+
48 rows in set (0.222 sec)
```

### SQL Query 2 - Common Columns Across Tables (Supplementary):
```sql
SELECT 
  COLUMN_NAME,
  COUNT(DISTINCT TABLE_NAME) AS table_count
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'Rfam'
GROUP BY COLUMN_NAME
HAVING COUNT(DISTINCT TABLE_NAME) > 1
ORDER BY COUNT(DISTINCT TABLE_NAME) DESC, COLUMN_NAME;
```

**Result:**
```
+-------------------+-------------+
| COLUMN_NAME       | table_count |
+-------------------+-------------+
| rfam_acc          |          30 |
| comment           |          11 |
| description       |          11 |
| rfamseq_acc       |          10 |
| type              |          10 |
| author            |           9 |
| motif_acc         |           9 |
| created           |           8 |
| ncbi_id           |           7 |
| pdb_id            |           6 |
| updated           |           6 |
| bit_score         |           5 |
| chain             |           5 |
| clan_acc          |           5 |
| seq_end           |           5 |
| seq_start         |           5 |
| cm                |           4 |
| cm_end            |           4 |
| cm_start          |           4 |
| evalue_score      |           4 |
| pmid              |           4 |
| rfam_id           |           4 |
| species           |           4 |
| title             |           4 |
| upid              |           4 |
| version           |           4 |
| clen              |           3 |
| cmbuild           |           3 |
| cmcalibrate       |           3 |
| db_id             |           3 |
| db_link           |           3 |
| ecmli_cal_db      |           3 |
| ecmli_cal_hits    |           3 |
| ecmli_lambda      |           3 |
| ecmli_mu          |           3 |
| gathering_cutoff  |           3 |
| hex_colour        |           3 |
| hmm_lambda        |           3 |
| hmm_tau           |           3 |
| is_significant    |           3 |
| match_pair_node   |           3 |
| maxl              |           3 |
| noise_cutoff      |           3 |
| order_added       |           3 |
| other_params      |           3 |
| pdb_end           |           3 |
| pdb_start         |           3 |
| seed              |           3 |
| seed_source       |           3 |
| source            |           3 |
| trusted_cutoff    |           3 |
| accession         |           2 |
| assembly_acc      |           2 |
| assembly_level    |           2 |
| assembly_name     |           2 |
| assembly_version  |           2 |
| author_id         |           2 |
| auto_overlap      |           2 |
| auto_wiki         |           2 |
| chromosome_name   |           2 |
| chromosome_type   |           2 |
| circular          |           2 |
| closed            |           2 |
| common_name       |           2 |
| embl_release      |           2 |
| forward_to        |           2 |
| id                |           2 |
| image             |           2 |
| is_reference      |           2 |
| is_representative |           2 |
| kingdom           |           2 |
| length            |           2 |
| level             |           2 |
| lft               |           2 |
| lsf_id            |           2 |
| md5               |           2 |
| message           |           2 |
| mol_type          |           2 |
| motif_id          |           2 |
| num_families      |           2 |
| num_rfam_regions  |           2 |
| num_seed          |           2 |
| number_families   |           2 |
| opened            |           2 |
| parent            |           2 |
| pdb_seq           |           2 |
| previous_acc      |           2 |
| previous_id       |           2 |
| refseq_acc        |           2 |
| rfam_release      |           2 |
| rfam_release_date |           2 |
| rgt               |           2 |
| scientific_name   |           2 |
| status            |           2 |
| study_ref         |           2 |
| taxonomy          |           2 |
| total_length      |           2 |
| truncated         |           2 |
| ungapped_length   |           2 |
| user              |           2 |
| uuid              |           2 |
| wgs_acc           |           2 |
| wgs_version       |           2 |
| wiki              |           2 |
+-------------------+-------------+
104 rows in set (0.410 sec)
```

## Question 2c: Rice Type with Longest DNA Sequence

### Question:
Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)

### SQL Query:
```sql
SELECT 
  t.species,
  t.ncbi_id,
  rf.length AS sequence_length
FROM rfamseq rf
JOIN taxonomy t ON rf.ncbi_id = t.ncbi_id
WHERE t.tax_string LIKE '%Oryza%'
ORDER BY rf.length DESC
LIMIT 1;
```

**Results:**
```
+-----------------+---------+-----------------+
| species         | ncbi_id | sequence_length |
+-----------------+---------+-----------------+
| Oryza granulata |  110450 |        80745213 |
+-----------------+---------+-----------------+
1 row in set (0.893 sec)
```

### Answer:
Rice type with longest DNA squence is **Oryza granulata**  

#### Details:
- Species: Oryza granulata
- ncbi_id: 110450
- Sequence length: 80,745,213
## Question 2d: Paginated Family Names with Long DNA Sequences

### Question:
We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)

### Approach

- Results per page: 15
- Page number: 9
- Offset = (Page Number - 1) × Results per Page = (9 - 1) × 15 = 120

### SQL Query:
```sql
SELECT
  f.rfam_acc AS family_accession_id,
  f.rfam_id AS family_name,
  MAX(rs.length) AS max_length
FROM family f
JOIN full_region fr ON f.rfam_acc = fr.rfam_acc
JOIN rfamseq rs ON fr.rfamseq_acc = rs.rfamseq_acc
GROUP BY f.rfam_acc, f.rfam_id
HAVING MAX(rs.length) > 1000000
ORDER BY max_length DESC
LIMIT 15 OFFSET 120;
```

**Results:**
```
+---------------------+--------------+------------+
| family_accession_id | family_name  | max_length |
+---------------------+--------------+------------+
| RF01848             | ACEA_U3      |  836514780 |
| RF01856             | Protozoa_SRP |  836514780 |
| RF01911             | MIR2118      |  836514780 |
| RF03160             | twister-P1   |  836514780 |
| RF03209             | MIR9657      |  836514780 |
| RF03674             | MIR5387      |  836514780 |
| RF03685             | MIR9677      |  836514780 |
| RF03896             | MIR2275      |  836514780 |
| RF03926             | MIR1435      |  836514780 |
| RF04110             | MIR5084      |  836514780 |
| RF04251             | MIR5070      |  836514780 |
| RF00145             | snoZ105      |  830829764 |
| RF00134             | snoZ196      |  801256715 |
| RF00160             | snoZ159      |  801256715 |
| RF00202             | snoR66       |  801256715 |
+---------------------+--------------+------------+
15 rows in set (2 min 8.844 sec)
```

### Answer:
The query successfully returns the 9th page (results 121-135) of families with DNA sequence lengths greater than 1,000,000, sorted by maximum length in descending order.