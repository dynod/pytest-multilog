# Test for Test Helper
import logging
import time
from pathlib import Path
from threading import Event, Thread

from pytest_multilog import TestHelper


class TestTheHelper(TestHelper):
    def test_simple(self):
        # Just some basic tests
        assert self.worker.startswith("gw")
        assert self.worker_index >= 0
        assert self.root_folder == Path(__file__).parent.parent.parent
        assert self.output_folder == self.root_folder / "out" / "tests"
        assert self.test_folder == self.output_folder / "__running__" / "gw0" / "test_simple_TestTheHelper_test_simple"
        assert self.test_logs.exists()

    def add_log(self, event: Event):
        event.set()
        time.sleep(1)
        logging.info("Log From Thread !!!")

    def test_checklogs(self):
        # Simple
        self.check_logs("New test: test_simple_TestTheHelper_test_checklogs")
        self.check_logs(["helper.py", "TestTheHelper"])

        # No match
        try:
            self.check_logs("some unknown log")
            raise Exception("Shouldn't get here")
        except AssertionError as e:
            assert "Expected pattern not found in logs" in str(e)

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
