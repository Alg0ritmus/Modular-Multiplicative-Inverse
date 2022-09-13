/*

Algorithm taken from:
https://www.researchgate.net/profile/Nikolay-Kyurkchiev/publication/344712990_New_Algorithms_for_Finding_Modular_Multiplicative_Inverse/links/5f8afd7ea6fdccfd7b65d11c/New-Algorithms-for-Finding-Modular-Multiplicative-Inverse.pdf

*/

pub fn modular_inverse_algo1(mut a: i64,mut b: i64)->i64{
    let mut x1 = 1;
    let mut x2 = 0;
    let b0 = b;

    while b>0{
        let q = a/b;
        let r = a%b;
        a = b;
        b=r;
        // value "t" is just temporary
        let t=x2;
        x2=x1-q*x2;
        x1=t;
    }

    if a ==1 {
        if x1<0{
            x1+=b0;
        }
        // eecami stands for extended euclidean algorithm for multiplicative inverse
        
        //eecami = x1; return eecami;
        x1
    }
    else{
        //eecami = 0; return eecami;
        0
    }
}


// simple tests

#[cfg(test)]
mod test{

    use super::*;
    #[test]
    fn test_correctness_eecami_1(){
        let test1: i64 = modular_inverse_algo1(6,26);
        assert_eq!(test1,0);
    }

    #[test]
    fn test_correctness_eecami_2(){
        let test1: i64 = modular_inverse_algo1(19,26);
        assert_eq!(test1,11);
    }
}

