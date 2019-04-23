# -*- coding:utf-8 -*-
import os


def iter_files(path):
    r"""
    Returns a list of all files in the file directory path.
    :param path: file path, str object.
    :return: files path list.
    :rtype: list object
    """

    filename = []

    def iterate_files(path):

        path_rest = path if not isinstance(path, bytes) else path.decode()
        abspath = os.path.abspath(path_rest)

        try:
            all_files = os.listdir(abspath)
            for items in all_files:
                files = os.path.join(path, items)
                if os.path.isfile(files):
                    filename.append(files)
                else:
                    iterate_files(files)
        except (FileNotFoundError, AttributeError, BytesWarning, IOError, FileExistsError):
            pass

    iterate_files(path)

    return filename
