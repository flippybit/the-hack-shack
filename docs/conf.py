html_theme = "pydata_sphinx_theme"
master_doc = 'index'

extensions = ['myst_parser']
html_sidebars = {
    "**": ["sidebar-nav-bs", "sidebar-ethical-ads"]
}

html_theme_options = {
  "show_nav_level": 0
}