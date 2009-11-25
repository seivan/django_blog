import pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import re


def embed_syntax(match):
    code_string = match.group("code")
    try:
        lexer = get_lexer_by_name(match.group("language"), stripall=True)
    except ValueError:
        lexer = pygments.lexers.PythonLexer()
    return "<p>%s</p>" % (pygments.highlight(code_string, lexer, pygments.formatters.HtmlFormatter(linenos=True)))
