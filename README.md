# Instructions

## Como executar a aplicação

### Dependências
A aplicação é escrita em python, usando a versão 3.8 da linguagem. Para executar você vai precisar das seguintes ferramentas na sua máquina:
- python 3.8
- virtualenv 20.4.2
- make
- coverage 5.5
- pip 19.2.3


### Criando o ambiente virtual

**Todos o comando abaixo devem ser executados na raiz do projeto**

Na intenção de criar um ambiente virtual que lhe permita executar o projeto você deve executar os seguintes comandos.

```bash
virtualenv .venv && source .venv/bin/activate
```

### Instalando as dependências
```bash
pip install -r requirements.txt 
```

### Executando o arquivo de exemplo
```bash
python3 authorize.py < samplefile
```

### Como executar os testes
Os testes podem ser executados usando o comando `make`
```bash
make test
```

Ou usando diretamente o `coverage`
```
coverage run -m unittest tests/all.py && coverage report --fail-under=95 --show-missing --omit=".venv/*","*/test*","lib/business/authorizer.py"
```

Os testes estão configurados para falhar caso o coverage de código seja inferior à 95% 

## Como o projeto está organizados

### Modulos da aplicação
#### Separação em camadas
Escolhi uma arquitetura de separação em camadas para essa aplicação por julgar a mais adequada. Além de facilitar o **isolamento das responsabilidades**. 
Por consequência, facilita o *mocking* dos testes de unidade. As camadas foram nomeadas da seguinte maneira.

- **lib/controller**: Responsável por fazer o parse dos dados de input e repassa-los para a camada abaixo
- **lib/business**: Parte central da lógica de negócios, essa camada irá aplicar todas as regras envolvidas em criação de conta e transações
- **lib/repository**: Camada de controle do estado da aplicação, inputs validos da aplicação serão armazendos usando um *in-memory state*

#### Modulos auxiliares
- **lib/helpers**: Métodos de apoio geral (ex: conversão de data)
- **lib/constants**: Constantes utilizadas dentro do projeto, evitando bugs por erro de ortografia e permitindo refactoring rápido 

#### Modulos de tests
- **test/controller**: Utilizei os testes da camada de controller para fazer os testes de integração. 
- **test/business**: Os testes dentro desse modulo são os testes de unidade, normalmente mockam qualquer recurso externo a unidade, permitindo assim uma depuração mais específica.

[comment]: <> (- **test/repository**: Camada de controle do estado da aplicação, inputs validos da aplicação serão armazendos usando um *in-memory state*)

## Considerações
- Compreendi que para as violations `account-not-initialized` e `card-not-active` são impeditivas para o processamento das outras violations, ou seja, não faz sentido eu aplicar elas junto com uma violation `high-frequency-small-interval`, por exemplo.
- Em algumas partes do documento de especificação a violação de transação dupla é escrita como `doubled-transaction` e outras como `double-transaction`. Assumi a primeira como a correta.