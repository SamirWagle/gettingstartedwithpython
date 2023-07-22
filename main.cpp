#include <iostream>
using namespace std;
#include "linkedlist.h"
#include "linkedlist_stack.h"
#include "array_stack.h"
int main(){

    cout<<"Array implementation of Stack(1 for true 0 for false)\n";
    ArrayStack S1(3);
    cout<<S1.isEmpty()<<endl;
    cout<<S1.isFull()<<endl;
     for(int i=1;i<=3;i++){
        int j=i*10;
        S1.push(j);
    }
    S1.push(40);
    S1.top();
    for(int i=1;i<=3;i++){
        S1.pop();
    }
    S1.pop();
    cout<<endl<<endl;

    cout<<"LinkedList implementation of Stack(1 for true 0 for false)\n";
    LinkedListStack L1;
    cout<<L1.isEmpty()<<endl;
    for(int i=1;i<=3;i++){
        int j=i*10;
        L1.push(j);
    }
    L1.push(40);
    L1.top();
    for(int i=1;i<=4;i++){
        L1.pop();
    }
    L1.pop();
    return 0;
}