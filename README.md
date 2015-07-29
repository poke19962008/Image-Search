# Image Search

Image Search prototype for SRM Search Engine

## filter.py
- Converts txt dump to JSON format.
- Tokenise 'name' and 'folder' and remove stop words, non-ASCII characters.
- Assigns 'docID' and 'viewRank'
 
## mainIndex.py
- Produces MySQL Inverted Density Frequency table of **name** from JSON dump.
- 'ID' further links with Stem Index

## docTable.py
- Converts JSON from filter.py to MySQL
 
## Upcoming commits
- [ ] Porter Stemmer Indexing of 'ID' from 'Main_Index.sql'.
 -  http://tartarus.org/martin/PorterStemmer/def.txt 
- [ ] Intersection of docIDs.
- [ ] Set ranking parameters.

## Resource Websites Used
- www.archive.org
