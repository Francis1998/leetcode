package main

import "fmt"

func dfs(nums []int, i int, sum1 int, sum2 int) bool {
	if sum1 == sum2 {
		return true
	}
	if sum2 > sum1 || i >= len(nums) {
		return false
	}
	return dfs(nums, i+1, sum1-nums[i], sum2+nums[i]) || dfs(nums, i+1, sum1, sum2)
}

func canPartition(nums []int) bool {
	sum := 0
	for _, n := range nums {
		sum += n
	}
	if sum%2 == 1 {
		return false
	}
	return dfs(nums, 0, sum, 0)
}
func main() {

	l1 := []int{1, 5, 11, 5}
	fmt.Println("123", canPartition(l1))
}
