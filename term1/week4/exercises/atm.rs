use std::io;

pub fn exercise() {
    let pin = 6942;
    let mut input = String::new();
    println!("Please enter the pin:");
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Skill issue type a number");

    if pin == input {
        println!("Welcome Back");
    } else {
        println!("Wrong code! Now you die")
    }
}
