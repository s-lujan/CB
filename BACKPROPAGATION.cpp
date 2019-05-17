/******************************************************
ALGORITMO DE BACKPROPAGATION
*************************************************************/


//ME GUSTARÍA AJUSTARLO UN POQUITO MAS (valores de n, B, etc)

#include <iostream>
#include <cmath>

using namespace std;

double e= 2.718281828;
const double n= 1.1;

const int A= 5;
const int B= 50;
const int C= 5;

double x[A]={1, 0, 0.3, 0.9, 0.2}; //x[0]=1;
double h[B];
double o[C]; //o[0]=0 y y[0]=0 permanentemente ya que no se usan
double y[C]={0, 0.3, 0.4, 0.6, 0.9}; 

double w1[A][B];
double w2[B][C];

double sumaX(int j){
    double s=0.0;
    for (int i= 0; i<A; i++){
        s+=x[i]*w1[i][j];
    }
    return s;
}

double sumaH(int j){
    double s=0.0;
    for (int i= 0; i<B; i++){
        s+=h[i]*w2[i][j];
    }
    return s;
}

double sumaO(int j){
    double s=0.0;
    for (int i= 1; i<C; i++){
        s+=o[i]*(1-o[i])*(y[i]-o[i])*w2[j][i];
    }
    return s;
}

void printO(){
    cout << "\n";
    for (int i=0; i<C; i++)
        cout << "// " << o[i];
}

bool equal(){
    for (int i=0; i<C; i++)
        if (o[i]!=y[i]) return false;
    return true;
}

int main()
{
    x[0]=1;
    h[0]=1;
    o[0]=0;
    y[0]=0;
    int iteracion=0;
    printO();
    for (int a=0; a<200; a++){
        //step 2
        for (int j=1; j<B; j++)
            h[j]=1/(1+pow(e, -1.0*sumaX(j)));
        //step 3
        for (int j=1; j<C; j++)
            o[j]=1/(1+pow(e, -1.0*sumaH(j)));
        //step 4
        for (int i=0; i<B; i++)
            for (int j=1; j<C; j++)
                w2[i][j]=n*h[i]*o[j]*(1-o[j])*(y[j]-o[j]);
        //step 5
        for (int i=0; i<A; i++)
            for (int j=1; j<B; j++)
                w1[i][j]=n*x[i]*h[j]*(1-h[j])*sumaO(j);
        cout << "\niteracion #" << iteracion++;
        printO();
    }
    return 0;
}
