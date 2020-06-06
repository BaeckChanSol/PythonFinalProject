#include <python.h>
#include <time.h>

int months[] = {31,28,31,30,31,30,31,31,30,31,30,31};

static PyObject *
calc_day(PyObject *self, PyObject *occrdeDay)
{
    int gettenDay = 0;
    int year = 0;
    int mon = 0;
    int day = 0;
    int result = 0;
	
	time_t ct = time(NULL);
	struct tm lt = *localtime(&ct);

    if (!PyArg_ParseTuple(occrdeDay, "i", &gettenDay))
        return NULL;

    day = gettenDay%100;
    gettenDay = gettenDay / 100;
    mon = gettenDay%100;
    gettenDay = gettenDay / 100;
    year = gettenDay;

    result += (lt.tm_mday - day);
    if ((result) < 0)
    {
        lt.tm_mon -= 1;
        result += months[lt.tm_mon];
    }

    result += ((lt.tm_mon - mon)*100);
    if ((result) < 0)
    {
        lt.tm_year -= 1;
        result += 1200;
    }

    result += ((lt.tm_year - year)*100);

    return Py_BuildVaule("i",result);
}

static PyMethodDef CalcMethods[] = {
    //파이썬에서 쓸 함수이름,
    //실제 함수 이름,
    //파이썬에서 호출할 때 인수를 어떻게 자료형으로 받을지 결정하는 상수
    //함수에 대한 설명
    {"calc_day", calc_day, METH_VARARGS, "실종일로부터 며칠 지났는지 알려주는 함수"},
    //추가할거면 이쪽에 정의
    {NULL,NULL,0,NULL}          //마지막이란 표시
};

static struct PyModuleDef calcmodule = {
	PyModuleDef_HEAD_INIT,
	"calc",
	"C++이용 계산모듈",
	-1,
	CalcMethods
};

PyMODINIT_FUNC
PyInit_calc(void)
{
    return PyModule_Create(&calcmodule);
}