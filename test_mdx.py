from mdx import Document

md = """
# Introduction

This is a small testing document to make sure that my module works. Here's a quote from the author:

> This is a quote which should have the same formatting as the line above.

This sentence was written on the 3rd of June, 2022 and hasn't yet been modified. That's all I have to say about that. The next sections are taken and lightly modified from the documentation website I used to create this module, have fun!

Make sure you do have these though:

- Bullet point should work
- List points don't work yet

# Working with Styles

This page uses concepts developed in the prior page without introduction. If a term is unfamiliar, consult the prior page Understanding Styles for a definition.

## Access a Style

Styles are accessed using the Document.styles attribute:

```python
>>> document = Document()
>>> styles = document.styles
>>> styles
<docx.styles.styles.Styles object at 0x10a7c4f50>
```

The Styles object provides dictionary-style access to defined styles by name:

```python
>>> styles['Normal']
<docx.styles.style._ParagraphStyle object at <0x10a7c4f6b>
```

The Styles object is also iterable. By using the identification properties on BaseStyle, various subsets of the defined styles can be generated. For example, this code will produce a list of the defined paragraph styles:

```python
>>> from docx.enum.style import WD_STYLE_TYPE
>>> styles = document.styles
>>> paragraph_styles = [
...     s for s in styles if s.type == WD_STYLE_TYPE.PARAGRAPH
... ]
>>> for style in paragraph_styles:
...     print(style.name)
...
Normal
Body Text
List Bullet
```

## Apply a Style

The Paragraph, Run, and Table objects each have a style attribute. Assigning a style object to this attribute applies that style:

```python
>>> document = Document()
>>> paragraph = document.add_paragraph()
>>> paragraph.style
<docx.styles.style._ParagraphStyle object at <0x11a7c4c50>
>>> paragraph.style.name
'Normal'
>>> paragraph.style = document.styles['Heading 1']
>>> paragraph.style.name
'Heading 1'
```

A style name can also be assigned directly, in which case python-docx will do the lookup for you:

```python
>>> paragraph.style = 'List Bullet'
>>> paragraph.style
<docx.styles.style._ParagraphStyle object at <0x10a7c4f84>
>>> paragraph.style.name
'List Bullet'
```

A style can also be applied at creation time using either the style object or its name:

```python
>>> paragraph = document.add_paragraph(style='Body Text')
>>> paragraph.style.name
'Body Text'
>>> body_text_style = document.styles['Body Text']
>>> paragraph = document.add_paragraph(style=body_text_style)
>>> paragraph.style.name
'Body Text'
```
"""

doc = Document(md)
doc.title = "Hello, World!"
doc.subtitle = "Example Document"
doc.save("test.docx")
