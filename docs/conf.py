# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'prismdata'
copyright = '2024, Saswata Nandi'
author = 'Saswata Nandi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "autoapi.extension",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# html title
html_title = "PRISMDATA"

# Output file base name for HTML help builder.
htmlhelp_basename = 'prismdatadoc'

source_suffix = ['.rst', '.md']

# auto-api settings
autoapi_template_dir = "_templates/autoapi"
autoapi_type = 'python'
autoapi_dirs = ['../src/prismdata']
# autoapi_options = ['undoc-members'] #['members', 'undoc-members', 'show-inheritance', 'show-module-summary', 'special-members', 'imported-members']
# autoapi_python_class_content = 'both'
# autoapi_member_order = 'bysource'
# autoapi_add_toctree_entry = False
# autodoc_typehints = "signature" # signature, description, both, none 
autoapi_keep_files = True
autoapi_ignore = ["*/__about__.py"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
