from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True) # we call vari inside this without any func call
class DataIngestionConfig: #all this from config.yaml
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
