from severus.app import app
from severus.db import db


def main():
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)


if __name__ == '__main__':
    main()
