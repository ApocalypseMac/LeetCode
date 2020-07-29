use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        for n in &nums {
            let count = map.entry(n).or_insert(0);
            *count += 1;
        }
        for j in 0..nums.len() {
            if let Some(count) = map.get(&(target - nums[j])) {
                if (*count > 1 && target - nums[j] == nums[j]) || target - nums[j] != nums[j] {
                    for k in j + 1..nums.len() {
                        if nums[k] == target - nums[j] {
                            return vec![j as i32, k as i32];
                        }
                    }
                }
            }
        }
        vec![0, 0]
    }
}
