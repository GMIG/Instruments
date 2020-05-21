# Инструменты
Инструменты - это программно-образовательная платформа, которая позволяет использовать мощь бесплатного программного обеспечения для того чтобы делать мультимедийные и интерактивные объекты
## Для чего нужны инструменты?

Вот что можно сделать с помощью интсрументов:

- мне нужно по кругу запустить видеофайл на музеном телевизоре, где демонстрируется файл с моими афоризмами. При этом не должно появляться технических окошек "replay" и тд. Также нужно чтобы телевизор ночью сам выключался, а утром включался. У меня на это 6 000 руб.
- я нашел 5 разных отрезков из трансляций телеканалов "Первый", "ICTV", "Новороссия ТВ" и тд от 22 июня 2014 года и необходимо сделать 5 кнопок, с помощью которых посетитель сможет переключать видео. У меня на это 10 000 руб.
- я делаю реконструкцию инсталляции Нам Джун Пайка и мне необходимо чтобы синхронно проигрывались 20 видео файлов одинаковой длинны на 20 разных экранах. У меня на это 120 000 руб.
- я ретранслирую "Зеркало" Тарковского и каждый раз, когда там появляется ветер должен включался мой промышленный вентилятор. У меня та это 6 000 руб.

Другими словами Инструменты позволяют:

- запускать по кругу файлы видео, изображения или звука на любом устройстве, которое может их выводить. Например, телевизор, проектор, аудио-колонка или дисплей компьютера. 
- управлять воспроизведением видео, изображения - переключать, останавливать, делать fade и управлять звуком - делать громче или тише. Управлять с клавиатуры или внешней кнопки или любого другого датчика.
- запускать видео, изображения или звук синхронно.
- управлять внешним светом и чем угодно через замыкание контактов.
- управлять включением и выключением устройства вывода изображения (если оно это поддерживает)

## Как использовать Инструменты

Для того чтобы работать с Инструментами нужно подготовится. Это займет несколько часов, а то и дней. Но это стоит того.

Вот что вам точно придется сделать:

- купить или найти [комплект Raspberry PI](https://ru.wikipedia.org/wiki/Raspberry_Pi) .  
- установить на него систему и Инструменты
- научиться немного программировать
- написать свою программу, используя Инструменты

## Что необходимо приобрести или найти для того, чтобы работать с Инструментами?

1. Маленький компьютер Raspbrry PI. Он выглядит как электронная плата, но не бойтесь, это компьютер. Лучше всего выбрать Raspberry PI 4 (2 Гб). Проще всего купить в интернет-магазине.
2. Блок питания к Raspbrry PI. В том же магазине.
3. Компьютерный монитор. Подойдет ваш обычный рабочий монитор, но удобнее иметь еще один.
4. Провод между Raspberry PI и монитором. У Raspberry PI 4 разъем для монитора называется micro HDMI. Какой разъем у вашего монитора? 

Если HDMI - <img src="https://i.imgur.com/Dri4ET1.png" height="100">, 

то вам нужен провод micro HDMI-HDMI <img src="https://i.imgur.com/yJT8veQ.jpg" height="100">. 

Если монитор у вас старый и разъем у него VGA <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/SVGA_port.jpg/1200px-SVGA_port.jpg" height="100">,

то кроме провода micro HDMI-HDMI вам понадобится переходник hdmi-VGA. 

Все это можно купить в том же магазине.

5. Мышка и клавиатура. Оба должны подключаться по USB <img src="https://i.imgur.com/4n2uyX0.png" height="100">
6. microSD карта 16 GB. Лучше всего выбирать одну из [этих](https://maker.pro/raspberry-pi/tutorial/what-micro-sd-card-is-best-for-a-raspberry-pi-4).
7. Обычный компьютер или ноутбук. Важно, чтобы в них можно было вставить microSD.
8. Обычная флешка

Весь комплект из 1,2,4,6,8 обойдется вам в 6-7 тыс руб в 2020 году.

## Вы купили все это. Что дальше

Лучше всего следовать вот этому руководству
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/1

Вот что вы увидите в результате. 

<img src="https://i.imgur.com/ZfnvY7O.png" height="400">

У вас появился новый компьютер. На нем можно свободно работать в интернете и в офисных программах. Но мы используем его для искусства.

## Устанавливаем на Raspbrry PI Инструменты

Чтобы иметь возможность делать все что мы хотим, нам надо подготовить наш новый компьютер.

Для этого нужно: 

1. Скачать [файл] и Записать его на обычную флешку
2. Вставить флешку в Raspberry
3. Переписать файл с флешки в папку home на Raspberry ([подробнее]) 
4. Запустить консоль, нажав на кнопку

<img src="https://i.imgur.com/toYmI5k.png" height="400">

Эта та самая linux консоль, которая фигурирует в сериалах про хакеров. 

5. Ввести команду `sudo ./install.sh`. Теперь если вы видите `такой прямоугольник` это код. Его нужно куда-то вводить.
6. Если все прошло хорошо, то вы увидите вот это окно
![Thonny]()
## Учимся программировать за 5 минут

Откройте linux консоль сверху и напишите там `pipenv run python Main.py`. 

Что это значит - пока не важно. Главное что перед вами запустилось странное видео.

### Настраиваем простой проигрыватель файлов
Код, который по очереди по кругу проигрывает файлы drop.avi,  bird.avi.
Чтобы закрыть проигрыватель нажмите ESC
```
from mpv_simple import LoopPlayer 
vid = LoopPlayer('vid')
vid.names.append('drop.avi')
vid.names.append('bird.avi')
vid.start()
```
Вот что делает каждая строчка (в перспективе - построчно)
```
vid = LoopPlayer('vid')
```
Создаем объект vid. В аргументе `LoopPlayer` - буквенный идентификатор, который будет отображаться в консоли отладки
```
vid.names.append('drop.avi')
```
`vid.names` - массив (array) строк с именами файлов, которые будут последовательно проигрываться. Его можно редактировать во время проигрывания. 
```
vid.start()
```
запускает проигрыватель. У проигрывателя нет режима "стоп". Если нужно показать черный экран - просто делаем картинку с черным экраном в jpeg и  добавляем его в `vid.names`

### Управляем файлами с клавиатуры
Для того, чтобы по нажатию клавиши `1` запускался файл `drop.avi`, а по нажатию `2` - `bird.avi`:
```
from mpv_simple import LoopPlayer 
from pynput import keyboard

vid = LoopPlayer('vid')
vid.names.append('drop.avi')
vid.names.append('bird.avi')
vid.start()

def startVideo(key):
    logging.debug(str(key))
    if key.char in ['1','2']:
        vid.start(int(key.char))
listener = keyboard.Listener(on_press=startVideo)
listener.start()
```
<добавить описание keyboard>
`vid.start(int(key.char))` запускает файл с номером 1 или 2
### Делаем затемнение при управлении с клавиатуры
Для того, чтобы по нажатию клавиши `1` происходило затемнение того файла, что проигрывается и запускался `drop.avi` и все то же самое происходило с клавишей `2` и `bird.avi`:
```
from mpv_simple import LoopPlayer 
from pynput import keyboard

vid = LoopPlayer('vid')
vid.names.append('drop.avi')
vid.names.append('bird.avi')
vid.start()

def fadeBackgroundAndPlay(int filenum):
    vid.splayer.fade(1)
    def playFileNum():
        vid.start(filenum)
    vid.splayer.caller.on_faded(playFileNum)
    
vid.start()
def startVideo(key):
    logging.debug(str(key))
    if key.char in ['1','2']:
        fadeBackgroundAndPlay(int(key.char))
listener = keyboard.Listener(on_press=startVideo)
listener.start()
```
