# Второй урок
Базовые операции при работе с изображением.
## План лекции
- считывание и редактирование значения индивидуального пикселя
- цветовые модели: [RGB][RGB], [Grayscale][Grayscale]
- ROI
- базовые математические операции
- измерение эффективности исполнения
- методы увеличения производительности

## Практика
1. [`change_color.py`][change_color_ex]:
  - Работаем с отдельным пикселем
  - Разделяем пиксель на цвета
  - О способе вывода с фигурными скобками читать [здесь][string_format]
2. [`roi_image.py`][roi_image_ex]:
  - Выделяем кусок изображения
  - Вставляем его в копию первоначального изображения
  - Про копирование в Python читать [здесь][copy_in_python]
  - Бонусное задание: определять вырезанную область мышью. [Пример решения][crope_with_mouse]
    - Учесть что направление выделения может быть как снизу вверх, так и наоборот
3. [`find_blue_objects.py`][find_blue_objects]:
  - Конвертируем изображение в [HSV][HSV]
  - Определяем диапазон цвета для отображения
  - Накладываем маску изображения


[RGB]: https://en.wikipedia.org/wiki/RGB_color_model
[Grayscale]: https://en.wikipedia.org/wiki/Grayscale
[string_format]:https://docs.python.org/2/library/string.html#format-examples
[copy_in_python]:https://docs.python.org/2/library/copy.html
[roi_image_ex]: ./examples/roi_image.py
[change_color_ex]: ./examples/change_color.py
[crope_with_mouse]: ./examples/crope_image_with_mouse.py
[find_blue_objects]: ./exmples/find_blue_objects.py
[HSV]: https://en.wikipedia.org/wiki/HSL_and_HSV
