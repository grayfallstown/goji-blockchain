import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("GOJI_ROOT", "~/.goji-blockchain/mainnet"))).resolve()
