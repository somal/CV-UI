# Первый урок
Он посвящен обзору компьютерного зрения, что это такое, с чем его едят и что из этого можно получить (см. папку `videos`).
Также рассматривался основной инструмент OpenCV и его история.
[Сама лекция][presentation]


##План лекции и полезные ссылки
- Как меняет видеокамера и комп зрение возможности обычного лего-робота (см. папку `videos`) (опционально)
- Опредение и применение комп зрения
- Общая схема работы с изображениями
- [Пример как за 20 строчек написать неплохое распознавание лиц на Python (по ссылке подробнее кому интересно)][face_detection]
- Что такое [OpenCV][opencv]?
- [Как оно появилось на свет][opencv_history]?
- Полезные ресурсы
- [Функциональность][opencv_modules] (просто посмотрите на количество модулей)
- Книги

## [Практика  ][practices](в папке `src`)
__Задача практики__: научиться работать с камерой, считывать картинку и делать простейшие действия
- [Установка OpenCV][opencv_installing]
- [Решение первого туториала OpenCV-Python][opencv_python_tutorial] 
  - `videocapture.py`: вывод видео с камеры на экран
    - Все общение с OpenCV (cv2 модуль в питоне) происходит с помощью быстрой и производительной библиотеки [numpy][numpy]
    - [Посмотрите зачем нужна 5 строка][ifnm]
    - В питоне все передается ссылками - имейте ввиду!
    - Посмотрите, что хранится в переменной `ret`
    - Подумайте как подключить видеопоток для другой камеры, если их у вас две
    - [Зачем нужен 0xFF?][waitkey]
    - Посмотрите сколько выполняется тело основного цикла и сравнить время нужное для real-time (кстати, какое оно??)
  - [`drawing.py`][drawing]: рисование простых фигух в окошке с изображением. Это часто нужно для выделения требуемых областей (наприме, которые детектировали)
    - Т.к. изображение цветное, то оно имеет 3 канала(цвета -BGR, об этом на следующем занятии). Поэтому мы создаем с помощью `zeros()` массив `512*512*3`,заполненное нулями
    - Дальше рисуем стандартные фигуры
    - Обратите внимание где здесь начало координат и какие направления оси
    - Обратите внимание на преобразования, требуемые для `polylines()`
    - Сделайте так, чтобы окошко не закрывалось сразу после открытия (подсказка, изображение нужно долго выводить)
  - [`mouse_callback.py`][mouse_callback]: Часто требуется что-то отмечать на изображении, поэтому нужно уметь считывать события с мышки
  


<!--LINKS-->
[face_detection]: https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/
[opencv]: http://www.opencv.org
[opencv_history]: https://habrahabr.ru/company/itseez/blog/146434/
[opencv_modules]: http://docs.opencv.org/3.1.0/#gsc.tab=0
[opencv_installing]: https://github.com/Somal/CV-UI/blob/master/docs/OpenCV_installing.md
[opencv_python_tutorial]: http://docs.opencv.org/3.1.0/dc/d4d/tutorial_py_table_of_contents_gui.html#gsc.tab=0
[presentation]: https://github.com/Somal/CV-UI/blob/master/Class1/%D0%9A%D0%BE%D0%BC%D0%BF%D1%8C%D1%82%D0%B5%D1%80%D0%BD%D0%BE%D0%B5%20%D0%B7%D1%80%D0%B5%D0%BD%D0%B8%D0%B5.%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5.%20%D0%91%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20OpenCV.pptx
[practices]: https://github.com/Somal/CV-UI/tree/master/Class1/src
[numpy]: http://www.numpy.org/
[ifnm]: http://stackoverflow.com/questions/419163/what-does-if-name-main-do
[waitkey]: http://stackoverflow.com/questions/14494101/using-other-keys-for-the-waitkey-function-of-opencv
[drawing]:http://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html
[mouse_callback]: http://docs.opencv.org/3.1.0/db/d5b/tutorial_py_mouse_handling.html
