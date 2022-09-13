# Simple implementation of modular multiplicative inverse

Modular arithmetic is a part of mathematics that allows us perform computations (+, -, /, *) without needs of float numbers. Multiplicative inverse is "a way" in which we can define division in modular arithmetics.<br><br>

## Operations in modular arithmetics:

__Addition:__  

Let's say we want to add number 6 and number 7, where modulus is number 9. We can do that like this: 

> e.g.  
>
> _6 + 7 (mod 9) = 4_

which is the same as `(6+7) % 9` (in most programming languages). Result is of course `4`.

<br>

__Subtraction:__  

We can perform subtraction with the same logic as addition:

> e.g.  
>
> _12 - 7 (mod 9) = 5_
>
>_6 - 7 (mod 9) = 8_

Now you may wonder how did we come up to number `8` in  `6 - 7 (mod 9)`.   
If we have negative number like 6 - 7 = -1, we can perform modulo operation like so:    

neg_numbe + (k*modulus) % modulus,

where `k` is positive inteeger such that: `[neg_number + (k*modulus)] > 0`
<br>

So in this case it would be ( `6 - 7  mod (9)` )  =>  ( `-1 + (1 * 9) mod (9)` ) => `8  (mod 9) = 8`,   
where k = 1 (which is smallest positive int, that satisfies condition `[neg_number + (k*modulus)] > 0`).

<br>

__Multiplication:__

Modular multiplication is pretty straigh-forward and we can express it like so:  

> e.g.  
>
> _4 * 3 (mod 9)_ => _12 (mod 9) = 3_

programatically we can express modular multiplication like this:  
`(4 * 3) % 9`

<br>

__Division:__

Modular division can be a little bit burden when it comes to learning so  
I'll do my best explaining it and hopefully it'll all make sense to you.  
  
<br>

Firstly we'll introduce a little bit of basic algebra.  
<br>
> `(a / b)`, is the same as `(a * b^-1)`

<br>
This is something that is well-known to us. Fortunatelly, the same rule applies  
in modular division so `9/4 (mod 9)` is the same as `[ 9 * (4^-1 (mod 9)) ] (mod 9)`.  
  

 Here you can spot our first problem, why do we express `4^-1` as `4^-1 (mod 9)` ?   

 You can think of `4^-1` as a kind of modular "operation", that's why we need to perform modulo 9. Now here is real problem,  how we can acctually calculate `4^-1 (mod 9)`?.  

 In general `a^-1 (mod n)` is known as modular multiplicative inverse and it can be calculated in many ways and the most popular way to calc modular multiplicative inverse is by using EEA ( [Extended Euclidean Algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) ).  

 In this repo you can find various implementation of modular multiplicative inverse written in Python but also in Rust. There are also couple of examples on how to calc modular multiplicative inverse on "paper".

 (Feel free to correct me if there is typo or smth else :). This repo will be updateed progressively. )

