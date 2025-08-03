#include <stack>
#include <string>
class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> string_stack;

        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                string_stack.push(c);
            } 
            else {
                if (string_stack.empty()) return false;
                char top = string_stack.top();
                string_stack.pop();

                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return string_stack.empty();
    }
};
