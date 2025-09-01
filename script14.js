let i , j, n = parseInt(prompt("Enter the value: "));
let count = 1;

for (i = 1; i <= n; i++) {

  for (j = 1; j <= i; j++) 
  {
    document.write(count);
    count++;
  }
document.write("<br>");
}
