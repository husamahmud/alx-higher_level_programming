#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list_info(PyObject *p)
{
    long int len;
    int i;
    PyListObject *list;

    len = PyList_Size(p);
    list = (PyListObject *)p;
    printf("[*] Size of the Python List = %li\n", len);
    printf("[*] Allocated = %li\n", list->allocated);
    for (i = 0; i < len; i++)
    {
        PyObject *item = list->ob_item[i];
        printf("Element %i: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
