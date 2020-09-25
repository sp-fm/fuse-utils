from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="FUSE",
    settings_files=["configs/settings.yaml", "configs/.secrets.yaml"],
    environments=True,
)

# `envvar_prefix` = export envvars with `export FUSE_FOO=bar`.
# `settings_files` = Load this files in the order.
