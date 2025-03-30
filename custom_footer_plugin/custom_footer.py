from mkdocs.plugins import BasePlugin

class CustomFooterPlugin(BasePlugin):

    def on_config(self, config):
        config['extra']['version'] = self.get_version()
        return config

    def get_version(self):
        with open("version", "r") as version_file:
            return version_file.read().strip()
