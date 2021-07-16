package main

import (
	"fmt"
	"io/ioutil"
	"crypto/md5"
	"strconv"
)

const fiveZeroes = "00000"

func main() {
	input, err := ioutil.ReadFile("2015_04.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("Part 1 answer: %d\n", doPartOne(input))
	//fmt.Printf("Part 2 answer: %d\n", calculateDuoMode(input))
}

func doPartOne(input []byte) int {
	for i:= 1; i > 0; i++ {
		attempt := []byte(string(input) + strconv.Itoa(i))
		output := fmt.Sprintf("%x", md5.Sum(attempt))
		if output[:5] == fiveZeroes {
			return i
		}
	}
	return -1
}
