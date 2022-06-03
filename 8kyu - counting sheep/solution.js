// https://www.codewars.com/kata/54edbc7200b811e956000556/train/javascript
function countSheeps(arrayOfSheep) {
    let count = 0;
    for (item of arrayOfSheep){
      if (item == true){
        count++;                   //increments the count counter everytime true is detected.
      };
    };
    return count;                  //returns total counter
  }