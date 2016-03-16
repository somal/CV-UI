# Третий урок
1. Morphological transformations
    - `Erosion` \- размытие, разрушение
        - пример: [`image_erosion.py`][image_erosion]
        - изменить размеры массива `kernel`, проанализировать результат
        - заменить генерацию массива `np.ones` на `np.zeroes`, проанализировать
        - написать размытие видеопотока с камеры; [вариант решения][video_erosion]
        - подробнее о работе алгоритма размытия читать [здесь][how_to_erosion]
    - `Dilation` \- растяжение
        - пример: [`video_dilation.py`][video_dilation]
        - написать версию для обработки изображения
        - подробнее о работе алгоритма растяжения читать [здесь][how_to_dilation]
    - `Opening` & `Closing`
        - `opening` \- сокращенное название для алгоритма `dilation` который обрабатывает изображение, уже подвергнутое `erosion`
        - функция полезна для устранения шума
        - [сравнение][video_opening] отдельной функции и соединения `erosoin & dilation`
        - `closing` \- алгоритм, обратный `opening`
        - кусок кода: closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        - функция полезна для устранения мелких точек на изображении
        - написать сравнение результата при обработке двумя функциями и обработке встроенной функцией
2. Gradients
    - `Sobel & Scharr derivatives` (опрераторы [Собеля и Щарра][sobel_scharr])
        - [принцип работы алгоритмов][how_to_sobel]
        - [пример кода][sobel_conturs]
        - изменить размеры `ksize` (могут варьироваться от 1 до 31, обязательно нечётное число)
        - сделать оба изображения полупрозрачными и наложить друг на друга
        - даст ли нам предыдущий шаг нужные нам контуры? обьяснить почему
    - `Laplacian`
        - [принцип работы алгоритма][how_to_laplacian]
        - [пример кода][laplscian_conturs]
3. Canny edge detector
    - cтатья на [википедии][canny_edge]
    - отличный туториал по алгоритму [здесь][how_to_canny]
    - [реализация][canny_edge_detector] алгоритма
    - изменить порог обработки (2ой и 3ий аргумент функции `cv2.Canny()`)
    - скомбирировать с ранее изученными морфологическими трансформациями
4. `Усложненная` домашняя работа
    - выделить синий канал изображения из видеопотока
    - применить морфологические трансформации для устранения шумов
    - сигнализировать о детекции синего объекта, путем рисования прямоугольника вокруг него

По возникшим вопросам, писать в телеграме: @piaxar , @Somal1996

[image_erosion]:./scr/image_erosion.py
[video_erosion]:./scr/video_erosion.py
[video_dilation]:./scr/video_dilation.py
[video_opening]:./scr/video_opening.py
[sobel_conturs]:./scr/sobel_conturs.py
[laplscian_conturs]:./scr/laplscian_conturs.py
[canny_edge_detector]:./scr/canny_edge_detector.py
[how_to_erosion]:http://homepages.inf.ed.ac.uk/rbf/HIPR2/erode.htm
[how_to_dilation]:http://homepages.inf.ed.ac.uk/rbf/HIPR2/dilate.htm
[how_to_sobel]:https://habrahabr.ru/post/128753/
[how_to_laplacian]:http://robocraft.ru/blog/computervision/460.html
[how_to_canny]:http://dasl.mem.drexel.edu/alumni/bGreen/www.pages.drexel.edu/_weg22/can_tut.html
[canny_edge]:https://en.wikipedia.org/wiki/Canny_edge_detector
[sobel_scharr]:https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80_%D0%A1%D0%BE%D0%B1%D0%B5%D0%BB%D1%8F
