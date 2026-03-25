package parsinglogfiles
import ("regexp"
        "fmt")

func IsValidLine(text string) bool {
	pattern := `^(\[TRC\]|\[DBG\]|\[INF\]|\[WRN\]|\[ERR\]|\[FTL\])`
	re, err := regexp.Compile(pattern)
	if err != nil {
		panic(err)
	}
	return re.MatchString(text)
}

func SplitLogLine(text string) []string {
	pattern := `\<[~|*|=|-]*\>`
	re, err := regexp.Compile(pattern)
	if err != nil {
		panic(err)
	}
	return re.Split(text, -1)
}

func CountQuotedPasswords(lines []string) int {
	pattern := `"[^"]*(?i)password[^"]*"`
	re, err := regexp.Compile(pattern)
	if err != nil {
		panic(err)
	}
	fmt.Println("re: ", re)
	count := 0
	for _, val := range lines {
		fmt.Println(val)
		if re.MatchString(val) {
			count++
		}
	}
	return count
}

func RemoveEndOfLineText(text string) string {
	pattern := `end-of-line\d*`
	re, err := regexp.Compile(pattern)
	if err != nil {
		panic(err)
	}
	return re.ReplaceAllString(text, "")
}
func TagWithUserName(lines []string) []string {
	pattern := `User\s+([a-zA-Z0-9]+)`
	re, err := regexp.Compile(pattern)
	if err != nil {
		panic(err)
	}
	result := make([]string, len(lines))
	for index, line := range lines {
		match := re.FindStringSubmatch(line)
		if len(match) > 0 {
			result[index] = fmt.Sprintf("[USR] %s %s", match[1], line)
		} else {
			result[index] = line
		}
	}
	return result
}