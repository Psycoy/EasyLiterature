# EasyLiterature
**EasyLiterature** is a Python-based command line tool for automatic literature management. Welcome star or contribute!

Simply list the paper titles (or ids) you want to read in a markdown file and it will automatically `collect and refine its information in the markdown file`, `download the pdf to your local machine`, and `link the pdf to your paper in the markdown file`. You can forever keep your notes within the pdfs and mds on your local machine or cloud driver.

<br>

**A demo of the entries in your markdown note:**

<img src="figures/demo.png" alt="demo" style="zoom:90%;" />

<br>

Inspired by [Mu Li](https://www.bilibili.com/video/BV1nA41157y4), adapted from [autoLiterature](https://github.com/wilmerwang/autoLiterature). 
Compared to autoLiterature, **EasyLiterature** is much easier to use and supports a wider range of features, such as `title-based paper match`, `paper search and download on Google Scholar and DBLP` (the two main sites for scholars), `citation statistics`, `mannual information update assitant`, etc. **EasyLiterature covers almost all papers thanks to the support of Google Scholar and DBLP!**

___

**中文版介绍：**

**EasyLiterature** 是一个基于python的命令行文件管理工具，永久开源，欢迎star或contribute。

之前沐神（李沐）做过一期视频讲如何阅读文献和整理，我觉得讲得非常好，[链接](https://www.bilibili.com/video/BV1nA41157y4)。EasyLiterature基本基于沐神所述的这一流程实现，并丰富了其他功能。

简单来说，在 Markdown 文件中简单列出想要阅读的论文标题（或ID），它会自动收集并在Markdown文件中完善相关信息，下载论文的PDF到本地机器，并将PDF链接到Markdown文件中的论文。通过这样的流程，我们可以实现永久保存实时编辑的论文PDF和Markdown中的笔记，无论是在本地机器还是云端，并且方便论文一站式分类和管理。

<br>

**markdown文件中的论文信息条目（示意）:**

<img src="figures/demo.png" alt="demo" style="zoom:90%;" />

<br>

与之前的实现相比，EasyLiterature兼容之前实现的所有功能，并且支持更多功能，比如：1. 基于标题的论文匹配；2. Google Scholar和DBLP（全球两大主要paper数据库）的论文搜索和下载；3. 引用统计；4. 手动信息更新助手；5. 容错搜索匹配；等等。之前的实现由于数据库的限制，很多文章都找不到。**EasyLiterature得益于增加了Google Scholar和DBLP的支持，几乎覆盖了所有论文!**

<br><br>

## 1. A Simple Usage Example (一个简单的使用示例)
1. Have the python installed on your local machine (preferably >= 3.7).
2. Run `pip install easyliter` in your command line to install.
3. Prepare your markdown note file (e.g., `Note.md`). <br>**Attention:** You may need to download a markdown editor to create/edit this file. I am using [Typora](https://typora.io/), which is not totally free. You can also choose other alternatives.
4. List the formated papers titles in your markdown note file according to the Section 4 below (Recognition Rules). e.g.,<br>
  \- {{BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.}}<br>
  \- {{Xlnet: Generalized autoregressive pretraining for language understanding.}}<br>
  **(pay attention to the space after ‘\-’)** 
5. Create a folder to store the downloaded pdfs (e.g., `PDFs/`).
6. Run `easyliter -i <path to your md file> -o <path to your pdf folder>`. 
<br> (Replace `<path to your md file>` with the actual path to your markdown note file, `<path to your pdf folder>` with the actual path to your pdf folder)
<br>e.g., `easyliter -i "/home/Note.md" -o "/home/PDFs"`
7. Your should able to see that the updated information and downloaded pdf files if no error is reported.
8. This is a simple and common use case. For other features, please read the below sections carefully and follow the instructions.

<br>

**中文版示例**

1. 在您的本地机器上安装 Python（版本 >= 3.7）。
2. 在命令行中运行 `pip install easyliter` 进行安装。
3. 准备您的 markdown 笔记文件（例如，`Note.md`）。<br>**注意**： 您需要下载一个 markdown 编辑器来创建/编辑此文件。我使用的是[Typora](https://typora.io/)，它不是完全免费的。您也可以选择其他替代产品。
4. 根据下面第4节（识别规则）在您的 markdown 笔记文件中列出格式化的论文标题。例如：<br>
\- {{BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.}}<br>
  \- {{Xlnet: Generalized autoregressive pretraining for language understanding.}}<br>
  **(注意‘\-’后的空格)** 
5. 创建一个文件夹来存储下载的 pdf 文件（例如，`PDFs/`）。
6. 运行 `easyliter -i <您的 md 文件路径> -o <您的 pdf 文件夹路径>`。
<br>**注意**：将 `<您的 md 文件路径>` 替换为您 markdown 笔记文件的实际路径，将 `<您的 pdf 文件夹路径>` 替换为您 pdf 文件夹的实际路径。
<br>例如：`easyliter -i "/home/Note.md" -o "/home/PDFs"`
7. 如果没有报错，您应该能够看到更新的信息和下载的 pdf 文件。
8. 这是一个简单、常用的使用案例。有关其他功能或使用情形，请仔细阅读以下部分并按照说明操作。

## 2. Install (安装)
### pip install
```bash 
pip install easyliter
or
pip3 install easyliter
```

### install from source（to get the up-to-date version）
```bash
git clone https://github.com/Psycoy/EasyLiterature.git
cd EasyLiterature
pip install -e .
```

## 3. Arguments（使用参数）
```bash
easyliter

optional arguments:

  -h, --help            show this help message and exit
  
  -i INPUT, --input INPUT
  The path to the note file or note file folder.

  -o OUTPUT, --output OUTPUT
  Folder path to save paper pdfs and images. NOTE: MUST BE FOLDER.

  -p PROXY, --proxy PROXY
  The proxy. e.g. 127.0.0.1:1080. If this argument is specified, the google scholar will automatically use a free proxy (not necessarily using the specified proxy address). To use other proxies for google scholar, specify the -gp option. If you want to set up the proxies mannually, change the behaviour in GoogleScholar.set_proxy(). See more at https://scholarly.readthedocs.io/en/stable/ProxyGenerator.html.

  -gp GPROXY_MODE, --gproxy_mode GPROXY_MODE
  The proxy type used for scholarly. e.g., free, single, Scraper. (Note: 1. <free> will automatically choose a free proxy address to use, which is free, but may not be fast. 2. <single> will use the proxy address you specify. 3. <Scraper> is not free to use and need to buy the api key.).

  -d, --delete
  Delete unreferenced attachments in notes. Use with caution, when used, -i must be a folder path including all notes.

  -m MIGRATION, --migration MIGRATION
  The pdf folder path you want to reconnect to.
```


## 4. Recognition Rules (识别规则)：
- If the notes file contains `- {paper_id}`, it will download the information of that literature, but not the PDF.
- If the notes file contains `- {{paper_id}}`, it will download both the information of that literature and the PDF.

- Note: `paper_id` supports `article title`, published articles' `doi`, and pre-published articles' `arvix_id`, `biorvix_id`, and `medrvix_id`. It will try all the possible sources online.

___

- 当笔记文件中包含 `- {paper_id}`时候，会下载该文献的信息，不下载PDF。
- 当笔记文件中包含 `- {{paper_id}}`时候，会下载该文献的信息，以及PDF。

- 注意：`paper_id` 支持`文章标题`，已发表文章的`doi`, 预发布文章的`arvix_id`, `biorvix_id`, `medrvix_id`。EasyLiterature会从多个数据库自动识别需要收集和下载的论文，几乎覆盖所有目前存在的论文。


## 5. Usage（使用）
### 5.1. Basic Usage（基本使用）
Assuming `input` is the folder path of the literature notes (.md files) and `output` is the folder path where you want to save the PDFs.

假设`input`为文献笔记(md文件)的文件夹路径，`output`为要保存PDF的文件夹路径。

```bash
# Update all md files in the input folder
# 更新input文件夹下所有md文件
easyliter -i input -o output 

# Only update the input/example.md file
# 仅更新input/example.md文件
easyliter -i input/example.md -o output  

# -d is an optional flag, when -i is a folder path, using -d will delete unrelated pdf files in the PDF folder from the literature notes content
# -d 是个可选项，当 -i 是文件夹路径时候，使用 -d 会删除PDF文件夹下和文献笔记内容无关的pdf文件
easyliter -i input -o output -d
```

### 5.2. Migrating Notes and PDF Files（笔记和pdf文件的迁移）
When you need to move the literature notes or the PDF folder, the links to the PDFs in the literature notes might become unusable. You can use `-m` to re-link the PDF files with the literature notes.

当要移动文献笔记或者PDF文件夹的时候，文献笔记中的PDF链接可能会变的无法使用。可以使用`-m`来重新关联PDF文件和文献笔记。

```bash
# Update all md files in the input folder
# 更新input文件夹下所有md文件
easyliter -i input -m movedPDFs/

# Only update the input/example.md file
# 仅更新input/example.md文件
easyliter -i input/example.md -m movedPDFs/  
```

## 6. Note (注意事项)

1. For users from China mainland, the Google Scholar feature may need a VPN to get it work (the citation function is based on the Google Scholar). If you don't have a VPN, some features may be lost.

  - 对于来自中国大陆的用户，Google Scholar相关功能可能需要 VPN 才能正常工作（引用功能基于 Google scholar）。如果没有挂VPN，某些功能可能会丢失，但不完全影响使用。

2. If your Google Scholar is not working (usually caused by too frequent requests of the Google Scholar API), try to set a proxy for it. Check out the help for `-p` and `-gp` options using `easyliter -h`. See more at the 'Using proxies' section of https://scholarly.readthedocs.io/en/stable/quickstart.html.

  - 如果Google Scholar 无法使用（通常由于对Google Scholar API的访问过于频繁），尝试为其设置代理。使用 easyliter -h 查看 -p 和 -gp 选项的帮助信息来设置代理。详见 https://scholarly.readthedocs.io/en/stable/quickstart.html 的 Using proxies部分。
