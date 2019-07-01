#!/usr/bin/python3

from operator import attrgetter

class bibtex_entry:

    def __init__(self, key, pub_type):
        self.key = key
        if pub_type == 'INPROCEEDING':
            self.pub_type = 'CONFABSTRACT'
        else:
            self.pub_type = pub_type
        # 'required' fields should be set to '' here
        self.month = ''
        self.booktitle = ''
        self.pages = ''
        self.publisher = ''
        self.volume = ''
        self.number = ''
        
    def update_title(self, title):
        self.title = title

    def update_author(self, author):
        # make sure last name is first so sorting works
        author_list = author.split(' and ')
        new_author_list = []
        for author in author_list:
            if ',' not in author:
                sub_author_list = author.split(' ')
                new_author_list.append(sub_author_list[-1] + ', ' + ' '.join(sub_author_list[:-1]))
            else:
                new_author_list.append(author)
        self.author = ' and '.join(new_author_list)

    def update_journal(self, journal):
        self.journal = journal

    def update_month(self, month):
        self.month = month

    def update_year(self, year):
        self.year = int(year)

    def update_doi(self, doi):
        self.doi = doi

    def update_doi2(self, doi2):
        self.doi2 = doi2

    def update_volume(self, volume):
        self.volume = volume

    def update_number(self, number):
        self.number = number
        
    def update_pages(self, pages):
        self.pages = pages

    def update_pdf_url(self, pdf_url):
        if self.pub_type == 'CONFABSTRACT':
            self.pub_type = 'INPROCEEDING'
        self.pdf_url = pdf_url

    def update_pmid(self, pmid):
        self.pmid = pmid

    def update_issue(self, issue):
        self.issue = issue
        
    def update_pmcid(self, pmcid):
        self.pmcid = pmcid

    def update_note(self, note):
        self.note = note

    def update_official_url(self, official_url):
        self.official_url = official_url

    def update_publisher(self, publisher):
        self.publisher = publisher
        
    def update_pdf_url2(self, pdf_url2):
        self.pdf_url2 = pdf_url2

    def update_pdf2_url(self, pdf2_url):
        self.pdf2_url = pdf2_url

    def update_issn(self, issn):
        self.issn = issn

    def update_address(self, address):
        self.address = address

    def update_day(self, day):
        self.day = day

    def update_abstract_url(self, abstract_url):
        self.abstract_url = abstract_url

    def update_cnote(self, cnote):
        self.cnote = cnote

    def update_ps_url(self, ps_url):
        if self.pub_type == 'CONFABSTRACT':
            self.pub_type = 'INPROCEEDING'
        self.ps_url = ps_url

    def update_ps2_url(self, ps2_url):
        self.ps2_url = ps2_url

    def update_booktitle(self, booktitle):
        self.booktitle = booktitle

    def update_school(self, school):
        self.school = school

    def update_editor(self, editor):
        self.editor = editor

    def update_chapter(self, chapter):
        self.chapter = chapter

    def update_isbn(self, isbn):
        self.isbn = isbn

    def update_edition(self, edition):
        self.edition = edition

    def update_series(self, series):
        self.series = series

    def update_institution(self, institution):
        self.institution = institution

    def update_date(self, date):
        self.date = date

    def update_url(self, url):
        self.url = url

    def parse_bibtex_entry(self, entry_str):
        opening_brace = entry_str.find('{')
        etype = entry_str[1 : opening_brace]
        entry_fields = entry_str[opening_brace+1 :].split(',')
        key = entry_fields.pop(0)

        curr_obj = bibtex_entry(key, etype)
        for field in entry_fields:
            kv = field.split('=')
            if len(kv) != 2:
                continue
            else:
                curr_val = kv[1].strip(' "')
                curr_key = kv[0].strip(' ')

            if curr_key[0] == 'x' or curr_key[0] == 'b' or curr_key[0] == 'c':
                continue
            elif curr_key == 'TITLE':
                curr_obj.update_title(curr_val)
            elif curr_key == 'AUTHOR':
                curr_obj.update_author(curr_val)
            elif curr_key == 'JOURNAL':
                curr_obj.update_journal(curr_val)
            elif curr_key == 'MONTH':
                curr_obj.update_month(curr_val)
            elif curr_key == 'YEAR':
                curr_obj.update_year(curr_val)
            elif curr_key == 'DOI':
                curr_obj.update_doi(curr_val)
            elif curr_key == 'DOI2':
                curr_obj.update_doi2(curr_val)
            elif curr_key == 'VOLUME':
                curr_obj.update_volume(curr_val)
            elif curr_key == 'NUMBER':
                curr_obj.update_number(curr_val)
            elif curr_key == 'PAGES':
                curr_obj.update_pages(curr_val)
            elif curr_key == 'PDF-URL':
                curr_obj.update_pdf_url(curr_val)
            elif curr_key == 'PMID':
                curr_obj.update_pmid(curr_val)
            elif curr_key == 'ISSUE':
                curr_obj.update_issue(curr_val)
            elif curr_key == 'PMCID':
                curr_obj.update_pmcid(curr_val)
            elif curr_key == 'NOTE':
                curr_obj.update_note(curr_val)
            elif curr_key == 'OFFICIAL-URL':
                curr_obj.update_official_url(curr_val)
            elif curr_key == 'PUBLISHER':
                curr_obj.update_publisher(curr_val)
            elif curr_key == 'PDF-URL2':
                curr_obj.update_pdf_url2(curr_val)
            elif curr_key == 'PDF2-URL':
                curr_obj.update_pdf2_url(curr_val)
            elif curr_key == 'ISSN':
                curr_obj.update_issn(curr_val)
            elif curr_key == 'ADDRESS':
                curr_obj.update_address(curr_val)
            elif curr_key == 'DAY':
                curr_obj.update_day(curr_val)
            elif curr_key == 'ABSTRACT-URL':
                curr_obj.update_abstract_url(curr_val)
            elif curr_key == 'cNOTE':
                curr_obj.update_cnote(curr_val)
            elif curr_key == 'PS-URL':
                curr_obj.update_ps_url(curr_val)
            elif curr_key == 'PS2-URL':
                curr_obj.update_ps2_url(curr_val)
            elif curr_key == 'BOOKTITLE':
                curr_obj.update_booktitle(curr_val)
            elif curr_key == 'SCHOOL':
                curr_obj.update_school(curr_val)
            elif curr_key == 'EDITOR':
                curr_obj.update_editor(curr_val)
            elif curr_key == 'CHAPTER':
                curr_obj.update_chapter(curr_val)
            elif curr_key == 'ISBN':
                curr_obj.update_isbn(curr_val)
            elif curr_key == 'EDITION':
                curr_obj.update_edition(curr_val)
            elif curr_key == 'SERIES':
                curr_obj.update_series(curr_val)
            elif curr_key == 'INSTITUTION':
                curr_obj.update_institution(curr_val)
            elif curr_key == 'DATE':
                curr_obj.update_date(curr_val)
            elif curr_key == 'URL':
                curr_obj.update_url(curr_val)
            else:
                #print('bad key {0}'.format(curr_key))
                # ignore all other keys
                continue
        return curr_obj

    def display_author_lcv(self):
        # display author in format: First Middle Last
        # so swap if comma in author
        author_list = []
        for author in self.author.split(' and '):
            if ',' in author: # assuming only 1 comma
                sub_author_list = author.split(',')
                author_list.append(sub_author_list[-1].strip() + ' ' +
                                   ''.join(sub_author_list[:-1]))
            else:
                author_list.append(author)
        return ' and '.join(author_list)

    def display_author_vnl(self):
        pass
    
    def display_entry_lcv(self, obj):
        #### FIX: this can be refactored to remove redundancy!!!
        if obj.pub_type == 'INPROCEEDINGS':
            pages = ''
            if obj.pages != '':
                pages = 'pages {0}.'.format(obj.pages)
            publisher = ''
            if obj.publisher != '':
                publisher = ' {0},'.format(obj.publisher)
            print('<P><B>{0}</B><BR>{1}. Published in {2}, {3} {4} {5} {6}.</P>'.format(obj.title,
                                                                                        obj.display_author_lcv(),
                                                                                        obj.booktitle,
                                                                                        pages, publisher,
                                                                                        obj.month,
                                                                                        obj.year))
        elif obj.pub_type == 'ARTICLE':
            volnum = ''
            if obj.volume !=  '' and obj.number != '':
                volnum = '{0} ({1}),'.format(obj.volume, obj.number)
            elif obj.volume != '':
                volnum = '{0},'.format(obj.volume)
            pages = ''
            if obj.pages != '':
                pages = 'pages {0}.'.format(obj.pages)            
            print('<P><B>{0}</B><BR>{1}. Published in {2}, {3}, pp.{4}, {5} {6}.</P>'.format(obj.title,
                                                                                                   obj.display_author_lcv(),
                                                                                                   obj.journal,
                                                                                                   volnum,
                                                                                                   pages,
                                                                                                   obj.month,
                                                                                                   obj.year))
        #elif obj.pub_type == 
        

class bibtex_repo(bibtex_entry):

    entry_list = []

    def __init__(self, filename):
        self.filename = filename
        bib_entry_list = self.parse_bibtex_file(self.filename)

    def parse_bibtex_file(self, filename):
        print('parse_bibtex_file')

        entry = ''
        entry_list = []
        with open(filename, 'r', encoding='ISO-8859-1') as fp:
            for line in fp:
                line = line.strip().replace('\t','')
                if len(line) == 0:
                    continue
                
                if line[0] == '@' and line != '@COMMENT':
                    # new entry, so save last entry
                    if entry != '':
                        # remove any comments after closing bracket
                        entry = entry[:entry.rfind('}')]
                        entry_obj = self.parse_bibtex_entry(entry)
                        entry_list.append(entry_obj)
                    # start new entry
                    entry = line
                elif line[0] != '%' and line != '':
                    entry += line
        self.entry_list = entry_list

    def need_divider(curr_obj, prev_obj, sort_method):
        # do we need a divider based on current and prev
        #   objects and display method (date, author, etc.)
        if sort_method == 'date':
            if curr_obj.year != prev_obj.year:
                return True
            else:
                return False
        elif sort_method == 'author':
            if curr_obj.author != prev_obj.author:
                return True
            else:
                return False
        elif sort_method == 'pub_type':
            if curr_obj.pub_type != prev_obj.pub_type:
                return True
            else:
                return False
            
    def display_divider_lcv(obj):
        pass
    
    def write_all_pages(self, mode, out_path):
        print('displaying html')
        # need to sort then write each page type
        #entry_list_date = sorted(self.entry_list, key=attrgetter('year','author'), reverse = True)
        entry_list_date = sorted(self.entry_list, key=attrgetter('author'))
        entry_list_date = sorted(entry_list_date, key=attrgetter('year'),
                                 reverse = True)
               
        prev_obj = ''
        for obj in entry_list_date:
            if self.need_divider(obj, prev_obj):
                self.display_divider_lcv(obj)
            self.display_entry_lcv(obj)
            pref_obj = obj

bibtex_repo('simoncelli.bib').write_all_pages('lcv','path')

