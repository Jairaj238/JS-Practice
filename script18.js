let n = parseInt(prompt("Enter the value: "));
let i , j;

for (i = 1; i <= n; i++) {

  for (j = 1; j <= i; j++) 
  {
    document.write(2 * i - 1);
  }
document.write("<br>");
}