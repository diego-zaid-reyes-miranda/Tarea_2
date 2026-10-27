
class Solution {
public:
    bool isValid(string s) {
        stack<char> pila;
        for (char c : s) {
            if (c == '(' || c == '['|| c == '{') {
                pila.push(c);
            } else {
                if (pila.empty()) {
                    return false;
                }
                char tope = pila.top();
                if ((c == ')' && tope != '(') ||
                    (c == ']' && tope != '[') ||
                    (c == '}' && tope != '{')) {
                    return false;
                }
                pila.pop();
            }
        }
        return pila.empty();
    }  
};
            
            
    
