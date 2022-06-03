// https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0/train/javascript
function last(x){

    let arr_words = x.split(" ");
    
    arr_words.sort((a,b) => { //Running arrow function for sorting function
      if (a.slice(-1) == b.slice(-1)){
        return 0 //Sorting function, return 0 if a and b order unchanged.
      }
      return a.slice(-1) > b.slice(-1) ? 1 : -1; ////Sorting function, return 1 if a before b, otherwise return -1 if b before a.
    });
    
    return arr_words
  }
  