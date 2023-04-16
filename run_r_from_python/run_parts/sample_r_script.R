# Define a function to calculate the factorial of a number
factorial <- function(n) {
  if (n == 0) {
    return(1)
  } else {
    return(n * factorial(n-1))
  }
}

# Define a function to calculate the Fibonacci sequence up to n
fibonacci <- function(n) {
  if (n == 1) {
    return(0)
  } else if (n == 2) {
    return(1)
  } else {
    return(fibonacci(n-1) + fibonacci(n-2))
  }
}

# Define a function to print "Hello, world!"
hello_world <- function() {
  print("Hello, world!")
}