# EasyLiterature
**EasyLiterature** is a Python-based command line tool for automatic literature management. Welcome star or contribute!

Simply list the paper titles (or ids) you want to read in a markdown file and it will automatically `collect and refine its information in the markdown file`, `download the pdf to your local machine`, and `link the pdf to your paper in the markdown file`. You can forever keep your notes within the pdfs and mds on your local machine or cloud driver.

<br>

**A demo of the entries in your markdown note:**

<img src="figures/demo.png" alt="demo" style="zoom:90%;" />

<br>

Inspired by [Mu Li](https://www.bilibili.com/video/BV1nA41157y4), adapted from [autoLiterature](https://github.com/wilmerwang/autoLiterature). 
Compared to autoLiterature, **EasyLiterature** is much easier to use and supports a wider range of features, such as `title-based paper match`, `paper search and download on Google Scholar and DLBP` (the two main sites for scholars), `citation statistics`, `mannual information update assitant`, etc. **EasyLiterature covers almost all papers thanks to the support of Google Scholar and DLBP!**

___

**中文版介绍：**

**EasyLiterature** 是一个基于python的命令行文件管理工具，永久开源，欢迎star或contribute。

之前沐神（李沐）做过一期视频讲如何阅读文献和整理，我觉得讲得非常好，[链接](https://www.bilibili.com/video/BV1nA41157y4)。

简单来说，在 Markdown 文件中简单列出想要阅读的论文标题（或ID），它会自动收集并在Markdown文件中完善相关信息，下载论文的PDF到本地机器，并将PDF链接到Markdown文件中的论文。通过这样的流程，我们可以实现永久保存实时编辑的论文PDF和Markdown中的笔记，无论是在本地机器还是云端，并且方便论文一站式分类和管理。

<br>

**markdown文件中的论文信息条目（示意）:**

<img src="figures/demo.png" alt="demo" style="zoom:90%;" />

<br>

与之前的实现相比，EasyLiterature兼容之前实现的所有功能，并且支持更多功能，比如：1. 基于标题的论文匹配；2. Google Scholar和DLBP（全球两大主要paper数据库）的论文搜索和下载；3. 引用统计；4. 手动信息更新助手；5. 容错搜索匹配；等等。之前的实现由于数据库的限制，很多文章都找不到。EasyLiterature得益于增加了Google Scholar和DLBP的支持，几乎覆盖了所有论文。

<br><br>

## Install (安装)
1. pip install
```bash 
pip install easyliter
or
pip3 install easyliter
```

2. install from source
```bash
git clone https://github.com/Psycoy/EasyLiterature.git
cd EasyLiterature
pip install -e .
```

## Arguments（使用参数）
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


## Recognition Rules (识别规则)：
- Automatically recognizes `- {xxx}`。
- If the notes file contains`- {paper_id}`, it will download the information of that literature, but not the PDF.
- If the notes file contains `- {{paper_id}}`, it will download both the information of that literature and the PDF.

Note: `paper_id` supports `the title of the article`, published articles' `doi`, and pre-published articles' `arvix_id`, `biorvix_id`, and `medrvix_id`. It will try all the possible sources online.

- 自动识别 `- {xxx}`。
- 当笔记文件中包含`- {paper_id}`时候，会下载该文献的信息，不下载PDF。
- 当笔记文件中包含`- {{paper_id}}`时候，会下载该文献的信息，以及PDF。

注意：paper_id支持`文章标题`，已发表文章的`doi`, 预发布文章的`arvix_id`, `biorvix_id`, `medrvix_id`。EasyLiterature会从多个数据库自动识别需要收集和下载的论文，几乎覆盖所有目前存在的论文。


## Usage（使用）
### Basic Usage（基本使用）
Assuming `input` is the folder path of the literature notes (.md files) and `output` is the folder path where you want to save the PDFs.

假设`input`为文献笔记(md文件)的文件夹路径，`output`为要保存PDF的文件夹路径。

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

当要移动文献笔记或者PDF文件夹的时候，文献笔记中的PDF链接可能会变的无法使用。可以使用`-m`来重新关联PDF文件和文献笔记。

```bash
# Update all md files in the input folder
easyliter -i input -m movedPDFs/

# Only update the input/example.md file
easyliter -i input/example.md -m movedPDFs/  
```

### Note (注意事项)
For users from China mainland, the Google scholar feature may need a VPN to get it work (the citation function is based on the Google Scholar). If you don't have a VPN, some features may be lost.

对于来自中国大陆的用户，Google Scholar相关功能可能需要 VPN 才能正常工作（引用功能基于 Google scholar）。如果没有挂VPN，某些功能可能会丢失，但不完全影响使用。

