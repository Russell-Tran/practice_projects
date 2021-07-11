/*
For https://adventofcode.com/2015/day/1
*/
package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	input, err := ioutil.ReadFile("2015_01.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	output := 0
	basement_idx := -1
	for i := 0; i < len(input); i++ {
		if input[i] == '(' {
			output++
		} else if input[i] == ')' {
			output--
		} else {
			fmt.Printf("Error: Character '%c'\n", input[i]);
			return
		}
		if basement_idx == -1 && output == -1 {
			basement_idx = i + 1 // positions are 1-indexed
		}
	}
	fmt.Printf("Part 1 answer: %d\n", output)
	fmt.Printf("Part 2 answer: %d\n", basement_idx)
}