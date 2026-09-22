type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    let a = await promise1
    let b = await promise2
    return a + b
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */