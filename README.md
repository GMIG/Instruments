# Instruments
Instruments is a software-educational platform that leverages the power of free software to create multimedia and interactive objects.

## What are Instruments for?

Here's what you can do with Tools:

- I need to loop a video file on a museum TV displaying my aphorisms, without any technical pop-ups like "replay." Also, the TV should turn off at night and on in the morning. I have 6,000 rubles for this.
- I found 5 different clips from broadcasts of channels "First," "ICTV," "Novorossiya TV," etc., from June 22, 2014. I need 5 buttons so visitors can switch between these videos. I have 10,000 rubles for this.
- I am reconstructing a Nam June Paik installation and need 20 video files of equal length to play synchronously on 20 different screens. I have 120,000 rubles for this.
- I am retransmitting Tarkovsky's "Mirror," and every time the wind appears, my industrial fan should turn on. I have 6,000 rubles for this.

In other words, Tools allow you to:

- Loop video, image, or audio files on any device that can display them, like a TV, projector, audio speaker, or computer display.
- Control video and image playback—switch, stop, fade, and manage sound volume from the keyboard, an external button, or any other sensor.
- Play videos, images, or sounds synchronously.
- Control external lights and anything else through contact closure.
- Manage the power of the display device (if supported).

## How to use Tools

To work with Tools, you'll need to prepare. This might take a few hours or even days, but it's worth it.

Here's what you'll definitely need to do:

- Buy or find a [Raspberry PI kit](https://ru.wikipedia.org/wiki/Raspberry_Pi).
- Install the system and Tools on it.
- Learn a bit of programming.
- Write your program using Tools.

## What do you need to buy or find to work with Tools?

1. A small computer, Raspberry PI. It looks like an electronic board but don't be afraid, it's a computer. Raspberry PI 4 (2 GB) is the best choice. You can easily buy it in an online store.
2. Power supply for Raspberry PI. In the same store.
3. Computer monitor. Your regular work monitor will do, but having an extra one is more convenient.
4. Cable between the Raspberry PI and the monitor. The Raspberry PI 4 has a micro HDMI port. What port does your monitor have?

If it's HDMI - <img src="https://i.imgur.com/Dri4ET1.png" height="100">,

you need a micro HDMI to HDMI cable <img src="https://i.imgur.com/yJT8veQ.jpg" height="100">.

If your monitor is old and has a VGA port <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/SVGA_port.jpg/1200px-SVGA_port.jpg" height="100">,

you'll also need an HDMI to VGA adapter.

All this can be bought in the same store.

5. Mouse and keyboard. Both should connect via USB <img src="https://i.imgur.com/4n2uyX0.png" height="100">
6. 16 GB microSD card. It's best to choose one of [these](https://maker.pro/raspberry-pi/tutorial/what-micro-sd-card-is-best-for-a-raspberry-pi-4).
7. Regular computer or laptop. It's important that it can insert a microSD card.
8. Regular USB flash drive.

The entire set from items 1, 2, 4, 6, and 8 will cost you 6-7 thousand rubles in 2020.

## You bought all this. What's next?

It's best to follow this guide:
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/1

Here's what you'll see as a result.

<img src="https://i.imgur.com/ZfnvY7O.png" height="400">

You have a new computer. You can freely work on the internet and office programs. But we use it for art.

## Installing Tools on Raspberry PI

To be able to do everything we want, we need to prepare our new computer.

Here's what you need to do:

1. Download [file] and write it to a regular USB flash drive.
2. Insert the flash drive into the Raspberry.
3. Copy the file from the flash drive to the home folder on the Raspberry ([details]).
4. Open the console by clicking the button

<img src="https://i.imgur.com/toYmI5k.png" height="400">

This is the same Linux console featured in hacker TV shows.

5. Enter the command `sudo ./install.sh`. If you see `such a rectangle`, it's code. It needs to be entered somewhere.
6. If everything went well, you will see this window
![Thonny]()

## Learning to program in 5 minutes

Open the Linux console above and type `pipenv run python Main.py`.

What this means is not important for now. The main thing is that a strange video has started in front of you.

### Setting up a simple file player
Code that sequentially loops the files drop.avi and bird.avi.
To close the player, press ESC
```
from mpv_simple import LoopPlayer 
vid = LoopPlayer('vid')
vid.names.append('drop.avi')
vid.names.append('bird.avi')
vid.start()
```
Here's what each line does (in perspective - line by line)
```
vid = LoopPlayer('vid')
```
Create an object vid. In the `LoopPlayer` argument is a letter identifier that will be displayed in the debug console
```
vid.names.append('drop.avi')
```
`vid.names` is an array of strings with the filenames to be played sequentially. It can be edited during playback.
```
vid.start()
```
Starts the player. The player has no "stop" mode. If you need to show a black screen, just make a black screen image in jpeg and add it to `vid.names`.

### Controlling files from the keyboard
To launch `drop.avi` by pressing the `1` key and `bird.avi` by pressing `2`:
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
<add keyboard description>
`vid.start(int(key.char))` launches the file with number 1 or 2.

### Adding fade effect with keyboard control
To make the current file fade out and `drop.avi` start when pressing key `1`, and the same for key `2` and `bird.avi`:
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
