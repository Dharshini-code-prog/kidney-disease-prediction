from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True) # we call vari inside this without any func call
class DataIngestionConfig: #all this from config.yaml
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


#we use frozen bz if user enter other than these content it'll throw error
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list