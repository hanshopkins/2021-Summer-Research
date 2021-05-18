// includes, system
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

// includes, project
#include <cuda_runtime.h>
#include <cufft.h>
#include <cufftXt.h>

// Complex data type
typedef float2 Complex;
static __host__ inline float ComplexAbs(Complex);

//This is the number of data points and stuff
#define N 50

constexpr double Pi = 3.14159265358979323846;

//this is the function we're transforming
float f(float t)
{
    return sin(2*Pi*t);
}

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv) {

    //memory for the function we're transforming
    Complex* h_fvalues = reinterpret_cast<Complex*>(malloc(sizeof(Complex) * N));
    for (unsigned int i = 0; i < N; i++) //initializing
    {
        h_fvalues[i].x = f(i * 1.0 / N);
        h_fvalues[i].y = 0;
    }
    
    //device memory for the signal
    Complex* d_fvalues;
    cudaMalloc(reinterpret_cast<void**>(&d_fvalues), sizeof(Complex)*N);
    //copy host memory to device
    cudaMemcpy(d_fvalues, h_fvalues, sizeof(Complex)*N, cudaMemcpyHostToDevice);

    //setting up the plan
    cufftHandle plan;
    cufftPlan1d(&plan, sizeof(Complex)*N, CUFFT_C2C,1);

    //execute plan. This transforms the signal in place.
    cufftExecC2C(plan, d_fvalues, d_fvalues, CUFFT_FORWARD);

    //copying the results back onto the host
    Complex* h_Fvalues = reinterpret_cast<Complex*>(malloc(sizeof(Complex) * N));
    cudaMemcpy(h_Fvalues, d_fvalues, sizeof(Complex) * N, cudaMemcpyDeviceToHost);

    for (unsigned int i = 0; i < N; i++)
    {
         std::cout << "i: " << i << " Re(F): " << h_Fvalues[i].x/N << " Im(F): " << h_Fvalues[i].y/100 << " |F|: " << ComplexAbs(h_Fvalues[i])/100 << std::endl;
    }

    free(h_fvalues);
    cudaFree(d_fvalues);
    free(h_Fvalues);
    return 0;
}

//Complex absolute value
static __host__ inline float ComplexAbs(Complex a)
{
    return sqrt(a.x * a.x + a.y * a.y);
}
