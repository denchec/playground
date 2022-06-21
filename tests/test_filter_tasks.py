import pytest
import playground.__main__ as filter_file


@pytest.mark.parametrize(("iterable", "sub_str", "expected_result"), [
    ([], "abc\n", []),
    (["abc\n", "def\n", "gahi"], "a", ["def\n"])
])
def test_str_filter(iterable, sub_str, expected_result):
    assert list(filter_file.str_filter(sub_str, iterable)) == expected_result


@pytest.mark.parametrize(("iterable", "sub_str", "expected_result"), [
    (["abc\n", 137, "def\n", "gahi", 9], "a", ["def\n"]),
])
def test_for_fail_str_filter(iterable, sub_str, expected_result):
    with pytest.raises(TypeError):
        assert list(filter_file.str_filter(sub_str, iterable)) == expected_result
