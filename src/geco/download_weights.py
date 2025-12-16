import os
from os.path import exists

from requests import get
from tqdm import tqdm

from geco.paths import WEIGHTS_FILE, WEIGHTS_DOWNLOAD_URL, WEIGHTS_DIR


def download_weights(force_download=False):
    os.makedirs(WEIGHTS_DIR, exist_ok=True)
    if exists(WEIGHTS_FILE) and not force_download:
        print('weights file already exists, skipping download')
        return

    print(f'Downloading weights from {WEIGHTS_DOWNLOAD_URL}...')
    response = get(WEIGHTS_DOWNLOAD_URL, stream=True)
    response.raise_for_status()  # Raise an error for bad status codes

    # Get the total file size from the response headers
    total_size = int(response.headers.get('content-length', 0))

    with open(WEIGHTS_FILE, 'wb') as f, tqdm(
            desc=f"Downloading GeCo weights to: {WEIGHTS_FILE}",
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
    download_weights()
