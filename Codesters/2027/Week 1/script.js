function fahrenheitToCelsius(fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

console.log(fahrenheitToCelsius(98.6)); // 37


function sumOfEvens(numbers) {
    let sum = 0;
    for (let num of numbers) {
        if (num % 2 === 0) {
            sum += num;
        }
    }
    return sum;
}

console.log(sumOfEvens([1, 2, 3, 4, 5, 6])); // 12


const person = {
    name: "Sebastian",
    age: 28,
    country: "Estonia"
};

function describePerson(p) {
    console.log(`My name is ${p.name}, I am ${p.age} years old, and I live in ${p.country}.`);
}

describePerson(person);


function reverseString(str) {
    return str.split("").reverse().join("");
}

console.log(reverseString("hello")); // "olleh"


function findLargest(numbers) {
    return Math.max(...numbers);
}

console.log(findLargest([5, 10, 2, 8, 3])); // 10


function filterPositive(numbers) {
    return numbers.filter(num => num > 0);
}

console.log(filterPositive([-2, 5, -8, 0, 10])); // [5, 10]