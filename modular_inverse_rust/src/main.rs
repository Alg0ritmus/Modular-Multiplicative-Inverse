// all code is defined in lib.rs
use modular_inverse_rust::modular_inverse_algo1;

fn main() {
    let test1: i64 = modular_inverse_algo1(6,26);
    let test2: i64 = modular_inverse_algo1(19,26);

    println!("Results:\ntest1: {}\ntest2: {}",test1,test2);

}
