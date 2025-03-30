# main.py
def define_env(env):
    @env.macro
    def download_pdf(file_date, file_name, label="Download"):
        url = f'https://files.diniscruz.ai/pdfs/{file_date}/{file_name}'
        return f'[:fontawesome-solid-file-pdf: {label}]({url}){{ .md-button .md-button--primary .md-button--small .no-print}}'
