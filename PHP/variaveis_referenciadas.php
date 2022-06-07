<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Variaveis Referenciadas</title>
</head>
<body>
    <?php
    $a = 3;
    $b = &$a;
    $b += 5;
    echo "A variavel A vale $a";
    echo "<br>A variavel B vale $b";

    echo "<br>";//variaveis de variaveis 
    $a = "abc";
    $$a = "def";
    echo "<br>o conteudo da variavel A é $a";
    echo "<br>a variavel ABC criada recebeu o valor $abc";
    ?>
<br>
</body>
</html>