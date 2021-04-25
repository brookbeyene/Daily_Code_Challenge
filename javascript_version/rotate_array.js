var rotate = function(nums, k) {
    const rotateArray = nums.concat();
    for (let i = 0; i < k; i++){
        const top_Array = rotateArray.shift();
        rotateArray.push(top_Array);

    }
    return rotateArray;
};

const k_Number = 3;
const sample_Array = [1,2,3,4,5,6,7]

const expected_Array = [5,6,7,1,2,3,4]

console.log(rotate(sample_Array, k_Number))