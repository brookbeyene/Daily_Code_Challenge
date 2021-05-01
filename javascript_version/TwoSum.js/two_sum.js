





var twoSum = function(nums, target){
    const map = new Map();
    // look at speed in map is O(1)
    for(let i = 0; i < nums.length; i++){
        let currVal= nums[i];
        if(map.has(currVal)){ // we find the diff that adds up to target
            return [map.get(currVal), i];
        }
        let diff = target - currVal;
        map.set(diff, i);
    }
};

//Note
console.log(twoSum([1,2,8,6,3,9, 8],9))