package main

import "fmt"

func isValid(s string) bool {
	exp := make([]rune, 0, len(s)/2) // Preallocate with half the length of s
	match := map[rune]rune{
		'(': ')',
		'{': '}',
		'[': ']',
	}
	for _, char := range s {
		if v, ok := match[char]; ok {
			exp = append(exp, v)
		} else if len(exp) == 0 || exp[len(exp)-1] != char {
			return false
		} else {
			exp = exp[:len(exp)-1]
		}
	}
	return len(exp) == 0
}

func main() {
	fmt.Println(isValid("()"))
	fmt.Println(isValid("()[]{}"))
	fmt.Println(isValid("(]"))
	fmt.Println(isValid("([)]"))
	fmt.Println(isValid("{[]}"))
}
