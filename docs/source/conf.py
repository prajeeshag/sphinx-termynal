project = "sphinx-termynal"
copyright = "2024, Prajeesh Ag"
author = "Prajeesh Ag"
# release = "0.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_termynal",
    "myst_parser",
    "sphinx_design",
]


templates_path = ["_templates"]
exclude_patterns = []


html_theme = "sphinx_book_theme"
# html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/prajeeshag/sphinx-termynal",
    "use_repository_button": True,
}

html_title = "Sphinx Termynal"

myst_enable_extensions = ["colon_fence"]
