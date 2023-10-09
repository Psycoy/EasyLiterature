# EasyLiterature
**EasyLiterature** is a Python-based command line tool for automatic literature management.

Simply list the paper titles (or ids) you want to read in a markdown file and it will automatically collect and refine its information in the md file, download the pdf to your local machine, and link the pdf to your paper in the markdown file. You can forever keep your notes within the pdfs and mds on your local machine or cloud driver.

Inspired by [Mu Li](https://www.bilibili.com/video/BV1nA41157y4), adapted from [autoLiterature](https://github.com/wilmerwang/autoLiterature). 
Compared to autoLiterature, **EasyLiterature** is much easier to use and supports a wider range of features, such as **title-based paper match**, **paper search and download on Google Scholar and DLBP** (the two largest sites in the world), **citation statistics**, **mannual information update template**, etc. EasyLiterature covers almost all papers thanks to the support of Google Scholar and DLBP!


**Recognition rules：**
- Automatically recognizes `- {xxx}`。
- If the notes file contains`- {paper_id}`, it will download the information of that literature, but not the PDF.
- If the notes file contains `- {{paper_id}}`, it will download both the information of that literature and the PDF.

Note: `paper_id` supports `the title of the article`, published articles' `doi`, and pre-published articles' `arvix_id`, `biorvix_id`, and `medrvix_id`. It will try all the possible sources online.

## Install
1. pip install (to do)
```bash 
pip install easyliter
or
pip3 install easyliter
```

2. install from source
```bash
git clone https://github.com/Psycoy/EasyLiterature.git
cd easyLiterature
python setup.py install
```

### Arguments
```bash
autolter

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The path to the note file or note file folder.
  -o OUTPUT, --output OUTPUT
                        Folder path to save paper pdfs and iamges. NOTE: MUST BE FOLDER
  -p PROXY, --proxy PROXY
                        The proxy. e.g. 127.0.0.1:1080. If this argument is specified, the google scholar will automatically use a free proxy (not necessarily this proxy). To use other proxies for google scholar, change the behaviour in GoogleScholar.set_proxy.
  -d, --delete          Delete unreferenced attachments in notes. Use with caution,
                        when used, -i must be a folder path including all notes
  -m MIGRATION, --migration MIGRATION
                        the pdf folder path you want to reconnect to
```

## Usage
### Basic Usage
Assuming `input` is the folder path of the literature notes (.md files) and `output` is the folder path where you want to save the PDFs.

```bash
# Update all md files in the input folder
autoliter -i input -o output 

# Only update the input/example.md file
autoliter -i input/example.md -o output  

# -d is an optional flag, when -i is a folder path, using -d will delete unrelated pdf files in the PDF folder from the literature notes content
autoliter -i input -o output -d
```

### Migrating Notes and PDF Files
When you need to move the literature notes or the PDF folder, the links to the PDFs in the literature notes might become unusable. You can use `-m` to re-link the PDF files with the literature notes.

```bash
# Update all md files in the input folder
autoliter -i input -m movedPDFs/

# Only update the input/example.md file
autoliter -i input/example.md -m movedPDFs/  
```


## License
MIT