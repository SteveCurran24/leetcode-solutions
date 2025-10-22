#include <iostream>
class Solution {
public:
    bool isPalindrome(int x) {
        int reverse=x%10;
        int original = x;
        if(x>0){
            while(x/10>0 ){
                //std::cout << "x " << x << std::endl;
                //std::cout << "reverse " << reverse << std::endl;
                x=x/10;
                reverse=reverse*10 + x%10;
            }
        }
        if(original==reverse){
            return true;
        }
        return false;
    }
};