/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const seen = new Map();
    
    return function(...args) {
        const key = JSON.stringify(args)

        if (seen.has(key)) {
            return seen.get(key);
        }

        let result = fn(...args);
        seen.set(key, result);
        return result;
    }
}