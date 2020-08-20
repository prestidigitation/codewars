// Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.
//
// Examples:
// foo -> foo1
// foobar23 -> foobar24
// foo0042 -> foo0043
// foo9 -> foo10
// foo099 -> foo100
//
// Attention: If the number has leading zeros the amount of digits should be considered.

const paddingHelper = (numStrLength) => {
  const padding = [...Array(numStrLength)].map(() => '0');
  return padding.join('');
};

const incrementString = (str) => {
  const numRegexResults = str.match(/\d+/g);
  if (numRegexResults === null) {
    return `${str}1`;
  }
  const numStr = numRegexResults[0];
  const num = Number(numStr);
  const incrementedNum = num + 1;
  const strRegexResults = str.match(/\D+/g);
  const slicedStr = strRegexResults === null ? '' : strRegexResults[0];
  const incrementedNumStr = incrementedNum.toString();
  const padding = paddingHelper(numStr.length);
  if (incrementedNumStr.length >= padding.length) {
    return slicedStr + incrementedNumStr;
  }
  const paddedNum = (`${paddingHelper(numStr.length)}${incrementedNumStr}`).slice(incrementedNumStr.length);
  return `${slicedStr}${paddedNum}`;
};
