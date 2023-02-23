use std::io;

// under 2 = free, under 10 = $15, under 65 = $29, 65 or over = $1
pub fn exercise() {
    let mut age = String::new();
    println!("Please enter your age:");
    io::stdin()
        .read_line(&mut age)
        .expect("Failed to read line");

    let age: u32 = age.trim().parse().expect("Skill issue type a number");

    if age < 2 {
        println!("Free");
    } else if age < 10 {
        println!("It will cost $15");
    } else if age < 65 {
        println!("It will cost $29")
    } else {
        println!("It will cost $1")
    }
}
