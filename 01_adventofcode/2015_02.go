/*
For https://adventofcode.com/2015/day/2
*/
package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strings"
    "strconv"
)

func min(is ...int) int {
	min := is[0]
	for _, i := range is[1:] {
		if i < min {
			min = i
		}
	}
	return min
}

func main() {
    file, err := os.Open("2015_02.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    totalPaper := 0
    totalRibbon := 0
    for scanner.Scan() {
    	text := scanner.Text()
    	textSlice := strings.Split(text, "x")

    	l, err := strconv.Atoi(textSlice[0])
    	if err != nil {
        	log.Fatal(err)
    	}
    	w, err := strconv.Atoi(textSlice[1])
    	if err != nil {
        	log.Fatal(err)
    	}
    	h, err := strconv.Atoi(textSlice[2])
    	if err != nil {
        	log.Fatal(err)
    	}

        volume := l * w * h
        perimA, perimB, perimC := 2*l + 2*w, 2*l + 2*h, 2*w + 2*h 
    	areaA, areaB, areaC := l * w, l * h, w * h 
    	
        surfaceArea := 2 * areaA + 2 * areaB + 2 * areaC
    	extraPaper := min(areaA, areaB, areaC)
    	paper := surfaceArea + extraPaper

        ribbonWrap := min(perimA, perimB, perimC)
        bow := volume
        ribbon := ribbonWrap + bow

    	totalPaper += paper
        totalRibbon += ribbon
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    fmt.Printf("[Part 1] Total paper: %d\n", totalPaper)
    fmt.Printf("[Part 2] Total ribbon: %d\n", totalRibbon)
}