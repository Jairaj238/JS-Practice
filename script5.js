let n = parseInt(prompt("Enter the value: "));
let i , j;


for (i = 1; i <= n; i++) {
    for (j = 1; j <= i; j++) {
        if (j === 1 || j === i || i === n) {
            document.write("*");
        } else {
            document.write("-");
        }
    }
    document.write("<br>");
}