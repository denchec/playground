import argparse


def parser_func():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    parser_filter = subparsers.add_parser("filter")
    parser_filter.add_argument("sub_str")
    parser_filter.add_argument("file")
    parser_filter.set_defaults(func=filter_main)

    arguments = parser.parse_args()

    return arguments


def filter_main(sub_str, file, **_):
    with open(file, "r", encoding='utf-8') as file:
        for line in str_filter(sub_str, file):
            print(line, end="")


def str_filter(sub_str, iterable):
    for line in iterable:
        if sub_str in line:
            yield line


def main():
    arguments = parser_func()
    arguments.func(**vars(arguments))


if __name__ == "__main__":
    main()
