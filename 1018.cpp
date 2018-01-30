
#include <iostream>

using namespace std;

int main() {
  
  int N, i, n;
  int notas [] {100, 50, 20, 10, 5, 2, 1};
  
    
  cin >> N;
  
  cout << N << endl;
  for (i = 0; i < sizeof(notas)/sizeof(*notas) ; ++i)
  {
    n = (int) N/notas[i];
    N = N - (notas[i]*n);
    cout << n << " nota(s) de R$ " << notas[i] << ",00" << endl;
    
  }

 
  

  
}