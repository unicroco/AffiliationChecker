import csv
try:
    authors = open('001_authors.csv', 'r')  # file contains authors to find
    try:
        with open('002_publications.csv', 'r') as csvfile:  # main list with all publications downloaded from PubMed
            affiliation = csv.reader(csvfile, delimiter = ',', quotechar = '"')
            try:
                n_i = open('003_nature_index.csv', 'r')  # opening a list with nature index journals
                author_list = [str(line).strip() for line in authors.readlines()]
                nature_index_list = [str(line).strip().lower() for line in n_i.readlines()]

                with open('corrected_affiliation.csv', 'w', newline='') as file_to_write:
                    writer = csv.writer(file_to_write, delimiter = ';')
                    writer.writerow(["Main", "PMID", "Year", "Affiliation Author", "First Author", "Journal", "DOI", "Link", "Nature Index"])

                    for row in affiliation:
                        pmid_counter = 0
                        affiliation_author_set = set()
                        body = str(row[0].strip('"')).replace('"', '')
                        pmid = body[:body.find(',')]
                        pmid_counter += 1
                        first_author = row[1].strip('""')
                        journal = row[2].strip('""')
                        year = row[3].strip('""')
                        pmc = row[5].strip('""')
                        doi = row[7].strip('"')
                        link = 'https://pubmed.ncbi.nlm.nih.gov/'+pmid
                        title_authors = body[body.find(',')+1:]
                        n_index = ''

                        for i in range(len(author_list)):
                            if author_list[i].lower() not in body.lower() or len(author_list[i])< 1:
                                pass  # a loop to exclude extra authors from other departments, laboratories etc.
                            else:
                                affiliation_author_set.add(author_list[i])
                                for j in range(len(nature_index_list)):
                                    if nature_index_list[j].lower() not in journal.lower():   # a loop to add nature index 
                                        pass
                                    else:
                                        n_index = 'Nature Index'

                        if len(affiliation_author_set) < 1:  # to exclude empty lines from authors list if they are exists 
                            pass
                        else:
                            affiliation_author = ', '.join(affiliation_author_set)  # to add all authors in one row instead of creating one row wor each author
                            writer.writerow([body, pmid,  year, affiliation_author, first_author, journal, doi, link, n_index])  # adding all rows to a new file

                    print("Jobs done!")
                    file_to_write.close()
                    n_i.close()
                    csvfile.close()
                    authors.close()

            except FileNotFoundError:
                print('No such file or directory: 002_publications, press any key to exit')
                b = input()
                exit()

    except FileNotFoundError:
        print('No such file or directory: 002_publications, press any key to exit')
        b = input()
        exit()

except FileNotFoundError:
    print('No such file or directory: 001_authors, press any key to exit')
    b = input()
    exit()