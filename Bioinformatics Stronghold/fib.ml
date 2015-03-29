let n = 29
let k = 5

let rec fib_rabbits n =
  if n <= 2 then 1
  else
    fib_rabbits (n-1) + k*(fib_rabbits(n-2));;

print_endline (string_of_int (fib_rabbits n))
