from setuptools import setup

setup(
    name='custom-footer-plugin',
    version='0.1',
    py_modules=['custom_footer_plugin.custom_footer'],
    entry_points={
        'mkdocs.plugins': [
            'custom-footer = custom_footer_plugin.custom_footer:CustomFooterPlugin'
        ]
    },
)
