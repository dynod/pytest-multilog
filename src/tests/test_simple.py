# Test for Test Helper
import logging
import re
import time
from pathlib import Path
from threading import Event, Thread

import pytest

from pytest_multilog import TestHelper


class TestTheHelper(TestHelper):
    def test_simple(self):
        # Just some basic tests
        assert self.worker.startswith("gw") or self.worker == "master"
        assert self.worker_index >= 0
        assert self.root_folder == Path(__file__).parent.parent.parent
        assert self.output_folder == self.root_folder / "out" / "tests"
        assert self.test_folder == self.output_folder / "__running__" / self.worker / "simple_TheHelper_simple"
        assert self.test_final_folder == self.output_folder / "simple" / "TheHelper" / "simple"
        assert self.test_name == "simple/TheHelper/simple"
        assert self.test_logs.exists()

    def add_log(self, event: Event):
        event.set()
        time.sleep(1)
        logging.info("Log From Thread !!!")

    def test_checklogs_string(self):
        # Simple
        self.check_logs("New test: simple/TheHelper/checklogs_string")
        self.check_logs(["helper.py", "TheHelper"])

        # No match
        try:
            self.check_logs("some unknown log")
            raise Exception("Shouldn't get here")
        except AssertionError as e:
            assert "Missing patterns: ['some unknown log']" in str(e)

        # With timeout, but first find is OK
        logging.info("new log entry !!!")
        self.check_logs("new log entry !!!", timeout=1)

        # Start logging thread
        event = Event()
        t = Thread(target=self.add_log, kwargs={"event": event})
        t.start()
        event.wait()

        # Wait for log sent by logging thread
        self.check_logs("Log From Thread !!!", timeout=2)
        t.join()

    def test_checklogs_pattern(self):
        # Simple
        self.check_logs(re.compile("New test: simple/[^/ ]+/checklogs_pattern"))

        # No match
        try:
            self.check_logs(re.compile("some *unknown +logs"))
            raise Exception("Shouldn't get here")
        except AssertionError as e:
            assert "Missing patterns: ['some *unknown +logs']" in str(e)

    def test_emoji_logs(self):
        # Add emoji in logs
        logging.info("Some logs with emoji ! -- 💀 --")

        # Verify we can check for it
        self.check_logs("-- 💀 --")

    def test_logs_order(self):
        # Add logs in a given order
        logging.info("first log")
        logging.info("second log")

        # Check in any order
        self.check_logs(["second log", "first log"])

        # Check with required order
        try:
            self.check_logs(["second log", "first log"], check_order=True)
            raise Exception("Shouldn't get here")
        except AssertionError as e:
            assert "Missing patterns: ['first log']" in str(e)

    @pytest.mark.parametrize(["param", "ids"], [[1, "one"], [2, "two?"]])
    def test_path_with_parameterize(self, param: int, ids: str):
        assert param in [1, 2]
        assert ids in ["one", "two?"]


class Test(TestHelper):
    def test_simple(self):
        # Check name with the Class name filtered out (empty part after prefix removal)
        assert self.test_folder == self.output_folder / "__running__" / self.worker / "simple_simple"
        assert self.test_final_folder == self.output_folder / "simple" / "simple"
        assert self.test_name == "simple/simple"
