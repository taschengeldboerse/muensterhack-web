from severus.app import app
from severus.utils import initialize_database


def main():
    initialize_database()
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
