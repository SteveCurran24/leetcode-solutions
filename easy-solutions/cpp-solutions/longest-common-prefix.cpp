class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res;
        for (int i = 0; i < strs[0].length(); ++i) {
            char c = strs[0][i];
            for (int k = 1; k < strs.size(); ++k) {
                if (i == strs[k].length() || strs[k][i] != c) return res;
            }
            res += c;
        }
        return res;
    }
};
