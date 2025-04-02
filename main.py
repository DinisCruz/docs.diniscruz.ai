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


    @env.macro
    def show_spotify_ui(spotify_id):
        return f'''
## Podcast
<iframe src="https://open.spotify.com/embed/episode/{spotify_id}?utm_source=generator"
        width="100%" height="152" frameborder="0"
        allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
        loading="lazy"></iframe>
'''

    @env.macro
    def show_infographic(file_date, file_name):
        url = f'https://files.diniscruz.ai/s3/pdf/{file_date}/infographic__{file_name}'
        return f'''
## Infographic    
<iframe src="{url}"
        width="100%" height="512px" style="border: none;"></iframe>
'''