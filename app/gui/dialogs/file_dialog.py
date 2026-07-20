from PySide6.QtWidgets import QFileDialog


def open_image_dialog(parent):

    filename, _ = QFileDialog.getOpenFileName(
        parent,
        "Open MRI Image",
        "",
        "Images (*.png *.jpg *.jpeg *.bmp)",
    )

    return filename