// TODO: part 2
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
        if containsAtLeastNVowels(text, 3) &&
            containsAtLeastOneLetterNTimesInARow(text, 2) &&
            noBadSubstrings(text) {
            count++
        }
        
    }
    return count
}

/* Part 1 helpers */

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
    count := uint(1)
    for i, char := range s {
        if i > 0 && char == prior {
            count++
        } else {
            count = 1
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

/* Part 2 helpers */ 

func ContainsPairOfLettersTwice(s string) bool {
    pairs := map[string]int{}
    for i := 0; i < len(s)-1; i++ {
        pair := s[i:i+1]
        if idx, ok := pairs[pair]; ok && idx != i-1 { // nonoverlapping
            return true
        } else if ok {
            continue
        } else {
            pairs[pair] = i
        }    
    }
    return false
}

func ContainsLetterTwice(s string) bool {
    letters map[rune]int{}
    for i := 0; i < len(s); i++ {
        letter := s[i]
        if idx, ok := letters[letter]; ok && idx != i-1 { // nonadjacent
            return true
        } else if ok {
            continue
        } else {
            letters[letter] = i
        }
    }
    return false
}
