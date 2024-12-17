/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = [];
        let completed = 0;

        for (let i = 0; i < functions.length; i++) {
            let f = functions[i];
            f().then((res) => {
                results[i] = res;
                completed++;

                if (completed == functions.length) {
                    resolve(results);
                }
            }).catch((e) => {
                reject(e);
            })
        }
    })
};