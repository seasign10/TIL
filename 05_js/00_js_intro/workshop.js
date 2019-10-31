function concat(str1, str2) {
  return `${str1} - ${str2}`
}

function checkLongStr(str) {
  if (str.length > 10) {
    return true
  } else {
    return false
  }
}

if (checkLongStr(concat('Haapy', 'Hacking'))) {
  console.log('LONG STRING') 
} else {
  console.log('SHORT STRING') 
}