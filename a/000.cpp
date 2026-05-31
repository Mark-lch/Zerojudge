#include<iostream>
#include<vector>
using namespace std;
int main(){
    int N;
    cin>>N;
    vector<bool> array(N+1,true);

    for(int a=2;(a*a)<=N;a++){
        if(array[a]){
            for(int i=a*a;i<=N;i+=a){
                array[i]=false;
            }
        }
    }
    for(int isprime=2;isprime<=N;isprime++){
        if(array[isprime])
            cout<<isprime<<" ";
    }
}