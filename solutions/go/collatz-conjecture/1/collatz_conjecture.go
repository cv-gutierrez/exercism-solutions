package collatzconjecture

import (
	"errors"
)

func CollatzConjecture(n int) (int, error) {
	if n <= 0 {
		return 0, errors.New("Numero cero o negativo")
	}
	if n == 1 {
		return 0, nil
	}

	resto := n % 2

	if resto == 0 {
		steps, err := CollatzConjecture(n / 2)
		steps++
		return steps, err
	} else {
		steps, err := CollatzConjecture(n*3 + 1)
		steps++
		return steps, err
	}
}