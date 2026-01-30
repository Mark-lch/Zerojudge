#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main(){
    int data;
    while (cin>>data){
        string result;
        if (data==0){   
            cout<<0;
            continue;
        }
        while (data!=0){            
            result += to_string(data%2);
            data=data/2;
        }
        reverse(result.begin(),result.end());
        cout<<result<<endl;
       }
}

//為了寫這個學了很多c++概念 不輟不輟
// 就是有點費時間.