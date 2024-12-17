/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let count = 0;
    return function(...args){
        if (count < 1) {
            count += 1;
            return fn(...args);
        }
        return;
    }
};