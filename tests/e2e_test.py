import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from module_cli import main
from module_cli import MODULE_S


def test_cli_writes_to_stdout_when_no_args_provided():
    args = ("module-cli",)
    completed_process = subprocess.run(args, text=True, capture_output=True)

    assert MODULE_S.strip() == completed_process.stdout.strip()


def test_cli_writes_to_file_when_arg_provided(tmp_path: Path):
    module_path = tmp_path / "t.py"

    assert module_path.read_text().strip() == ""

    args = ("module-cli", str(module_path))
    completed_process = subprocess.run(args, text=True, capture_output=True)

    assert completed_process.stdout == ""
    assert module_path.read_text().strip() == MODULE_S.strip()


def test_no_traceback_shown_if_main_raises_an_exception_and_debug_flag_not_set():
    msg = "An error message ..."
    with patch("module_cli.handler") as mock:
        mock.side_effect = RuntimeError(msg)
        retval = main(())
        assert retval == msg


def test_traceback_is_shown_if_main_raises_an_exception_and_debug_flag_is_set():
    msg = "An error message ..."
    with patch("module_cli.handler") as mock:
        mock.side_effect = RuntimeError(msg)
        with pytest.raises(RuntimeError):
            main(("--debug",))
