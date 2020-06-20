#include <Python.h>
#include <chrono>
#include <string>

static PyObject *
spam_calc(PyObject *self, PyObject *args)
{
    int months[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    char *str;
    if(!PyArg_ParseTuple(args, "s", &str))
        return NULL;

    int date = atoi(str);

    auto tp = std::chrono::system_clock::now();
	auto ct = std::chrono::system_clock::to_time_t(tp);
	auto lt = localtime(&ct);

    int day = date%100;
    date = date/100;
    int month = date%100;
    int year = date/100;


    int resultDay = lt->tm_mday - day;
    if (resultDay < 0 )
    {
        month++;
        resultDay += months[lt->tm_mon-1];
    }
    int resultMon = lt->tm_mon - month + 1;
    if(resultMon < 0)
    {
        year++;
        resultMon+=12;
    }
    int resultYear = (lt->tm_year+1900)-year;
    std::string result = std::to_string(resultYear) + " Y ";
    result = result + std::to_string(resultMon) + " M ";
    result = result+ std::to_string(resultDay) + " D";

    return Py_BuildValue("s",result.c_str());
}

static PyMethodDef SpamMethods[] = {
    {"calc",spam_calc, METH_VARARGS, "Elapsed time"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",
    "Elapsed time",
    -1, SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}