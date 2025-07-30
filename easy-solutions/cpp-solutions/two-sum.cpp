#include <unordered_map>
#include <vector>


//iterate through the nums array, compare the target to the value at the index. That is the complement. If the complement exists in the has map, add that set of I's to the output. 
//otherwise, add the index number to the has map. 
class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (m.find(complement) != m.end()) {
                return {m[complement], i};
            }
            m[nums[i]] = i;
        }
        return {}; 
    }
};
