#include <string>
#include <iostream>
#include <cctype>

class Solution {
public:
    int romanToInt(string s) {
        int total=0;
        for(int i=0; i<s.length(); i++){
            switch(s[i]){
                case ('I'):
                    if(s[i+1] == 'V' || s[i+1] == 'X'){
                        total--;
                        break;
                    }else{
                        total++;
                        break;
                    }
                case ('V'):
                    total+=5;
                    break;
                case ('X'):
                    if(s[i+1] == 'L' || s[i+1]=='C'){
                        total-=10;
                        break;
                    }else{
                        total+=10;
                        break;
                    }
                case ('L'):
                    total+=50;
                    break;
                case ('C'):
                    if(s[i+1] == 'D' || s[i+1] == 'M'){
                        total-=100;
                        break;
                    }else{
                        total+=100;
                        break;
                    }
                case ('D'):
                    total+=500;
                    break;
                case ('M'):
                    total+=1000;
                    break;
            }
        }
        return total;
    }
}; 