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
	fmt.Printf("Part 1 answer: %d\n", calculateSingleMode(input))
	fmt.Printf("Part 2 answer: %d\n", calculateDuoMode(input))
}

func calculateSingleMode(input []byte) int {
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
			return -1
		}

		s[currCoord] = true
	}
	return len(s)
}

func calculateDuoMode(input []byte) int {
	santaCoord, roboCoord := coord{}, coord{}
	s := map[coord]bool{coord{}: true}
	for i := 0; i < len(input); i++ {
		var currCoord *coord
		if i % 2 == 0 {
			currCoord = &santaCoord
		} else {
			currCoord = &roboCoord
		}

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
			return -1
		}

		s[*currCoord] = true
	}
	return len(s)
}
