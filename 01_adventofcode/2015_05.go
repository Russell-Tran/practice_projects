// TODO: debug
package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strings"
)

var vowels map[rune]struct{} = map[rune]struct{}{
    'a': struct{}{},
    'e': struct{}{},
    'i': struct{}{},
    'o': struct{}{},
    'u': struct{}{},
}

var badSubstrings []string = []string{"ab", "cd", "pq", "xy"}

func main() {
    file, err := os.Open("2015_05.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    fmt.Printf("Part 1 answer: %d\n", doPartOne(file))
    //fmt.Printf("Part 2 answer: %d\n", doPartTwo(file))
}

func doPartOne(file *os.File) int {
    scanner := bufio.NewScanner(file)
    count := 0
    for scanner.Scan() {
        text := scanner.Text()
        if containsAtLeastNVowels(text, 3) && containsAtLeastOneLetterNTimesInARow(text, 2) && noBadSubstrings(text) {
            count++
        }
        
    }
    return count
}

func containsAtLeastNVowels(s string, n uint) bool {
    count := uint(0)
    for _, char := range s {
        if _, ok := vowels[char]; ok {
            count++
        }
        if count >= n {
            return true
        }
    }
    return count >= n
}

func containsAtLeastOneLetterNTimesInARow(s string, n uint) bool {
    var prior rune
    count := uint(0)
    for i, char := range s {
        if i > 0 && char == prior {
            count++
        } else {
            count = 0
        }
        if count >= n {
            return true
        }
        prior = char
    }
    return count >= n
}

func noBadSubstrings(s string) bool {
    for _, bad := range badSubstrings {
        if strings.Contains(s, bad) {
            return false
        }
    }
    return true
}
