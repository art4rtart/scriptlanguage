#include <python.h>

static PyObject *

spam_strlen(PyObject * self, PyObject *args)
{
	char* str;
	int len;
	if (!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	len = strlen(str);
	return Py_BuildValue("i", len);
}