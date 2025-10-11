from PySide6.QtGui import QPixmap, QImage, QColor

def crop_transparent_area(pixmap: QPixmap) -> QPixmap:
    """Обрезает прозрачные края изображения по альфа-каналу."""
    image = pixmap.toImage()
    width, height = image.width(), image.height()

    min_x, min_y = width, height
    max_x, max_y = -1, -1

    for y in range(height):
        for x in range(width):
            if image.pixelColor(x, y).alpha() > 0:
                if x < min_x: min_x = x
                if y < min_y: min_y = y
                if x > max_x: max_x = x
                if y > max_y: max_y = y

    # если все пиксели прозрачные — вернуть пустой
    if max_x == -1 or max_y == -1:
        return QPixmap()

    # вырезаем только видимую область
    rect_width = max_x - min_x + 1
    rect_height = max_y - min_y + 1
    cropped = pixmap.copy(min_x, min_y, rect_width, rect_height)
    return cropped
