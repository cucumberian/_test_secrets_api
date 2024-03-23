# Тестовое задание на вакансию backend разработчика
## Задача:
Нужно сделать HTTP сервис для одноразовых секретов наподобие https://onetimesecret.com/.

Он должен позволить создать секрет, задать кодовую фразу для его открытия и сгенерировать код, по которому можно прочитать секрет только один раз. UI не нужен, это должен быть 
JSON Api сервис.

Для написания сервиса можно использовать FastAPI или любой другой фреймворк.
    • Метод /generate должен принимать секрет и кодовую фразу и отдавать secret_key по которому этот секрет можно получить.
    • Метод /secrets/{secret_key} принимает на вход кодовую фразу и отдает секрет.

### Требования:
    • Язык программирования: Python 3.7.
    • Использование Docker, сервис должен запускаться с помощью docker-compose up.
    • Код должен быть реализован на Фреймворке FastAPI .
    • Код должен соответствовать PEP, необходимо использование type hints, к публичным методам должна быть написана документация на английском языке.
### Усложнения:
    • Написаны тесты (постарайтесь достичь покрытия в 70% и больше). Вы можете использовать pytest или любую другую библиотеку для тестирования.
    • Сервис асинхронно обрабатывает запросы.
    • Данные сервиса хранятся во внешнем хранилище, запуск которого также описан в docker-compose. Мы рекомендуем использовать Postgres, но Вы можете использовать любую подходящую базу.
    • Секреты и кодовые фразы не хранятся в базе в открытом виде.
    • Добавлена возможность задавать время жизни для секретов. Можно попробовать реализовать это с помощью TTL индексов.


## Реализация