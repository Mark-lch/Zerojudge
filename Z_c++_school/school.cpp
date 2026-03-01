#include<iostream>
#include<vector>
using namespace std;
int main(){
    int a,b,res;
    vector<int> result;
    
    cin>>a>>b;
    
    for(int i=a;i<=b;i++){
        if (i%3==2 && i%5==3 && i%7==2){
            res=i;
            for(int i=0;res<=b;i++){
                result.push_back(res);
                res+=105;
            }
        }
    }
    if(result.size()==0){
        cout<<"none";
        return 0;
    }

    for(int res:result){
        cout<<res<<" ";
    }
}