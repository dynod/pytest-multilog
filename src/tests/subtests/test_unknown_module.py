from pytest_multilog import TestHelper


class TestUnknownModule(TestHelper):
    @property
    def test_module(self) -> str:
        # Unknown test module: only the file name will be used
        return "unknown_module"

    def test_simple(self):
        # Just some basic tests
        assert self.test_folder == self.output_folder / "__running__" / self.worker / "unknown_module_UnknownModule_simple"
        assert self.test_final_folder == self.output_folder / "unknown_module" / "UnknownModule" / "simple"
        assert self.test_name == "unknown_module/UnknownModule/simple"
