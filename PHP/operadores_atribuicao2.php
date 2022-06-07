<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Operadores de Atribuicao</title>
</head>
<body>
    <?php
    //http://localhost:3000/operadores_atribuicao2.php?aa=2022
    $atual = $_GET["aa"];
    echo "o ano ano atual é $atual e o ano anterior é " . --$atual;
    echo "<br>o ano ano atual é $atual e o proximo ano é " . ++$atual;
    /* comentario gigante multilinha
    adad
    dad
    a
    da
    */
    ?>
<br>
</body>
</html>