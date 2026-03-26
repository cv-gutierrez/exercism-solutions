package airportrobot
import "fmt"

// Write your code here.
// This exercise does not have tests for each individual task.
// Try to solve all the tasks first before running the tests.
type Greeter interface {
	LanguageName() string
	Greet(a string) string
}

// ///////////
type German string

func (g German) LanguageName() string {
	return "German"
}

func (g German) Greet(name string) string {
	return fmt.Sprintf("Hallo %s!", name)
}

// //////////////
type Italian struct{}

func (i Italian) LanguageName() string {
	return "Italian"
}
func (i Italian) Greet(name string) string {
	return fmt.Sprintf("Ciao %s!", name)
}

// ////////////
type Portuguese struct{}

func (p Portuguese) LanguageName() string {
	return "Portuguese"
}
func (p Portuguese) Greet(name string) string {
	return fmt.Sprintf("Olá %s!", name)
}

// /////////////
func SayHello(name string, greet Greeter) string {
	return fmt.Sprintf("I can speak %s: %s", greet.LanguageName(), greet.Greet(name))
}