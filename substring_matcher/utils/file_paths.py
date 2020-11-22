import os
import sys


def resource_path(relative_path):
    """
    Gets the absolute path to resource. Necessary for
    providing the paths the code should check for a
    given resource. This strategy is being used since
    it works for the dev environment and the executable
    that gets created by PyInstaller.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
