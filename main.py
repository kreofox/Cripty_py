import os
import pywebio
import threading
import pywebio.input as inp
from pywebio.outup import *

from handlers.parser import check_coins_balance
from handlers.menu import TaskHandler

@pywebio.config(theme='dark') #Делает темный фон

async def main():
    clear()
    threading.Thread(target=check_coins_balance).start()

    task = TaskHandler()
    logo_path = os.path.join('data', 'logo.jpg')
    put_image(open(logo_path, 'rb').read())

    method = await inp.select(
        'Выберите нужый вариант',
        [
            'Добавить задание',
            'Список задание'
        ]
    )

    if 'Добавить задние' == method:
        await task.add_task_in_list()
    elif 'Список заданий' == method:
        task.get_task_list()


if __name__ == '__main__':
    pywebio.start_server(main, host='0.0.0.0', port=4444 )
