import gevent.monkey
gevent.monkey.patch_all()

import server
from config import ProductionConfig

app, socketio = server.init_app(ProductionConfig)


if __name__ == "__main__":
    with app.app_context():
        socketio.run(
            host=app.config["BACKEND_SERVER_HOST"],
            port=app.config["BACKEND_SERVER_PORT"],
        )
