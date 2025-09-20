from pytest_multilog import TestHelper


class TestWithoutFileName(TestHelper):
    @property
    def test_module(self) -> str:
        # Use empty prefix to only keep test class and method names
        return ""

    def test_simple(self):
        # Just some basic tests
        assert self.test_folder == self.output_folder / "__running__" / self.worker / "WithoutFileName_simple"
        assert self.test_final_folder == self.output_folder / "WithoutFileName" / "simple"
        assert self.test_name == "WithoutFileName/simple"
