// https://www.codewars.com/kata/5bb904724c47249b10000131/train/javascript
function points(games) {
  let ret_score = 0;
  for (result of games){
    let [x, y] = result.split(":");    //deconstruct array by putting variables in [a,b,rest] format
    if (x > y){ret_score += 3};
    if (x == y){ret_score += 1};
  };
  return ret_score;
}