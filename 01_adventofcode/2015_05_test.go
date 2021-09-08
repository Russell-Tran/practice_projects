package main

import "testing"

func TestContainsPairOfLettersTwice(t *testing.T) {
	input := "xyxy"
	if !ContainsPairOfLettersTwice(input) {
		t.Errorf(input)
	}
	input = "aabcdefgaa"
	if !ContainsPairOfLettersTwice(input) {
		t.Errorf(input)
	}
	input = "aaa"
	if ContainsPairOfLettersTwice(input) {
		t.Errorf(input)
	}
}