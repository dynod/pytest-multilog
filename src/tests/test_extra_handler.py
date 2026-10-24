import logging

import pytest

from pytest_multilog import TestHelper


class TestTheExtraHandler(TestHelper):
    @pytest.fixture
    def extra_multilog_handlers(self) -> list[logging.Handler]:
        # Add an extra logging handler
        extra_handler = logging.FileHandler(filename=str(self.test_folder / "extra.log"), mode="w", encoding="utf-8", errors="ignore", delay=True)
        extra_handler.setFormatter(logging.Formatter("%(message)s", "%Y-%m-%d %H:%M:%S"))
        return [extra_handler]

    def test_with_extra(self):
        # Add some logs
        logging.info("Log abc")
        logging.info("Log def")

        # Check that the logs are present in both the default and extra log files
        extra_log = self.test_folder / "extra.log"
        assert extra_log.is_file()
        log_lines = extra_log.read_text(encoding="utf-8").splitlines()
        assert "Log abc" in log_lines
        assert "Log def" in log_lines
