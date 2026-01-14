
# Zero-Trace FS (Phantom Vault)

This repository contains the core components of the Zero-Trace File System, a system designed for secure data storage with an emphasis on leaving minimal forensic traces.

## Project Overview

The Zero-Trace FS aims to provide a secure vault where data is encrypted and stored in a way that appears as random noise, making it difficult for an adversary to detect the presence of encrypted data.

## Initial Setup

The `vault.bin` file is initialized as a block of random data. A master key is derived from a password using PBKDF2HMAC.

### Key Features (Planned)

- **Phantom Vault:** Data appears as random noise.
- **Strong Encryption:** Using AESGCM for authenticated encryption.
- **Key Derivation:** Secure password-based key derivation.
- **Block-level Operations:** Managing data in fixed-size blocks.

## Development Status

This is an initial commit, setting up the basic structure and key derivation components.

## Local Setup (Colab Environment)

To run this project in Google Colab:

1. Clone this repository.
2. Run the provided Python cells to initialize the vault and generate a master key.

```python
# Example: Initialize the vault
# ztfs = ZeroTraceEngine()
# ztfs.initialize_vault(size_mb=10)
# master_password = "YourStrongPasswordHere"
# key, salt = ztfs.generate_master_key(master_password)
```

## Contributing

Contributions are welcome! Please feel free to open issues or pull requests.


## Changelog

See the [CHANGELOG](CHANGELOG.md) for a history of changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
