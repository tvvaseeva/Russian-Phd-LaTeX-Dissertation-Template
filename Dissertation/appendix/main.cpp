#include <stdio.h>                                  // библиотека ввода и вывода на экран
#include <string.h>                                 // стандартная библиотека работы со строками
#include <math.h>                                   // математическая библиотека
#include <time.h>                                   // библиотеке работы с датой и временем
#include <chrono>                                   // библиотека времени(длительность, время, часы)
#include <iostream>


//      Глобальные переменные
// Константы
#define NRUN 1000                                       // Директива, количество запусков
#define NH1 100                                       // Директива, длина фильтра (начальное значение)
#define NH2 1000                                      // Директива, длина фильтра (конечное значение)
#define NHstep 100                                    // Директива,  шаг длина фильтра NH

#define NX1 1000                                        // Директива, длина сигнала (начальное значение)
#define NX2 3000                                        // Директива, длина сигнала (начальное значение)
#define NXstep 1000                                      // Директива,  шаг длина сигнала NX


int _nout;                                               // Длина результата
int _nh;                                                 // текущая длина фильтра
float h[NH2];                                          // Одномерный массив h, с длинной NH=1000
float x[NX2];                                          // Одномерный массив x, с длинной NX=3000
float dir_out[NX2-NH2+1];                                    // Одномерный массив dir_out результат, с длинной NOUT
float result[NH2/NHstep][NX2/NXstep];                   // Результаты измерения времени

//      Для проверки правильности работы методов

void fill_array(float* arr, int n) {                // Функция fill_array
    int i;
    for (i = 0; i < n; i++)                         // Цикл for (инициализация; условие; шаг)
        arr[i] = i + 1;
}
void print_array(float*arr, int n){                  // Печать функция fill_array
    int i;
    for (i = 0; i < n; i++)
        printf("%f \n", arr[i]);
}
//      Реализация 1D свертки (Convolution)
void dir_conv() {
    int i,j;
    for (i = 0; i < _nout; i++) {
        float sum = 0;
        float*ph = h;
        float*px = x + i;
        for (j = 0; j < _nh; j++)
            sum += *ph++ * *px++;
        dir_out[i] = sum;

    }
}

//       Подсчет времени функции
std::chrono::milliseconds measure_func_time(void(*f)()) {   // продолжительность в миллисекундах, соотношение 1: 1000 с секундами
    using clock = std::chrono::high_resolution_clock;       // high_resolution_clock-часы с высоким разрешением
    clock::time_point start = clock::now();                 // time_point-момент времени
    (*f)();
    clock::time_point end = clock::now();
    return std::chrono::duration_cast<std::chrono::milliseconds>(end - start );    //duration_cast-длительность
}

void test_func(){
    for(int j=0; j<NRUN; j++) {            			// loops - количество повторений
        dir_conv();
    }
}

void convolv_time(){
    std::chrono::milliseconds duration;
    for (int nx = NX1; nx < NX2; nx+=NXstep){
        fill_array(x, nx);
        printf("nx - %i \n",nx);
        for (int nh = NH1; nh < NH2; nh+=NHstep) {
            fill_array(h, nh);
            printf("    nh - %i \n",nh);
            _nout = nx-nh+1;                             // длина сигнала на выходе
            _nh = nh;                                    // длина фильтра
            duration = measure_func_time(&test_func);           // тестирование ф-и
            result[(nh-NH1)/NHstep][(nx-NX1)/NXstep] = duration.count();
        }
    }
}
// Функция сохранения в csv
void convolv_csv(int row, int col, float *matrix, char *file_name) {
    int i, j;
    FILE *file;
    file = fopen(file_name, "w");
    if (file == 0)
        printf("file error");
    for (i = 0; i < row; i++) {
        for (j = 0; j < col; j++)
            fprintf(file, "%f; ", matrix[i*col+j]);
        fprintf(file, "\n");
    }
}

int main()
{
    convolv_time();
    char file_name[] = "convolution.csv";
    convolv_csv(NH2/NHstep, NX2/NXstep, (float*)result, file_name);
    return  0;                                          // Возврат результата
}

