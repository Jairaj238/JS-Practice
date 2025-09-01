let n = parseInt(prompt("Enter the value:"));
let i, j;

for (i = n; i >= 1; i--) {
  for (j = n; j >= n - i + 1; j--) {
    document.write(j);
  }
  document.write("<br>");
}
