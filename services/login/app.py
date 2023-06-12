from dataclasses import dataclass
from typing import Optional
from abc import ABC, abstractmethod
from flask import Flask , request, render_template


class Executor(ABC):

    @abstractmethod
    def execute(self, *args: Optional, **kwargs: Optional) -> None:
        ...


@dataclass
class LoginService(Executor):

    app: Flask = Flask(__name__)
    host: str = '0.0.0.0'
    port: int = 1000

    @staticmethod
    @app.route('/')
    def index() -> render_template:
        return render_template('login.html')

    @staticmethod
    @app.route('/login',methods=['POST'])
    def login() -> str:
        username = request.form['username']
        password = request.form['password']
        return 'success' if username and password == 'admin' else 'fail'

    def execute(self) -> None:
        self.app.run(debug=True, host=self.host, port=self.port)


login_service = LoginService()
if __name__ == '__main__':
    login_service.execute()
