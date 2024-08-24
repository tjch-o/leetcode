/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    result = init;
    for (let i = 0; i < nums.length; i += 1) {
        result = fn(result, nums[i]);
    }
    return result;
};