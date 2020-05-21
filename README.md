# Инструменты
Инструменты - это программно-образовательная платформа, которая позволит музеям использовать мощь бесплатного программного обеспечения чтобы делать красивые мультимедийные и интерактивные инсталляции
## Для чего нужны инструменты?
Описание чего можно добиться с помощью инструментов
## Как использовать инструменты
Описание того, что понадобится, сколько времени займет и где найти.
## Установка Raspberry
### Вы купили распберри. Что дальше
Как и чем подключить распберри к монитору, клавиатуре и мыши
### Устанавливаем на распберри Инструменты
Описание того, как поставить на распберри батч, который установит:
- pipenv
- демон
- авторан скрипт
- main, который работает как LoopPlayer
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

