class ArrayWrapper {
    nums : number[];
    constructor(nums: number[]) {
        this.nums = nums
    }
    
    valueOf(): number {
        let res = 0
        for(var x of this.nums){
            res += x
        }
        return res
    }
    
    toString(): string {
        let res = '['
        for(var x of this.nums){
            res += String(x) + ','
        }
        if(res[res.length - 1] == ','){
            res = res.slice(0,res.length - 1)
        }
        res += ']'
        return res
    }
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */