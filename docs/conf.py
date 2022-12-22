html_theme = "furo"
html_title = "the-hack-shack"
master_doc = 'index'
html_logo = "imgs/shack.jpeg"

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # External stuff
    "myst_parser",
    "sphinx_design",
    "sphinx_inline_tabs",
]