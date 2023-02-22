console.log('table.js loaded 2/x');

//export renderBoard function
export { renderBoard };

//import getRandomNumber function
import { getRandomNumber } from './script.js';

const renderBoard = function() {
  console.log('rendering board...');

  // render a 2x2 table
  // each cell contains 2x2 table named 'subtable'
  let table = document.createElement('table');
  table.className = 'table';

  for (let i = 0; i < 2; i++) {
    let row = document.createElement('tr');
    row.className = 'row';

    for (let j = 0; j < 2; j++) {
      let cell = document.createElement('td');
      cell.className = 'cell';
      let subtable = document.createElement('table');

      for (let k = 0; k < 2; k++) {
        let subrow = document.createElement('tr');
        subrow.className = 'subrow';

        for (let l = 0; l < 2; l++) {
          let subcell = document.createElement('td');
          //give a css class to each cell
          subcell.className = 'subcell';
          subcell.innerHTML = getRandomNumber();
          subrow.appendChild(subcell);
        }

        subtable.appendChild(subrow);
      }

      cell.appendChild(subtable);
      row.appendChild(cell);
    }

    table.appendChild(row);
  }

  document.body.appendChild(table);
}





