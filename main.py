# main.py
def define_env(env):
    @env.macro
    def download_pdf(file_date, file_name, label="Download"):
        url = f'https://files.diniscruz.ai/github/pdf/{file_date}/{file_name}'
        return f'[:fontawesome-solid-file-pdf: {label}]({url}){{ .md-button .md-button--primary .md-button--small .no-print}}'

    @env.macro
    def download_wav(file_date, file_name, label="Listen Audio"):
        url = f'https://files.diniscruz.ai/s3/wav/{file_date}/{file_name}'
        return f'[:fontawesome-solid-headphones: {label}]({url}){{ .md-button .md-button--primary .md-button--small .no-print}}'
