let n = parseInt(prompt("Enter the value: "));
let i , j;


for (i = 1; i <= n; i++) {
    for (j = 1; j <= n; j++) {
        if (j === 1 || j === n || i === n || i === 1) {
            document.write("*");
        } else {
            document.write("-@-");
        }
    }
    document.write("<br>");
}