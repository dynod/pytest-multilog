from pytest_multilog import TestHelper


class TestTheHelper(TestHelper):
    def test_simple(self):
        # Just some basic tests
        assert self.test_folder == self.output_folder / "__running__" / self.worker / "subtests_fromsubmodule_TheHelper_simple"
        assert self.test_final_folder == self.output_folder / "subtests" / "fromsubmodule" / "TheHelper" / "simple"
        assert self.test_name == "subtests/fromsubmodule/TheHelper/simple"
