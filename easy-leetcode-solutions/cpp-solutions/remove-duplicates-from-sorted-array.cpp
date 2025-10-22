#include <stdio.h>
#include <vector>

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        std::vector<int> out = {};
        for(int i = 0; i < nums.size(); i++){
            if((i+1 < nums.size()) && (nums[i] == nums[i+1])){
                continue;
            }
            std::cout << nums[i]<<endl;
            out.push_back(nums[i]);
        }
        nums = out;
        return out.size();
    }
};