

# Переходим в домашнюю директорию
cd ~/

# Скачиваем инструментарий и переходим в папку с ним
git clone https://github.com/GMIG/Instruments.git 
cd Instruments/daemon

# Для удобства настраиваем окружение на работу с 3-й версией питона
alias pip=pip3
alias python=python3

# Устанавливаем виртуальное окружение pipenv
pip install --user pipenv
PATH=$PATH:~/.local/bin

# Устанавлиаем необходимые зависимости
pipenv update

# Возвращаемся в домашнюю папку и создаем скрипт автозапуска демона управления
cd ~/
{
  echo '#!/bin/bash'
  echo ' '
  echo 'cd ~/Instruments/daemon'
  echo '~/.local/bin/pipenv run python ~/Instruments/daemon/daemonMain.py'
} > autorun-daemon.sh

# Даем права на выполнение
chmod +x autorun-daemon.sh
 
# Добавляем созданный скрипт в автозагрузку 
# работает для raspbery pi с установленной RasbianOS с окружением рабочего стола\
# если у вас другая ОС, то файл автостарта может быть расположен в другом месте
sudo sh -c "echo '@~/autorun-daemon.sh' >> /etc/xdg/lxsession/LXDE-pi/autostart"