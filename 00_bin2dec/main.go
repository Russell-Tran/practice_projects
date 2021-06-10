package main

import "fmt"

func main() {
	fmt.Print("Enter a binary number: ")
	var input string
	fmt.Scanln(&input)

	output := 0
	for i := 0; i < len(input); i++ {
		if input[i] == '0' {
			output = (output << 1) | 0
		} else if input[i] == '1' {
			output = (output << 1) | 1
		} else {
			fmt.Printf("Error: Character '%c'\n", input[i]);
			return
		}	
	}
	fmt.Printf("Your number in decimal form is %d\n", output)
}