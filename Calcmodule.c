#include <Python.h>

static PyObject *
Calc_check(PyObject *self, PyObject *args)
{
    char* str;
	char result;
    if(!PyArg_ParseTuple(args, "s", &str))
        return NULL;

	int check = atoi(str);

	switch (check)
	{
	case 10:
		result = "정상";
		break;
	case 20:
		result = "가출인";
		break;
	case 40:
		result = "시설보호무연고자";
		break;
	case 60:
		result = "지적장애인";
		break;
	case 61:
		result = "지적장애인(18세미만)";
		break;
	case 62:
		result = "지적장애인(18세이상)";
		break;
	case 70:
		result = "치매환자";
		break;
	case 80:
		result = "불상(기타)";
		break;
	default:
		result = "정보없음";
		break;
	}

	return Py_BuildValue("s", result);
}

static PyMethodDef CalcMethods[] = {
    {"calcCheck",Calc_check, METH_VARARGS, "비고사항 구분"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef calcmodule = {
    PyModuleDef_HEAD_INIT,
    "calc",
    "그래프용 실종자 비고사항 구분",
    -1, CalcMethods
};

PyMODINIT_FUNC
PyInit_calc(void)
{
    return PyModule_Create(&calcmodule);
}