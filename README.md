# bhaskara-formula
Esse código resolve uma equação quadrática (do 2º grau) da forma 
𝑎𝑥² + 𝑏𝑥 + c = 0 usando a fórmula de Bhaskara. 

Primeiro, importa-se o módulo math para usar a função math.sqrt() (raiz quadrada).
As variáveis a, b e c armazenam os coeficientes da equação quadrática.
Calcula-se o delta (discriminante) com a fórmula: Δ = b² − 4ac.
O valor de delta determina o número de raízes reais.

Usa-se uma estrutura condicional:

Se delta < 0, a equação não possui raízes reais, pois não é possível extrair a raiz quadrada de um número negativo (em números reais).

Se delta == 0, existe apenas uma raiz real (raiz dupla). Ela é calculada com a fórmula: 𝑥 = −𝑏 / 2𝑎, como + e - resultam no mesmo valor, só é necessário calcular uma vez.

Se delta > 0, existem duas raízes reais distintas, calculadas com as fórmulas:
x1 = − b + √Δ / 2a, x2 − b - √Δ / 2a 

Por fim, as raízes (ou a mensagem correspondente) são exibidas no console com print().

👉 No caso dos valores definidos (a = 7, b = 5, c = 0), o delta é 
5² − 4 * 7 * 0 = 25, maior que zero. Assim, o programa imprime duas raízes reais.
x1 = 0.0 e x2 = -0.7142857142857143
