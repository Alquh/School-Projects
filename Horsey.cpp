#include <iostream>
#include <time.h>
#include <windows.h>
using namespace std;
#define MAX 25
class Horse {
    int position;
    public:
    Horse() {
        position=0;
    }

    int getPosition() {
        return position;
    }

    void advance() {
        if(rand()%2==0)
            position++;
    }
};

class Race {
    int Lanes;
    Horse *list;
    public:
    Race() {
        list=new Horse[6];
        srand(time(NULL));
    }

    void printLane() {
        for(int a=0;a<6;a++) {
            int q=list[a].getPosition();
            if(q<MAX) {
                for(int b=0;b<MAX;b++)
                if(b==q)
                    cout<<a;
                else
                    cout<<".";
            }
            else
                cout<<"Horse "<<a<<" wins!";
            cout<<endl;
        }
    }

    int start() {
        int result=0;
        for(int a=0;a<6;a++) {
            list[a].advance();
            int q=list[a].getPosition();
            if(q>=MAX)
                result=1;
        }
        printLane();
        return result;
    }
    ~Race() {
        delete[] list;
    }
};

int main() {
    Race race;
    while(race.start()==0)
        system("pause");
}
