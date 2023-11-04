from setuptools import setup, find_packages 

with open('README.md', 'r', encoding='UTF-8') as f:
    README_MD = f.read()

setup(
    name="easyliter",
    version="1.0.5",
    description="EasyLiterature is a opensourced, Python-based command line tool for automatic literature management. Simply list the paper titles (or ids) you want to read in a markdown file and it will automatically collect and refine its information in the markdown file, download the pdf to your local machine, and link the pdf to your paper in the markdown file. You can forever keep your notes within the pdfs and mds on your local machine or cloud driver.",
    long_description=README_MD,
    long_description_content_type='text/markdown',
    url="https://github.com/Psycoy/EasyLiterature",
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Markup",
    ],
    install_requires=["beautifulsoup4>=4.11.1", "feedparser>=6.0.10", 
                      "urllib3>=1.26.11","requests>=2.28.1", 
                      "tqdm>=4.64.0", "Unidecode>=1.3.4", "bibtexparser==1.4.0", "pandas", "scholarly"],
    entry_points={
        "console_scripts": [
            "easyliter = easy_literature.easyliter:main",
        ]
    },
    packages=find_packages(),
    license="AGPLv3",
    author="Oliver",
    author_email="olivernova1998@gmail.com",
    keywords=["title", "bibtex", "arxiv", "doi", "science", "scientific-journals"],
)
