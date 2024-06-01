/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if (typeof obj == "Array") {
        return obj.length == 0;
    } else if (typeof obj == "object") {
        return obj == null || Object.keys(obj).length == 0
    }
    return false;
};