
class Element:
    """Renders basic HTML elements by tag."""

    indent = 4
    tag = ""

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content is not None:
            self.content.append(content)
        self.kwargs = kwargs

    def append(self, content):
        self.content.append(content)

    def render(self, f, ind=" "):
        start_tag = ("\n{:>}<{}".format((ind * self.indent), self.tag))
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(">\n")
        else:
            f.write(start_tag + ">\n")
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write("{:>}    {}".format((ind * self.indent), (str(element))))
        end_tag = "\n{}</{}>".format((ind * self.indent), self.tag)
        f.write(end_tag)


class Body(Element):
    """Renders body (<body>) element."""

    tag = "body"


class Head(Element):
    """Renders head (<head>) element. This is NOT for text headers. 
    This is a container for all the head elements."""

    tag = "head"


class Html(Element):
    """Renders the document type and html (<html>) elements."""

    indent = 0
    tag = "html"

    def __init__(self, content=None, document_type="html"):
        Element.__init__(self, content=None)
        self.document_type = document_type
        self.content = []
        if content is not None:
            self.content.append(content)

    def render(self, f, ind=" "):
        start_tag = '<!DOCTYPE {}>\n<{}>'.format(self.document_type, self.tag)
        f.write(start_tag)
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write((ind * self.indent) + str(element))
        end_tag = "\n</{}>".format(self.tag)
        f.write(end_tag)


class Link(Element):
    """Renders link (anchors) element."""

    indent = 0
    tag = "a"

    def __init__(self, link=None, content=None, **kwargs):
        Element.__init__(self, content=None)
        self.link = link
        self.content = []
        if content is not None:
            self.content.append(content)
        self.kwargs = kwargs

    def render(self, f, ind=" "):
        start_tag = '<{} href="{}"'.format(self.tag, self.link)
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(">")
        else:
            f.write(start_tag + ">")
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write(str(element))
        end_tag = "</{}>".format(self.tag)
        f.write(end_tag)


class ListItem(Element):
    """Renders list item (<li>) element."""

    indent = 12
    tag = "li"


class Paragraph(Element):
    """Renders paragraph (<p>) element."""

    indent = 8
    tag = "p"


class UnordList(Element):
    """Renders unordered list (<ul>) element."""

    indent = 8
    tag = "ul"


class OneLineTag(Element):
    """For tags that should always render on a single line."""

    def render(self, f, ind=" "):
        start_tag = ("\n{}<{}".format((ind * self.indent), self.tag))
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(">")
        else:
            f.write(start_tag + ">")
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write(str(element))
        end_tag = '</{}>'.format(self.tag)
        f.write(end_tag)


class Header(OneLineTag):
    """Renders header (<hn>) element, where n is the header level."""

    indent = 8
    tag = "h"

    def __init__(self, level=None, content=None, **kwargs):
        OneLineTag.__init__(self, content=None)
        self.level = level
        self.content = []
        if content is not None:
            self.content.append(content)
        self.kwargs = kwargs

    def render(self, f, ind=" "):
        start_tag = '{}<{}{:d}'.format(
            (ind * self.indent), self.tag, self.level)
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(">")
        else:
            f.write(start_tag + ">")
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write(str(element))
        end_tag = '</{}{:d}>'.format(self.tag, self.level)
        f.write(end_tag)


class Title(OneLineTag):
    """Renders page title (<title>) element."""

    indent = 8
    tag = "title"


class SelfClosingTag(Element):
    """Renders html elements that do not take a closing tag."""

    indent = 8

    def render(self, f, ind=" "):
        start_tag = ("\n{}<{}".format((ind * self.indent), self.tag))
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(" />")
        else:
            f.write(start_tag + " />")


class HRule(SelfClosingTag):
    """Renders horizontal rule (<hr />) element."""

    tag = "hr"


class LineBreak(SelfClosingTag):
    """Renders line break (<br />) element."""

    tag = "br"


class Meta(SelfClosingTag):
    """Renders meta (<meta>) element."""

    tag = "meta"

    def __init__(self, content=None, charset="UTF-8", **kwargs):
        SelfClosingTag.__init__(self, content=None)
        self.charset = charset
        self.content = []
        if content is not None:
            self.content.append(content)
        self.kwargs = kwargs

    def render(self, f, ind=" "):
        start_tag = '{}<{} charset="{}"'.format((ind * self.indent), self.tag, self.charset)
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(" />")
        else:
            f.write(start_tag + " />")
