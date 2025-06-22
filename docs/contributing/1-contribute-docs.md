# Contributing to Documentation

This page outlines what you need in order to contribute to the documentation, along with the various markdown attributes and so forth you can use.

The documentation is hosted using GitHub Pages and is written in Markdown format, using MkDocs to publish the content. We use the MkDocs Material theme to give us the framework for the look and feel of the website, along with a number of other useful plugins and extensions to enhance the content.

**Important! Once up and running with the information on this page, please ensure you are familiar with **

## How to Contribute

For contributions from the general public, we recommend forking the [GitHub repository](https://github.com/DCC-EX/dcc-ex.github.io) and submitting pull requests for the DCC-EX Documenter team to review and merge.

If you wish to contribute more fully and become a part of the DCC-EX Documenter team, reach out to us via [Discord](https://discord.gg/y2sB4Fp). To gain access to the [GitHub repository](https://github.com/DCC-EX/dcc-ex.github.io), one of the DCC-EX team administrators will need to add you to the "Web" team in GitHub.

## MkDocs Links

Here are some handy links with more info:

- [MkDocs website](https://www.mkdocs.org/) - The official MkDocs documentation.
- [MkDocs Material theme](https://squidfunk.github.io/mkdocs-material/) - The MkDocs Material theme documentation.
- [MkDocs Awesome Nav plugin](https://lukasgeiter.github.io/mkdocs-awesome-nav/) - MkDocs Awesome Nav plugin is what we use for dynamic page structure.
- [MkDocs RSS Plugin](https://guts.github.io/mkdocs-rss-plugin/) - The MkDocs RSS Plugin publishes our DCC-EX News feed.
- [MkDocs ezglossary Plugin](https://realtimeprojects.github.io/mkdocs-ezglossary/) - The MkDocs ezglossary plugin enables our dynamically generated and linked glossary of terms.

## What You Need to Install

This is the list of software you need to successfully contribute to the documentation, including being able to preview it locally:

- [Visual Studio Code (VSCode)](https://code.visualstudio.com/)
- [Python](https://www.python.org/) - Version 3.13 is recommended, minimum required is 3.10

There are two VSCode plugins that are highly recommended also:

- Markdown Preview Mermaid Support by Matt Bierner - enables previewing Mermaid diagrams in VSCode
- markdownlint by David Anson - helps keep consistent, good formatting in Markdown files (like flake8 for Python)

## Getting Started

Once you have installed VSCode and Python, you need to clone the [GitHub repository](https://github.com/DCC-EX/dcc-ex.github.io), set up a virtual environment, and install the MkDocs requirements.

We recommend using the built-in Git functionality of VSCode to clone the repository, or you can use [GitHub Desktop](https://github.com/apps/desktop) or command line Git, whichever you prefer. There is plenty of information generally available on that so we won't cover it here, and instead will focus on the specifics required to ready to contribute to MkDocs content.

Follow the appropriate section below to setup MkDocs in Python for your operating system:

### Setup on macOS

```bash
cd mkdocs-test
python 3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Setup on Linux

``` bash
cd mkdocs-test
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

### Setup on Windows

```console
cd mkdocs-test
virtualenv venv
venv\scripts\activate
pip install -r requirements.txt
```

## Previewing and building MkDocs

Previewing locally is very simple:

```bash
mkdocs serve
```

Navigate to the local preview in a browser at <http://localhost:8000/mkdocs-test/>.

Building locally is equally as simple:

```bash
mkdocs build
```

MkDocs also has a feature to deploy to GitHub pages without using a workflow:

```bash
mkdocs gh-deploy
```
