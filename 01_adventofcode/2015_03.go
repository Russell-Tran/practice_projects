/*
For https://adventofcode.com/2015/day/3
*/
package main

import (
	"fmt"
	"io/ioutil"
)

type coord struct {
	x int
	y int
}

func main() {
	input, err := ioutil.ReadFile("2015_03.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	currCoord := coord{0, 0}
	s := map[coord]bool{currCoord: true}
	for i := 0; i < len(input); i++ {
		direction := input[i]

		if direction == '>' {
			currCoord.x++
		} else if direction == '^' {
			currCoord.y++
		} else if direction == '<' {
			currCoord.x--
		} else if direction == 'v' {
			currCoord.y--
		} else {
			fmt.Printf("Error: Character '%c'\n", direction);
			return
		}

		s[currCoord] = true
	}
	fmt.Printf("Part 1 answer: %d\n", len(s))
	// fmt.Printf("Part 2 answer: %d\n", basement_idx)
}
