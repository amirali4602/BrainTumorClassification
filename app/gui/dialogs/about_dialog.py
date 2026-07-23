from PySide6.QtWidgets import QMessageBox


def show_about(parent):

    QMessageBox.about(
        parent,
        "About NeuroVision AI",
        """
<h2>NeuroVision AI</h2>

<p><b>Version:</b> 1.0.0</p>

<p>
Brain Tumor MRI Classification using
Deep Learning.
</p>

<p>
Supported Models:
</p>

<ul>
<li>Custom CNN</li>
<li>ResNet50</li>
<li>EfficientNetB0</li>
<li>DenseNet121</li>
<li>EfficientNetV2B0</li>
<li>MobileNetV3 Large</li>
<li>Xception</li>
<li>ConvNeXt Tiny</li>
<li>InceptionV3</li>
</ul>

<p>
Developed using
Python, TensorFlow and PySide6.
</p>
""",
    )