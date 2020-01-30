package main

import "fmt"

func main() {

	fmt.Print(bubble_sort([]int{6, 5, 4, 3, 2, 1, 7, 9, 8}))

}

/*
*  Time O (n²) ,  Space O (1)
 */
func bubble_sort(arr []int) []int {
	lenth := len(arr)
	bound, newbound := lenth-1, 0
	for i := 0; i < lenth; i++ {
		newbound = i
		for j := 0; j < bound; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				newbound = j
			}
		}
		bound = newbound
	}
	return arr
}
