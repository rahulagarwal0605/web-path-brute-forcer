# web-path-brute-forcer

**Sample Input:**

**Webapp url:** [https://www.github.com](https://www.github.com/)

**Webapp paths:** sample 5 lines out of 1000 of the input file **wordlist.txt**

●      admin

●      info

●      .git/config

●      .htaccess

●      backup.zip

**Success status codes:** [200, 302]

**Sample Output: A list of URLs that responded with any of the success status codes as provided in the input by the user.**

●      <https://www.github.com/info> [**Status code 302**]

●      <https://www.github.com/.htaccess> [**Status code 200**]
