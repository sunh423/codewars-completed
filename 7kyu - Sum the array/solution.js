// https://www.codewars.com/kata/56bdf9d50d0b6433df001074/train/javascript
Array.prototype.sum = function() { //If not already declared, we need to add .prototype after class before adding method name.
    let return_sum = 0;
    for (let i = 0; i < this.length; i++){
     let num = Number(this[i]); //to reference 'self', use 'this'
      if (!isNaN(num)) {     //Checks to see if the number is valid. If yes, then add to total return sum.
        return_sum += num;
      };
    };
    return this.length <= 0 ? 0 : return_sum; //ternary operator, returns 0 if array size is less or equal to 0, otherwise, return total sum.
  };