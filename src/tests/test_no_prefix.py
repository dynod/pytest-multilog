from pytest_multilog import TestHelper


class TestNoPrefix(TestHelper):
    @property
    def filter_test_prefixes(self) -> bool:
        # Don't filter "test_" and "Test" prefixes
        return False

    def test_simple(self):
        # Just some basic tests
        assert self.test_folder == self.output_folder / "__running__" / self.worker / "test_no_prefix_TestNoPrefix_test_simple"
        assert self.test_final_folder == self.output_folder / "test_no_prefix" / "TestNoPrefix" / "test_simple"
        assert self.test_name == "test_no_prefix/TestNoPrefix/test_simple"
