from db_methods.db_methods import Query


def main():
    suppliers = Query().get_client_info()
    print('\nHello\n')

    for data in suppliers:
        print(data['name'])


if __name__ == '__main__':
    main()
