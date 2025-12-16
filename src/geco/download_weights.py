import os
from os.path import exists

from requests import get
from tqdm import tqdm

from geco.paths import GECO_WEIGHTS_FILE, GECO_WEIGHTS_DOWNLOAD_URL, WEIGHTS_DIR, SAM_HQ_WEIGHTS_FILE, SAM_HQ_WEIGHTS_DOWNLOAD_URL


def download_weights(download_url, file_location, file_dir=WEIGHTS_DIR, force_download=False):
    os.makedirs(file_dir, exist_ok=True)
    if exists(file_location) and not force_download:
        print('weights file already exists, skipping download')
        return

    file_name = os.path.split(file_location)[-1]
    response = get(download_url, stream=True)
    response.raise_for_status()  # Raise an error for bad status codes

    # Get the total file size from the response headers
    total_size = int(response.headers.get('content-length', 0))

    with open(file_location, 'wb') as f, tqdm(
            desc=f"Downloading {file_name}",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            bar.update(len(chunk))

    print('Download completed successfully.')


if __name__ == '__main__':
    download_weights(SAM_HQ_WEIGHTS_DOWNLOAD_URL, SAM_HQ_WEIGHTS_FILE, WEIGHTS_DIR, force_download=True)
    download_weights(GECO_WEIGHTS_DOWNLOAD_URL, GECO_WEIGHTS_FILE, WEIGHTS_DIR, force_download=True)
