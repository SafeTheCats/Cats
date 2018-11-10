Safer-Cats
==========

Safer-Cats создан и модифицируется в течение обучения в `Learn Python`_ .


Цель проекта
------------

Создать приложение для распознавания котов по камере в реальном времени и уведомлении
пользователя при обнаружении посредством Telegram бота.

Настройка
---------

Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

    PROXY = {'proxy_url': 'socks5://ВАШ_SOCKS5_ПРОКСИ:1080',
            'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}

    API_KEY = 'API ключ, который вы получили у BotFather'

    CLARIFAI_API = 'API ключ, который вы получили на сайте https://clarifai.com/'

    IP_CAMERA = 0  # По умолчанию 0, нужно ввести адрес камеры. Например: IP_CAMERA = "rtsp://10.42.0.57:554/onvif1"

Необходимо установить библиотеки telegram-bot, OpenCV и Clarifai.

Запуск
------

В активированном виртуальном окружении выполните:

.. code-block:: text

    python3 bot.py
    python3 camer_frame.py


Отправьте сообщение боту:

.. code-block:: text

    /frame


.. _Learn Python: https://learn.python.ru/