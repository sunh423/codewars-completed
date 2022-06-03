// https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/javascript
function filter_list(l) {
    return l.filter(x => Number.isInteger(x)); 
    /*Uses the filter method to return a new arr of values that return true in the given function. 
    Using arrow notation function, positive integers will return true with Number method isInteger() and be kept in the return array*/
  }