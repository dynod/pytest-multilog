# Test for Test Helper
from pathlib import Path

from pytest_multilog import TestHelper


class TestTheHelper(TestHelper):
    def test_simple(self):
        # Just some basic tests
        assert self.worker == "gw0"
        assert self.worker_index == 0
        assert self.root_folder == Path(__file__).parent.parent.parent
        assert self.output_folder == self.root_folder / "out" / "tests"
        assert self.test_folder == self.output_folder / "__running__" / "gw0" / "test_simple_TestTheHelper_test_simple"
        assert self.test_logs.exists()
        self.check_logs("New test: test_simple_TestTheHelper_test_simple")
        self.check_logs(["helper.py", "TestTheHelper"])
