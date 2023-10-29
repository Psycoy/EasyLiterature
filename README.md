# EasyLiterature
**EasyLiterature** is a Python-based command line tool for automatic literature management. Welcome star or contribute!

（**EasyLiterature** 是一个基于python的命令行文件管理工具，永久开源，欢迎star或contribute）

Simply list the paper titles (or ids) you want to read in a markdown file and it will automatically `collect and refine its information in the markdown file`, `download the pdf to your local machine`, and `link the pdf to your paper in the markdown file`. You can forever keep your notes within the pdfs and mds on your local machine or cloud driver.

（简单来说，在 Markdown 文件中简单列出想要阅读的论文标题（或ID），它会自动收集并在Markdown文件中完善相关信息，下载论文的PDF到本地机器，并将PDF链接到Markdown文件中的论文。通过这样的流程，我们可以实现永久保存实时编辑的论文PDF和Markdown中的笔记，无论是在本地机器还是云端，并且方便论文一站式分类和管理。）

Inspired by [Mu Li](https://www.bilibili.com/video/BV1nA41157y4), adapted from [autoLiterature](https://github.com/wilmerwang/autoLiterature). 
Compared to autoLiterature, **EasyLiterature** is much easier to use and supports a wider range of features, such as `title-based paper match`, `paper search and download on Google Scholar and DLBP` (the two main sites for scholars), `citation statistics`, `mannual information update assitant`, etc. **EasyLiterature covers almost all papers thanks to the support of Google Scholar and DLBP!**

（与之前的实现相比，EasyLiterature兼容之前实现的所有功能，并且支持更多功能，比如：1. 基于标题的论文匹配；2. Google Scholar和DLBP（全球两大主要paper数据库）的论文搜索和下载；3. 引用统计；4. 手动信息更新助手；5. 容错搜索匹配；等等。之前的实现由于数据库的限制，很多文章都找不到。EasyLiterature得益于增加了Google Scholar和DLBP的支持，几乎覆盖了所有论文。）


**Recognition rules (识别规则)：**
- Automatically recognizes `- {xxx}`。
- If the notes file contains`- {paper_id}`, it will download the information of that literature, but not the PDF.
- If the notes file contains `- {{paper_id}}`, it will download both the information of that literature and the PDF.

Note: `paper_id` supports `the title of the article`, published articles' `doi`, and pre-published articles' `arvix_id`, `biorvix_id`, and `medrvix_id`. It will try all the possible sources online.

## Install (安装)
1. pip install (to do)
```bash 
pip install easyliter
or
pip3 install easyliter
```

2. install from source
```bash
git clone https://github.com/Psycoy/EasyLiterature.git
cd EasyLiterature
python setup.py install
```

### Arguments（使用参数）
```bash
easyliter

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

## Usage（使用）
### Basic Usage（基本使用）
Assuming `input` is the folder path of the literature notes (.md files) and `output` is the folder path where you want to save the PDFs.

```bash
# Update all md files in the input folder
easyliter -i input -o output 

# Only update the input/example.md file
easyliter -i input/example.md -o output  

# -d is an optional flag, when -i is a folder path, using -d will delete unrelated pdf files in the PDF folder from the literature notes content
easyliter -i input -o output -d
```

### Migrating Notes and PDF Files（笔记和pdf文件的迁移）
When you need to move the literature notes or the PDF folder, the links to the PDFs in the literature notes might become unusable. You can use `-m` to re-link the PDF files with the literature notes.

```bash
# Update all md files in the input folder
easyliter -i input -m movedPDFs/

# Only update the input/example.md file
easyliter -i input/example.md -m movedPDFs/  
```


## License
MIT
