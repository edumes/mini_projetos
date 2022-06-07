<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Operadores de Atribuicao</title>
</head>
<body>
    <?php
    //http://localhost:3000/operadores_atribuicao.php?p=100
    $preco = $_GET["p"];
    echo "O preço do produto é R$ $preco";
    $preco += ($preco*10/100);
    echo "<br> e o preço com 10% de aumento ficara R$ $preco";

    $preco = $_GET["p"];
    echo "O preço do produto é R$ " . number_format($preco, 2); //formatar em valor monetário
    $preco -= ($preco*10/100);
    echo "<br> e o preço com 10% de desconto ficara R$ " . number_format($preco, 2);

    
    ?>
<br>
<img src="/atribuicao.PNG" alt="">
</body>
</html>