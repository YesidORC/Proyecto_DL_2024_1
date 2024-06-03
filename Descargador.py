import os
import requests

def ensure_download_folder_exists(folder: str):
    if not os.path.exists(folder):
        os.makedirs(folder)

def read_urls_from_file(file_path: str):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    return urls

def download_file(url: str, folder: str):
    local_filename = os.path.join(folder, url.split('/')[-1])
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    print(f"Downloaded {url} to {local_filename}")

def main(url_file: str, download_folder: str):
    ensure_download_folder_exists(download_folder)
    urls = read_urls_from_file(url_file)
    for url in urls:
        download_file(url, download_folder)

# Uso del script
if __name__ == "__main__":
    url_file = 'links.txt'  # Nombre del archivo que contiene las URLs
    download_folder = 'EST202'  # Carpeta donde se descargarán los archivos

    main(url_file, download_folder)
