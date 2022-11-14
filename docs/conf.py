html_theme = "pydata_sphinx_theme"
master_doc = 'index'

extensions = ['myst_parser']


html_theme_options = {
"show_nav_level": 0,
"navbar_start": ["navbar-logo"],
"navbar_center": ["navbar-nav"],
"navbar_end": ["navbar-icon-links"]
}