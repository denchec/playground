import pytest
import playground.__main__ as filter_file


@pytest.mark.parametrize(("file_name", "sub_str", "assert_equal"), [
    ("src/playground/test.txt", "я", "Здравствуйте!\n"),
])
def test_str_filter(file_name, sub_str, assert_equal):
    with open(file_name, "r", encoding='utf-8') as file:
        assert "".join(list(filter_file.str_filter(sub_str, file))) == assert_equal
