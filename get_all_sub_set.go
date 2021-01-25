package main

import (
	"fmt"
)

func getSubSet(newIdx, oldIdx, n int, list, one []int, result [][]int) {
	if newIdx == n-1 {
		newList := make([]int, n)
		copy(newList, one)
		result = append(result, newList)
		return
	}
	for idx:=newIdx; idx<len(list); idx++ {
		fmt.Println(idx, newIdx, oldIdx)
		fmt.Println(one)
		fmt.Println(list)
		one[idx] = list[oldIdx]
		getSubSet(newIdx+1, oldIdx+1,n, list, one, result)
	}
	return
}

// 参考python的解法，遍历所有的数量的组合
func combine(list []int) [][]int {
	result := make([][]int, 0, 0)
	// for n:=1; n<len(list); n++ {
	// 	one := make([]int, n)
	// 	getSubSet(0, 0, n, list, one, result)
	// }
	one := make([]int, 2, 2)
	getSubSet(0, 0, 2, list, one, result)
	return result
}

func main() {
	fmt.Println(combine([]int{1,2,3,4,5}))
}
