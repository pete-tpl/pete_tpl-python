#!/usr/bin/python

import platform
import requests

from pete_tpl import dll


LIBPETETPL_VERSION = 'v0.1.0'
SUPPORTED_TARGETS = ['linux-x86_64']

OS_ARCHITECTURE = platform.machine().lower()


def download_shared_lib():
    print("[PETETPL] Downloading the Petetpl shared lib...")
    target = f'{dll.OS_NAME}-{OS_ARCHITECTURE}'
    if target not in SUPPORTED_TARGETS:
        raise Exception(f"Target is '{target}' not supported")

    url = f"https://github.com/pete-tpl/libpetetpl/releases/download/" \
          f"{LIBPETETPL_VERSION}/libpetetpl-{target}.so"
    r = requests.get(url, allow_redirects=True)
    if r.status_code != 200:
        raise Exception(f'Failed to download a library: {url}\n'
                        f'HTTP status: {r.status_code}')
    with open(dll.PETETPL_SHARED_LIB_PATH, 'wb') as f:
        f.write(r.content)
    print("[PETETPL] Downloading complete")


download_shared_lib()
