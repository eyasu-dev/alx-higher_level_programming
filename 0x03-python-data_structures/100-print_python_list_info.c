#include <Python.h>
#include <stdio.h>
/**
*print_python_list_info - a function that prints a python list
*@p:a pyobject vairable
*Return: none
*/
void print_python_list_info(PyObject *p)
{
        int list_size;
        int alloc;
        int counter;
        PyObject *obj;
        list_size = Py_SIZE(p);
        alloc = (*(PyListObject *)p).allocated;
        printf("[*] Size of the Python List = %d\n", list_size);
        printf("[*] Allocated = %d\n", alloc);
        for (counter = 0; counter < list_size; counter++)
        {
                printf("Element %d: ", counter);
                obj = PyList_GetItem(p, counter);
                printf("%s\n", Py_TYPE(obj)->tp_name);
        }
}
