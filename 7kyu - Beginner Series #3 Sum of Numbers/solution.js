// https://www.codewars.com/kata/55f2b110f61eb01779000053/train/javascript
function getSum( a,b ){
    [a, b] = a > b ? [b,a] : [a,b] // Sets B as the higher value of the two, and A as the lower value.
    
    
    if (a == b){ //If it's single value, we can immediately return it.
      return a;
    }
    
    let sum = 0; //Initializes a counter to sum up the range of values.
    for (let i = a; i <= b; i++){ //Starting from a, we add the value to the total sum then increment it until it equals b (including b).
      sum += i;
    };
    
    return sum; //Return the total sum
  }