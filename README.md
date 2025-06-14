# MkDocs Testing

Repository to test if MkDocs meets the DCC-EX team's needs for a fresh start on simpler to maintain documentation.

MkDocs is being tested with the Material theme, which is reported to have an excellent search engine and other built-in features that reduce dependency complexity.

## Evaluation requirements

This is the simple working list of requirements to evaluate against:

- Must have at least a basic DCC-EX look/feel colour theme
- Must have useful search capability
- Must target RTR user base primarily
- Must be easy to contribute to for non-developers, nothing more complicated than Markdown syntax
- Must render well on both mobile and web
- Must reduce maintenance/management complexity as much as possible
- Must have DCC-EX News type blog/RSS feed
- Must support internal reference links
- Should enable adding new content without having to faff about with site structure
- Should have a glossary of terms
- Should be easy to preview locally
- Could have an auto generated list of references where glossary terms are in docs
- Could have a selector to change between production and development versions
- Will not have a complicated "language" or other that people need to learn in order to contribute

## MkDocs links

[MkDocs website](https://www.mkdocs.org/)
[MkDocs Material theme](https://squidfunk.github.io/mkdocs-material/)
[MkDocs Awesome Nav plugin](https://lukasgeiter.github.io/mkdocs-awesome-nav/)

## MkDocs requirements

MkDocs does require Python in order to be previewed and built locally, and all testing is being performed with Python 3.13.

Previewing and building locally is recommended to be done in a virtual environment, with requirements installed.

Linux/macOS:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows:

```console
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
