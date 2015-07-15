class Element(object):

    def __init__(self, name="", content=""):
        self.name = name
        self.content = content

    def append(self, new_text):
        self.content += new_text

    def render(self, file_name, ind=""):

        indent = ind
        indent += self.content
        file_name.write(indent)


class Html(Element):

    def __init__(self, name="", content=""):
        self.name = name
        self.content = "<!DOCTYPE html>\n"
        self.content += "<html>\n"
        self.content += content

    def render(self, file_name, ind=""):
        ind += self.content
        ind += "</html>\n"
        file_name.write(ind)


class Body(Element):

    def __init__(self, content="", name=""):
        self.name = name
        indented_content = add_indent(content)
        self.content = "<body>\n{}\n<\\body>\n".format(indented_content)

    def __str__(self):
        return self.content


class P(Element):

    def __init__(self, content="", name=""):
        self.name = name
        indented_content = add_indent(content)
        self.content = "<p>\n{}\n<\p>\n".format(indented_content)

    def __str__(self):
        return self.content


def add_indent(content):

    # Adds four blank spaces infront of every line of a given string
    lines = content.split("\n")
    ind_lines = []
    for line in lines:
        ind_lines.append("    " + line)
    return "".join(ind_lines)
    
