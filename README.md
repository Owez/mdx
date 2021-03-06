# mdx

Seemless markdown to docx converter

## Example

Command-line:

```shell
$ mdx hippo.md hippo.docx
```

In Python:

```python
from mdx import Document

doc = Document("Markdown here!")
doc.save("example.docx")
```

## Installation

Coming soon!

## Showcase

Coming soon!

## Roadmap

Here are the upcoming features for the development of mdx:

- Last of basics:
  - [x] Hyperlinks
  - [ ] Heading links
  - [x] Images
  - [ ] Tables
  - [ ] Document for first public release
- Quality-of-life
  - [x] Automatically remove Markdown TOCs
  - [x] Good references/bibiolography styling (no-spaced, newline-aware)
  - [ ] Support `#` titles as well as the current yml titles
- Extras:
  - [ ] Local URIs become automatic managed appendixes

This project isn't stable as not all basic markdown has been implemented. The hope for this project is to be able to seamlessly convert all well-formatted markdown to a docx.
