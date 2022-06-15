import sys


def str_filter(sub_str, text):
    split_text = text.split("\n")
    end_text = []

    for i in split_text:
        if sub_str not in i:
            end_text.append(i)

    return "\n".join(end_text)


def main():
    arguments = sys.argv
    file = open(arguments[3], "r", encoding='utf-8')
    file = file.read()
    if arguments[1] == "filter":
        print(str_filter(arguments[2], file))


if __name__ == "__main__":
    main()
