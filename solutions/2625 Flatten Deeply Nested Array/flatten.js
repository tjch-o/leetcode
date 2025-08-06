/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (n == 0) {
        return arr.slice();
    }

    const res = [];

    for (let i = 0; i < arr.length; i += 1) {
        if (Array.isArray(arr[i]) && n > 0) {
            const flattened = flat(arr[i], n - 1);

            for (const elem of flattened) {
                res.push(elem);
            }
        } else {
            res.push(arr[i]);
        }
    }
    return res;
};