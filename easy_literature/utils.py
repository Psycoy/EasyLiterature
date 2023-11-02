import os 
import logging
import re 
from tqdm import tqdm 
from .downloads import get_paper_info_from_paperid, get_paper_pdf_from_paperid, classify


logging.basicConfig()
logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)


class patternRecognizer(object):
    def __init__(self, regular_rule):
        self.pattern = re.compile(regular_rule)

    def match(self, string):
        return self.pattern.match(string)
    
    def findall(self, string):
        return self.pattern.findall(string)

    def multiple_replace(self, content, **replace_dict):
        def replace_(value):
            match = value.group()
            if match in replace_dict.keys():
                return replace_dict[match]
            else:
                return match+" **Not Correct, Check it. Maybe mannual update & download is needed.**"
        
        replace_content = self.pattern.sub(replace_, content)
        
        return replace_content
    

def note_modified(pattern_recog, md_file, **replace_dict):
    with open(md_file, 'r') as f:
        content = f.read()
    
    replaced_content = pattern_recog.multiple_replace(content, **replace_dict)

    with open(md_file, 'w') as f:
        f.write(''.join(replaced_content))
        

def get_pdf_paths(pdf_root):
    pdf_paths = []
    for root, _, files in os.walk(pdf_root):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_paths.append(os.path.join(root, file))
                
    return pdf_paths
 
        
def get_pdf_paths_from_notes(md_root, reg):
    
    md_files = []
    for root, _, files in os.walk(md_root):
        for file in files:
            if file.lower().endswith('md') or file.lower().endswith('markdown'):
                md_files.append(os.path.join(root, file))
    
    pdf_paths_from_notes = []
    for md_file in md_files:
        with open(md_file, 'r') as f:
            content = f.read()
        m = reg.findall(content)
        m = [i.split("(")[-1].split(')')[0] for i in m]
        pdf_paths_from_notes.extend(m)

    return pdf_paths_from_notes


def get_pdf_paths_from_notes_dict(md_root, reg):
    pdf_paths_from_notes_dict = {}
    if os.path.isdir(md_root):
        md_files = []
        for root, _, files in os.walk(md_root):
            for file in files:
                if file.lower().endswith('md') or file.lower().endswith('markdown'):
                    md_files.append(os.path.join(root, file))
    
        for md_file in md_files:
            with open(md_file, 'r') as f:
                content = f.read()
            m = reg.findall(content)
            m = [i.split("(")[-1].split(')')[0] for i in m]
            pdf_paths_from_notes_dict[md_file] = m
    else:
        with open(md_root, 'r') as f:
            content = f.read()
        m = reg.findall(content)
        m = [i.split("(")[-1].split(')')[0] for i in m]
        pdf_paths_from_notes_dict[md_root] = m
            
    return pdf_paths_from_notes_dict


def classify_identifier(identifier):
    """Not need to download PDF file 
    """
    if identifier.endswith("}}"):
        return True 
    else: 
        return False 


def get_update_content(m, note_file, pdfs_path, proxy, gproxy_mode):
    
    replace_dict = dict()
    for literature in tqdm(m):
        pdf = classify_identifier(literature)
        
        literature_id = literature.split('{')[-1].split('}')[0]
        bib = get_paper_info_from_paperid(literature_id, proxy=proxy, gproxy_mode=gproxy_mode)
        
        if bib:
            try:
                pdf_name = bib['title']
                # remove blank symbol, like \n, \t, \r
                pdf_name = re.sub(r'[\n\t\r]', '', pdf_name)
                # remove multiple blank spaces
                pdf_name = re.sub(r' +', ' ', pdf_name)
                pdf_name = re.sub(r'[.]', '', pdf_name)

                pdf_name = '_'.join(pdf_name.split(' ')) + '.pdf'

                # remove the special characters in the pdf name: / \ : * ? " < > |
                pdf_name = re.sub(r'[\\/:*?"<>|]', '', pdf_name)
                pdf_path = os.path.join(pdfs_path, pdf_name)
                
                logger.info(f"The pdf path to be saved: {pdf_path}")
                if pdf:
                    id_type = classify(literature_id)
                    if id_type == "title":
                        for pattern_str in [r'10\.(?!1101)[0-9]{4}/', r'10\.1101/', r'[0-9]{2}[0-1][0-9]\.[0-9]{3,}', r'.*/[0-9]{2}[0-1][0-9]{4}']:
                            res = re.search(pattern_str, bib['url'])  # search for the arxiv id in the url
                            if res:
                                literature_id = res.group(0)
                                if bib['pdf_link'] is None:
                                    bib['pdf_link'] = f'https://arxiv.org/pdf/{literature_id}.pdf'
                                logger.info(f"The paper's arxiv url: {bib['url']}; The converted arxiv id: {literature_id}; The pdf link: {bib['pdf_link']}.")
                        if not os.path.exists(pdf_path):
                            logger.info(f"PDF link: {bib['pdf_link']}")
                            get_paper_pdf_from_paperid(literature_id, pdf_path, direct_url=bib['pdf_link'], proxy=proxy)
                            if not os.path.exists(pdf_path):
                                get_paper_pdf_from_paperid(literature_id, pdf_path, proxy=proxy)
                    else:
                        if not os.path.exists(pdf_path):
                            logger.info(f"PDF link: {bib['pdf_link']}")
                            get_paper_pdf_from_paperid(literature_id, pdf_path, direct_url=bib['pdf_link'], proxy=proxy)
                            if not os.path.exists(pdf_path):
                                get_paper_pdf_from_paperid(literature_id, pdf_path, proxy=proxy)
                if os.path.exists(pdf_path):
                    replaced_literature = "- **{}**. {} et.al. **{}**, **{}**, **Number of Citations: **{}, ([pdf]({}))([link]({})).".format(
                                        bib['title'], bib["author"].split(" and ")[0], bib['journal'], 
                                        bib['year'], bib['cited_count'], os.path.relpath(pdf_path, note_file).split('/',1)[-1], 
                                        bib['url'])
                else:
                    logger.info("Can not find a downloading source for literature id {}. You may need to manually download this paper, a template has been generated in the markdown file. Put the pdf file in the folder you specified just now and add its name in the '(pdf)' of your markdown entry.".format(literature_id))
                    replaced_literature = "- **{}**. {} et.al. **{}**, **{}**, **Number of Citations: **{}, ([pdf]({}))([link]({})).".format(
                                            bib['title'], bib["author"].split(" and ")[0], bib['journal'], 
                                            bib['year'], bib['cited_count'], f'{pdfs_path}/your_pdf_name.pdf', bib['url']
                                            )
                replace_dict[literature] = replaced_literature
            except:
                
                    logger.info("Can not find a downloading source for literature id {}. You may need to manually download this paper, a template has been generated in the markdown file. Put the pdf file in the folder you specified just now and add its name in the '(pdf)' of your markdown entry.".format(literature_id))
                    replaced_literature = "- **{}**. {} et.al. **{}**, **{}**, **Number of Citations: **{}, ([pdf]({}))([link]({})).".format(
                                            bib['title'], bib["author"].split(" and ")[0], bib['journal'], 
                                            bib['year'], bib['cited_count'], f'{pdfs_path}/your_pdf_name.pdf', bib['url']
                                            )
                    replace_dict[literature] = replaced_literature
        else:
            logger.info("Can not find the literature {}. You may need to manually download this paper, a template has been generated in the markdown file. Put the pdf file in the folder you specified just now and add its name in the '(pdf)' of your markdown entry.".format(literature_id))
            replaced_literature = "- **{}**. ([pdf]({})).".format(
                                            literature_id, f'{pdfs_path}/your_pdf_name.pdf'
                                            )
            replace_dict[literature] = replaced_literature
    return replace_dict 