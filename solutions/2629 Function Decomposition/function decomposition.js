/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        result = x
        for (let i = functions.length - 1; i >= 0; i -= 1) {
            fn = functions[i]
            x = fn(x)
        }
        return x
    }
};