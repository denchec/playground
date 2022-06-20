import pytest
import playground.__main__ as filter_file


@pytest.mark.parametrize(("iterable", "sub_str", "expected_result"), [
    (["abc\n", "def\n", "gahi"], "a", ["def\n"]),
    ([], "abc\n", []),
    (["abc\n", "def\n", "ghi"], "abc\ndef\nghi", ["abc\n", "def\n", "ghi"]),
    (["abc\n", "def\n", "ghi"], "", []),
])
def test_str_filter(iterable, sub_str, expected_result):
    assert list(filter_file.str_filter(sub_str, iterable)) == expected_result


@pytest.mark.parametrize(("iterable", "sub_str", "expected_result"), [
    (["abc\n", "def\n", "ghi"], ["abc\n", "ghi"], ["def\n"]),
])
def test_on_fail_str_filter(iterable, sub_str, expected_result):
    with pytest.raises(Exception):
        assert list(filter_file.str_filter(sub_str, iterable)) == expected_result
