let count = 65;

for(i = 65; i <= 69; i++) {

  for(j = 65; j <= i; j++)
	{
    document.write(String.fromCharCode(count));
    count++;
  }
  document.write("<br>")
}