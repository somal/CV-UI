# Установка [OpenCV][opencv]
__Основная рабочая ОС__ - [Ubuntu][ubuntu]. Но это не значит, что нельзя будет работать на других ОСях. В этих случаях автор не гарантирует работы всего кода.

__Основный язык__ - Python, но также присутствуют примеры на С++ и Java.


## Установка OpenCV под Ubuntu
Прежде чем начать, почитайте [introduction][installing_introduction]

### Способ 1 [желательно]
Он самый простой. Спасибо товарищу [Jay Rambhia][jr], который создал [скрипты][scripts], которые ставят последнюю версию OpenCV со всеми зависимостями. Очень просто и быстро. Автор ставил таким способом.

### [Способ 2][second_variant]

### [Способ 3 (попробуйте-с виду неплохой)][third_variant]

## Установка OpenCV под Windows
Вот [тут][off_installing_opencv_on_windows] официальный туториал. 
Вот [тут][unoff_installing_opencv_on_windows] лежит установщик. Кстати, на этой страничке много библиотек, собранных в исполняемые файлы, что очень облегчает работу на Python on Windows.


## После установки
После того, как Вы все сделали, давайте проверим как все поставилось.
Для этого зайдем туда, куда мы все поставили (для Ubuntu это `/usr/local/share/OpenCV`)
В `java` лежит jar файл, который позволяет использовать OpenCV в Java.
Самое интересное лежит `samples`.
Там есть примеры для С++ и Python в соответствующих папках(`cpp` и `python`). Для лучшей демонстрации Вы можете запустить `python/demo.py` 





<!--LINKS-->
[ubuntu]: http://ubuntu.ru/
[opencv]: http://opencv.org/
[installing_introduction]: http://docs.opencv.org/3.1.0/d0/de3/tutorial_py_intro.html#gsc.tab=0
[jr]: https://github.com/jayrambhia
[scripts]: https://github.com/jayrambhia/Install-OpenCV
[second_variant]: http://milq.github.io/install-opencv-ubuntu-debian/
[off_installing_opencv_on_windows]: http://docs.opencv.org/3.1.0/d5/de5/tutorial_py_setup_in_windows.html#gsc.tab=0
[unoff_installing_opencv_on_windows]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
[third_variant]: https://github.com/sgjava/install-opencv
