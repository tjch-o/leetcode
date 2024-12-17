/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    if (nums.length === 0) {
        return init
    }

    let res = init
    for (const val of nums) {
        res = fn(res, val)
    }
    return res
};