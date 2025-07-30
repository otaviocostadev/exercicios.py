# O mesmo amigo dos Exercícios Resolvidos está muito empolgado com a nova sala que está montando. Após comprar a
# TV, ele decidiu também adquirir um sofá. No entanto, como ele já pagou pela TV, ele não pode pagar o valor integral
# do sofá à vista. Ele pretende então pagar o sofá parcelado, incorrendo em juros de 1% ao mês (juros compostos
# com parcelas fixas). Novamente, ele pediu sua ajuda para saber quanto ficará a parcela de cada mês e o valor total
# do sofá incluindo os juros.
#
# Faça um programa em Python que receba do usuário o valor do sofá e a quantidade de parcelas e exiba na tela a
# parcela de cada mês e o valor total do sofá incluindo os juros. Obs: Para saber o valor de cada parcela,
# utilize a fórmula: valor_parcela = (valor_vista * 0.01 * (1.01 ** qtd_parcelas)) / ((1.01 ** qtd_parcelas) - 1)

valor_vista = float(input("Digite o preço do sofa à vista\n"))
qtd_parcelas = int(input("Digite a quantidade de parcelas\n"))
valor_parcela = (valor_vista * 0.01 * (1.01 ** qtd_parcelas)) / ((1.01 ** qtd_parcelas) - 1)
valor_prazo = valor_parcela * qtd_parcelas
print("O valor total do sofá é de R$ %.2f e o valor de cada parcela será R$ %.2f" % (valor_prazo, valor_parcela))