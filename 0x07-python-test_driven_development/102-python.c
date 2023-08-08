#include <Python.h>

/**
 * print_python_string - Prints information about a Python string.
 * @p: A PyObject pointer.
 */

void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		Py_ssize_t length;
		wchar_t *value;

		length = PyUnicode_GET_LENGTH(p);
		value = PyUnicode_AsWideCharString(p, &length);

		if (value)
		{
			printf("[.] string object info\n");
			printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ?
					"compact ascii" : "compact unicode object");
			printf("  length: %ld\n", length);
			printf("  value: %ls\n", value);

			PyMem_Free(value);
			return;
		}
	}

	printf("[.] string object info\n");
	printf("  [ERROR] Invalid String Object\n");
}
