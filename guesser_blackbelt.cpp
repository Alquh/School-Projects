#include <iostream>
#include <string>
#include <time.h>
#include <cstdlib>
using namespace std;

//number guessing program.
//Has a menu with 3 options 1. User guessing game 2.System Guessing game 3. Exit
//In option 1 , computer generates a random number
//user guesses a number
//computer responds with "high, low, or correct"
//continue until user has guessed the number
//In option 2 ,User inputs a number
//computer guesses that number
//User responds with "high, low, or correct"
//continue until system has guessed the number
//Output the number of turns taken by the system
//Option 3 is used to end the program
void user_guess(){
    srand(time(NULL));
    int correct = rand() % 100;
    int guess;
    bool keepgoing = true;
    int turn = 0;
    cout << "correct: " << correct << endl;
    while(keepgoing){
        turn++;
        cout << turn << ": please enter a number: ";
        cin >> guess;

        if (guess < correct){
            cout << "Too Low" << endl;
        } else if (guess > correct){
            cout << "Too High" << endl;
        } else {
            cout << "Correct!" << endl;
            keepgoing = false;
        } // end if
    } // end while
    cout << "It took " << turn << " turns." << endl;
} //end user_guess

void computer_guess(){
    int correct;
    cout<<"Input the correct number to be guessed:";
    cin>>correct;
    int guess = 50;
    int low = 1 , high = 100 ;
    string response;
    bool keepgoing = true;
    int turn = 0;
    while(keepgoing){
        turn++;
        cout << turn << ": The number is: "<<guess<<endl;
        cout<<"The guess is high/low/correct ? : ";
        cin >> response;

        if (response == "low"){
            low = guess+1;
            guess = (low+high)/2;
        } else if (response == "high"){
            high = guess-1;
            guess = (low+high)/2;
        } else if (response == "correct"){
            cout << "Number guessed successfully !!" << endl;
            keepgoing = false;
        } else {
            cout << "Invalid Response . Please enter a valid response." << endl;
            turn--;
        } // end if
    } // end while
    cout << "It took " << turn << " turns." << endl;
} // end system_guess

main(){
    int choice;
    bool keepgoing = true;
    while(keepgoing){
        cout<<"=============GAME MENU============="<<endl;
        cout<<"1. User Guessing game"<<endl;
        cout<<"2. Computer Guessing game"<<endl;
        cout<<"3. Exit"<<endl;
        cout<<"Enter your choice :";
        cin >> choice;

        if (choice == 1){
            user_guess();
        } else if (choice == 2){
            computer_guess();
        } else if (choice == 3){
            keepgoing = false;
        } else {
            cout << "Invalid Choice. Please choose a valid option" << endl;
        } // end if
    } // end while
} // end main



