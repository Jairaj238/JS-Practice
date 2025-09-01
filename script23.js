let CharCode = 65;

for (let i = 1; CharCode <= 89; i++) {
  for (let j = 0; j < i && CharCode <= 90; j++) {
    document.write(String.fromCharCode(CharCode));
    CharCode++;
  }
  document.write("<br>");
}