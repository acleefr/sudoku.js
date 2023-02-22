console.log('arrayGenerator.js loaded 3/x');

// Give me a random sudoku array 4x4
const generateArray = function() {
  let array;
  //add 4 number between 1 and 4 to the array
  const addNumber = function() {
    let number = Math.floor(Math.random() * 4) + 1;
    array.push(number);
  }
  
  addNumber();
  return array;
}

generateArray();
console.log(generateArray());