__version__ = "0.1.0"

from ._function import process_image

{% if cookiecutter.include_reader_plugin == 'y' %}from ._reader import napari_get_reader{% endif %}
{% if cookiecutter.include_writer_plugin == 'y' %}from ._writer import napari_get_writer, napari_write_image{% endif %}
{% if cookiecutter.include_dock_widget_plugin == 'y' %}from ._dock_widget import napari_experimental_provide_dock_widget{% endif %}
{% if cookiecutter.include_function_plugin == 'y' %}from ._function import napari_experimental_provide_function{% endif %}
