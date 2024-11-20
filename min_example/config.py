from sqlmesh.core.config.format import FormatConfig
from sqlmesh.core.config.model import ModelDefaultsConfig
from sqlmesh.core.config.root import Config

config = Config(
    model_defaults=ModelDefaultsConfig(
        dialect="bigquery",
    ),
    format=FormatConfig(
        normalize_functions="upper",
    ),
)
