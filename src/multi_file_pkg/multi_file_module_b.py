"""Usage of data class"""

from multi_file_pkg import multi_file_module_a as module_a


def multi_file_func() -> module_a.SomeHashableDataClass:
    """Usage of data class

    :return: hashable data class
    :rtype: multi_file_pkg.multi_file_module_a.SomeHashableDataClass
    """
    inst = module_a.SomeHashableDataClass()
    return inst
