console.log('script.js loaded 1/x');

// imports
import { renderBoard } from './table.js';
//import {generateArray} from './arrayGenerator.js';

//export getRandomNumber function
export { getRandomNumber };

//--------------------------------------------//
// Model

// give a random number between 1 and 4
const getRandomNumber = function() {
  return Math.floor(Math.random() * 4) + 1;
}

//--------------------------------------------//
// View

const render = function() {
  console.log('rendering...');
  renderBoard();
}

//--------------------------------------------//
// Controller

render();