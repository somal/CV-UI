# Третий урок
1. Morphological transformations
    - `Erosion` \- размытие, разрушение
        - Пример: [`image_erosion.py`][image_erosion]
        - Изменить размеры массива `kernel`, проанализировать результат
        - Заменить генерацию массива `np.ones` на `np.zeroes`, проанализировать
        - Написать размытие видеопотока с камеры; [вариант решения][video_erosion]
        - Подробнее о работе алгоритма размытия читать [здесь][how_to_erosion]
    - `Dilation` \- растяжение
        - Пример: [`video_dilation.py`][video_dilation]
        - Написать версию для обработки изображения
        - Подробнее о работе алгоритма растяжения читать [здесь][how_to_dilation]
    - `Opening` & `Closing`
        - `Opening` \- сокращенное название для алгоритма `dilation` который обрабатывает изображение, уже подвергнутое `erosion`
        - Функция полезна для устранения шума
        - [Сравнение][video_opening] отдельной функции и соединения `erosoin & dilation`
        - `Closing` \- алгоритм, обратный `opening`
        - Кусок кода: closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        - Функция полезна для устранения мелких точек на изображении
        - Написать сравнение результата при обработке двумя функциями и обработке встроенной функцией
2. Gradients
    - `Sobel & Scharr derivatives` (опрераторы [Собеля и Щарра][sobel_scharr])
        - [Принцип работы алгоритмов][how_to_sobel]
        - [Пример кода][sobel_conturs]
        - Изменить размеры `ksize` (могут варьироваться от 1 до 31, обязательно нечётное число)
        - Сделать оба изображения полупрозрачными и наложить друг на друга
        - Даст ли нам предыдущий шаг нужные нам контуры? обьяснить почему
    - `Laplacian`
        - [Принцип работы алгоритма][how_to_laplacian]
        - [Пример кода][laplscian_conturs]
3. Filtration
    - `Convolution`
        - Фильтрация методом свертки
        - Что такое свертка читать [здесь][what_is_convolution]
        - Что такое свертка [понятным языком][convolution_easy]
        - Реализовать программу по алгоритму, данному по ссылке выше
4. Canny edge detector
    - Статья на [википедии][canny_edge]
    - Отличный туториал по алгоритму [здесь][how_to_canny]
    - [Реализация][canny_edge_detector] алгоритма
    - Изменить порог обработки (2ой и 3ий аргумент функции `cv2.Canny()`)
    - Скомбирировать с ранее изученными морфологическими трансформациями
5. `Усложненная` домашняя работа
    - Сжать исходное изображение
    - Выделить синий канал изображения 
    - Применить морфологические трансформации для устранения шумов
    - Найти крайние границы редуцированного обьекта
    - Сигнализировать о детекции синего объекта
    - [Решение][homework]
6. Почитать к следующему занятию:
    - [Fourier transformation](http://docs.opencv.org/3.1.0/de/dbc/tutorial_py_fourier_transform.html#gsc.tab=0)
    - [Hough Transform](http://docs.opencv.org/3.1.0/d6/d10/tutorial_py_houghlines.html#gsc.tab=0)
    - [Hough Circle Transform](http://docs.opencv.org/3.1.0/da/d53/tutorial_py_houghcircles.html#gsc.tab=0)
    - [Теория](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%A5%D0%B0%D1%84%D0%B0)

По возникшим вопросам, писать в телеграме: @piaxar , @Somal1996

[image_erosion]:./src/image_erosion.py
[video_erosion]:./src/video_erosion.py
[video_dilation]:./src/video_dilation.py
[video_opening]:./src/video_opening.py
[sobel_conturs]:./src/sobel_conturs.py
[laplscian_conturs]:./src/laplscian_conturs.py
[canny_edge_detector]:./src/canny_edge_detector.py
[homework]:./src/homework.py
[how_to_erosion]:http://homepages.inf.ed.ac.uk/rbf/HIPR2/erode.htm
[how_to_dilation]:http://homepages.inf.ed.ac.uk/rbf/HIPR2/dilate.htm
[how_to_sobel]:https://habrahabr.ru/post/128753/
[how_to_laplacian]:http://robocraft.ru/blog/computervision/460.html
[how_to_canny]:http://dasl.mem.drexel.edu/alumni/bGreen/www.pages.drexel.edu/_weg22/can_tut.html
[canny_edge]:https://en.wikipedia.org/wiki/Canny_edge_detector
[sobel_scharr]:https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80_%D0%A1%D0%BE%D0%B1%D0%B5%D0%BB%D1%8F
[what_is_convolution]:https://ru.wikipedia.org/wiki/%D0%A1%D0%B2%D1%91%D1%80%D1%82%D0%BA%D0%B0_(%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7)
[convolution_easy]:https://habrahabr.ru/post/62738/
