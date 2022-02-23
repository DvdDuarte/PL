# Comandos usados na aula
```Shell
$ cat musica/* > grande.txt
$ wc -l grande.txt
$ grep 'António Variações' grande.txt
$ grep 'title: Deolinda' grande.txt
$ grep 'title. Deolinda' grande.txt
$ grep -o 'title. Deolinda' grande.txt
$ grep 'singer.*Deolinda' grande.txt | wc -l
$ perl -pe 's!title: *(.*)!<h1>$1</h1>!' grande.txt > _2.html 
```
=== Acrescentar no ficheiro temporario criado _2.html
```Html
<html>
     <head>
          <meta charset="UTF-8"/>
     </head>
     .
     .
     .
</html>
```

=== Criar um ficheiro transforma com isto la dentro
```Shell
#! /usr/bin/perl -p
s!title: *(.*)!<h1>$1</h1>!;
s!(author|singer|lyrics): *(.*)!<hr><h2>$2</h2><small>$1</small>!;
s!^\n!<p>\n</p>!;
```

=== Comando a usar
```Shell
$ perl -pe 's!title: *(.*)!<h1>$1</h1>!' grande.txt > _2.html 
$ sed -rn '/title:/p; s!title:!!' grande.txt
$ sed -rn '/title:/p; s!author:!! s!;!\n!g p' grande.txt
```
