package main

import "fmt"

func main() {
	fmt.Print("Enter a binary number: ")

	var input string
	fmt.Scanln(&input)

	fmt.Println("You input: " + input)
	for i:= len(input)-1; i >= 0; i-- {
		fmt.Println(input[i] == '0')
	}
}