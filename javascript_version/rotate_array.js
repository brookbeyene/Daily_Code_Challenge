const rotateNums = (nums, start, end) => {
    while(start < end) {
        [nums[start], nums[end]] = [nums[end], nums[start]];
        start ++;
        end--;
    }
}
var rotate = function(nums, k) {

    k = k % nums.length;
    nums.reverse();
    rotateNums(nums, 0, k - 1);
    rotateNums(nums, k, nums.length -1);
    

}
