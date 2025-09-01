let n = parseInt(prompt("Enter the value: "));
let i , j;

for (i = n; i >= 1; i--) {

    for (j = 1; j <= i; j++)
    {
        document.write(j);
    }
    document.write("<br>");
}