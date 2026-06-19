print ("=======O Gerador de Crachás Corporativos==============")

#Peça o primeiro nome do funcionário

primeiro_nome = input("qual o seu primeiro nome?")

#Peça o sobrenome do funcionário.

sobrenome = input("qual o seu sobrenome?")

#Peça o ano de nascimento dele (número inteiro).

ano_de_nascimento = int(input("qual seu ano de nascimento?"))

#Peça o cargo dele na empresa (ex: Dev Junior).

cargo_na_empresa = input("qual o seu cargo na empresa?")

print ("====================DADOS==============================")

#Junte o nome e o sobrenome para criar o Nome Completo.

nome_completo = primeiro_nome + " " + sobrenome

#Use o ano atual (2026) menos o ano de nascimento para calcular a idade aproximada do funcionário.
                        
idade_aproximada = 2026 - ano_de_nascimento

#Crie um E-mail Corporativo automático usando o formato: nome.sobrenome@rlcorp.com

email_corporativo = primeiro_nome+ "." + sobrenome + "@rlcorp.com"

print (f"nome:{nome_completo}")
print (f"idade: {idade_aproximada} anos")
print (f"email: {email_corporativo}")

print ("=================Seja Bem Vindo========================")
 