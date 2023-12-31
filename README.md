# Acit4040 Config Helper

Config Helper provides multiple ways of getting configuration data from
environment variables and secrets from GCP Secret Manager..

### Environment Variables

As of version 0.1.1, the following methods are supported:
- get_envvar_int(envvar_name: str, default_value: int | None = None) -> int
    - Reads an integer from the environment variable in `envvar_name`.
    - Supports fallback values with `default_value`.
- get_envvar_path(envvar_name: str, check_exists: bool = True) -> Path
    - Reads a path from the environment variable in `envvar_name`.
    - Supports checking if the path exists with `check_exists`.
    - Does not support fallback values.
- get_envvar_str(envvar_name: str, default_value: str | None = None) -> str
  - Reads a string from the environment variable in `envvar_name`.
  - Supports fallback values with `default_value`.

### GCP Secret Manager

As of version 0.1.1, the following methods are supported:
- get_secret(env_var_name: str, fallback_env_var_name: t.Optional[str]) -> str
  - Reads a text secret from GCP Secret Manager.
  - Supports fallback values with `fallback_env_var_name`.
- get_secret_file(env_var_name: str, output_file: Path, fallback_env_var_name: t.Optional[str]) -> Path
  - Reads a binary secret/a file from GCP Secret Manager and writes it to `output_file`.
  - Supports fallback values with `fallback_env_var_name`.
