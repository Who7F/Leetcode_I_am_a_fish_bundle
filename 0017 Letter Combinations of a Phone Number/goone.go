type Letters struct{
    letter_map map[byte]string
}

func newLetters() *Letters {
    return &Letters {
        letter_map: map[byte]string {
            '2': "abc",  '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz",   
        },
    }
}

func (l *Letters) getCobinations(digits string, sol string, index int, res []string) []string {
    if index == len(digits) {
        return append(res, sol)
    } else {
        target := digits[index]
        letters := l.letter_map[target]
        for i := 0; i < len(letters); i++ {
            res = l.getCobinations(digits, sol + string(letters[i]), index + 1, res)
        }
        return res
    }
}

func letterCombinations(digits string) []string {
    if digits == "" {
        return []string{}
    }
    l := newLetters()
    return l.getCobinations(digits, "", 0, []string{})
}