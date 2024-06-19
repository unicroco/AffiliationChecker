# AffiliationChecker
This is the first version of the script that allows you to compile and add articles downloaded from Pubmed to a csv file.
What functionality is implemented:

1. Filter out publications by irrelevant authors with the requested affiliation
2. Add a link to an article on Pubmed
3. If several authors have written the same article, it does not duplicate the entry, but adds all the authors to the entry
4. Sets Nature index of article if this condition is satisfied

When this script could be used:
1. While working with a large array, when it is necessary to process articles for uploading to the site, to
the annual report, etc.
2. When it is necessary to reformat the csv files downloaded from Pubmed due to regional differences*

What columns does the script create?
• Home Page
• PMID
• Year of manufacture
• Affiliation with the authors
• The first author
• DOI of the journal
• Link
• Nature Index

Usage example:
1. Download the list of publications in a csv file with the required affiliation to your computer from the
Pubmed library. Link https://pubmed.ncbi.nlm.nih.gov /?term= With multiple affiliations, you can add
everything one by one to a single file
2. Add the list of publications to the 002_publications.csv file at the root of the directory
3. Check the list of authors in the 001_authors file. It is recommended to use the surname together with
the first letter of the name to exclude namesakes. If the author has a double spelling of the surname,
add both options to the column.
4. Double-click on af_ch.exe if you are using an exe file or run af_ch.py in any convenient interpreter
5. A corrected_affilation file will be created with a list of all sorted publications.

Notes.
• *Due to regional differences, CSV files use a different delimiter symbol, which means that when
opening a file in other regions, the entire record can be compiled without splitting into different
columns. The script allows you to adapt the division of columns in the European region and Asia. Please
let me know if there are any errors.
• Realizing the presence of virus threats, in addition to the executable file, a Syntax file was added so
that each user could safely download the script and view it. Also, I added the project in .py format.
• Since Pubmed does not accurately filter out affiliations, there may be cases when an article written by
an author from a list with another affiliation will still be in the output due to the presence of other
authors with the requested affiliation.
Example: We have the author Robert, New press affiliation; Claudia, Horizont affiliation. When
searching for Robert's author with Horizont affiliation, the article will be presented. This nuance can be
circumvented with full use of the API and will be implemented in future versions.
• Do not delete csv files 001_authors, 002_publications, 003_nature_index
• The Nature index is filled in manually and not all journals can be counted at the moment. When adding
journals by yourself, please take into account the specifics of writing titles in Pubmed. This query can
also be used in another way, for example, to search for articles by authors in specific journals. If such a
search is relevant, please let me know. I will add or rewrite the option if necessary.
• In case of improvements or further developments, please add a link to this github
In case of any questions I’ll be glad to help.
