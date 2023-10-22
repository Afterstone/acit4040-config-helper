import os
import tempfile
from pathlib import Path

import acit4040_config_helper as ach


def test_get_envvar_str__can_get_str():
    if os.getenv("ACH_TEST_STR") is not None:
        raise RuntimeError("ACH_TEST_STR is already set")

    try:
        os.environ["ACH_TEST_STR"] = "test"
        assert ach.get_envvar_str("ACH_TEST_STR") == "test"
    finally:
        del os.environ["ACH_TEST_STR"]


def test_get_envvar_int__can_get_int():
    if os.getenv("ACH_TEST_INT") is not None:
        raise RuntimeError("ACH_TEST_INT is already set")

    try:
        os.environ["ACH_TEST_INT"] = "42"
        assert ach.get_envvar_int("ACH_TEST_INT") == 42
    finally:
        del os.environ["ACH_TEST_INT"]


def test_get_envvar_path__can_get_path():
    if os.getenv("ACH_TEST_PATH") is not None:
        raise RuntimeError("ACH_TEST_PATH is already set")

    try:
        if os.name == "nt":
            f_name = os.environ["ACH_TEST_PATH"] = "C:\\tmp"
        elif os.name == "posix":
            f_name = os.environ["ACH_TEST_PATH"] = "/tmp"
        else:
            raise RuntimeError("Unknown OS")

        path = ach.get_envvar_path("ACH_TEST_PATH", check_exists=False).absolute()
        assert str(path) == f_name
    finally:
        del os.environ["ACH_TEST_PATH"]


def test_get_envvar_path__can_get_path__with_check_exists():
    with tempfile.NamedTemporaryFile() as f:
        if os.getenv("ACH_TEST_PATH") is not None:
            raise RuntimeError("ACH_TEST_PATH is already set")

        try:
            f.write(b"test")
            f_name = str(f.name)
            os.environ["ACH_TEST_PATH"] = f_name
            path = ach.get_envvar_path("ACH_TEST_PATH", check_exists=True).absolute()
            assert str(path) == f_name
        finally:
            del os.environ["ACH_TEST_PATH"]


def test_get_secret__fallback_works():
    if os.getenv("ACH_TEST_SECRET") is not None:
        raise RuntimeError("ACH_TEST_SECRET is already set")

    try:
        secret = os.environ["ACH_TEST_SECRET"] = "test"
        value = ach.get_secret(
            "ACH_TEST_SECRET_NOT_SET", fallback_env_var_name="ACH_TEST_SECRET"
        )
        assert value == secret
    finally:
        del os.environ["ACH_TEST_SECRET"]


def test_get_secret_file__fallback_works():
    if os.getenv("ACH_TEST_SECRET_FILE") is not None:
        raise RuntimeError("ACH_TEST_SECRET_FILE is already set")

    with tempfile.NamedTemporaryFile() as f:
        try:
            ref_path = os.environ["ACH_TEST_SECRET_FILE"] = str(f.name)
            path = ach.get_secret_file(
                "ACH_TEST_SECRET_FILE_NOT_SET",
                output_file=Path("doesnt_exist"),
                fallback_env_var_name="ACH_TEST_SECRET_FILE",
            )

            assert ref_path == str(path.absolute())
        finally:
            del os.environ["ACH_TEST_SECRET_FILE"]
