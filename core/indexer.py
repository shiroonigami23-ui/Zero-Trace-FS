import json
import os
import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class PhantomIndexer:
    def __init__(self, key):
        self.aesgcm = AESGCM(key)
        self.index = {}

    def hide_file(self, vault_path, filename, data):
        with open(vault_path, "r+b") as f:
            start_offset = secrets.randbelow(8 * 1024 * 1024)
            nonce = os.urandom(12)
            encrypted_data = self.aesgcm.encrypt(nonce, data, None)
            f.seek(start_offset)
            f.write(encrypted_data)
            self.index[filename] = {"offset": start_offset, "size": len(encrypted_data), "nonce": nonce.hex()}

    def export_index(self, path="index.oni"):
        with open(path, "w") as f:
            json.dump(self.index, f)
