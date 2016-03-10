# Второй урок
Базовые операции при работе с изображением.
## План лекции
- считывание и редактирование значения индивидуального пикселя
- цветовые модели: [RGB][RGB][(BGR in OpenCV)][BGR], [Grayscale][Grayscale]
- ROI
- базовые математические операции
- измерение эффективности исполнения
- методы увеличения производительности

## Практика
1. [`change_color.py`][change_color_ex]:
  - Узнаем информацию об изображении с помощью `img.shape` (описание формы изображения) и `img.dtype` (каким типом данных кодируется каждый пиксель)
  - Работаем с отдельным пикселем [(обратите внимание на систему координат)][coordinate_system]
  - Разделяем пиксель на цвета (если [глубина цвета][depth] более единицы)
  - О способе вывода с фигурными скобками читать [здесь][string_format]
2. [`roi_image.py`][roi_image_ex]:
  - Выделяем кусок изображения
  - Вставляем его в копию первоначального изображения
  - Про копирование в Python читать [здесь][copy_in_python]
  - Бонусное задание: определять вырезанную область мышью. [Пример решения][crope_with_mouse]
    - Учесть что направление выделения может быть как снизу вверх, так и наоборот
3. Разделение изображения на несколько слоёв:
  Если глубина цвета изображения более единицы,то мы мы можем разделить изображение на несколько слоев. Их количество равно глубине цвета. Смотреть [тут][splitting] (Splitting and Merging Image Channels)
  - `cv2.split()`
  - `b = img[:,:,0]`
  - Обратите внимание, что питоновские способ быстрее
  - Можем "сложить" эти каналы обратно в одно изображение
3. [Оптимизация][optimization]:
  Использую встроенную оптимизацию мы можем ускорить код в разы. 
  - Сравнить скорость разделения изображения на слои с оптимизацией и без
3. [`find_blue_objects.py`][find_blue_objects]:
  - Сначала надо научиться конвертировать из одной цветовой палитры в другую с помощью [`cvtColor`][cvtcolor]
  - Туториал по [`object detection`][detection] (далее по нему)
  - Конвертируем изображение в [HSV][HSV]
  - Определяем диапазон цвета для отображения
  - Накладываем маску изображения
3. [Бинаризация][thresholding]:
  Зачастую нам нужно разделить изображение на две части по какому-то порогу. Для это используют бинаризацию. 
4. * Как и было обещано был [показан простейший код на Jave][java]
5. * Рассмотрите самостоятельно [арифметические операции][arithmetic], [размытие][smoothing] (часто используется для фильтрации), [геометрические трансформации][trans]

[trans]: http://docs.opencv.org/3.1.0/da/d6e/tutorial_py_geometric_transformations.html#gsc.tab=0
[smooting]: http://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html#gsc.tab=0
[thresholding]: http://docs.opencv.org/3.1.0/d7/d4d/tutorial_py_thresholding.html#gsc.tab=0
[detection]: http://docs.opencv.org/3.1.0/df/d9d/tutorial_py_colorspaces.html#gsc.tab=0
[cvtcolor]: http://docs.opencv.org/3.1.0/d7/d1b/group__imgproc__misc.html#ga397ae87e1288a81d2363b61574eb8cab&gsc.tab=0
[optimization]: http://docs.opencv.org/3.1.0/dc/d71/tutorial_py_optimization.html#gsc.tab=0
[arithmetic]: http://docs.opencv.org/3.1.0/d0/d86/tutorial_py_image_arithmetics.html#gsc.tab=0
[splitting]: http://docs.opencv.org/3.1.0/d3/df2/tutorial_py_basic_ops.html#fragment&gsc.tab=0
[java]: ./src/Java/Imshow.java
[depth]: https://en.wikipedia.org/wiki/Color_depth
[coordinate_system]: http://stackoverflow.com/questions/25642532/opencv-pointx-y-represent-column-row-or-row-column
[RGB]: https://en.wikipedia.org/wiki/RGB_color_model
[BGR]: http://stackoverflow.com/questions/14556545/why-opencv-using-bgr-colour-space-instead-of-rgb
[Grayscale]: https://en.wikipedia.org/wiki/Grayscale
[string_format]:https://docs.python.org/2/library/string.html#format-examples
[copy_in_python]:https://docs.python.org/2/library/copy.html
[roi_image_ex]: ./src/roi_image.py
[change_color_ex]: ./src/change_color.py
[crope_with_mouse]: ./src/crope_image_with_mouse.py
[find_blue_objects]: ./src/find_blue_objects.py
[HSV]: https://en.wikipedia.org/wiki/HSL_and_HSV
