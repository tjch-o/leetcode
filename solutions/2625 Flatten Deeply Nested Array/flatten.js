/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    return flatten(arr, 0, n);
};

const flatten = (arr, depth, n) => {
    let result = [];

    for (const elem of arr) {
        if (Array.isArray(elem) && depth < n) {
            result.push(...flatten(elem, depth + 1, n));
        } else {
            result.push(elem);
        }
    }
    return result;
}