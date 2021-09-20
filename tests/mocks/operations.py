# Criando uma conta com sucesso
ACCOUNT_CREATION_INPUT = [{"account": {"active-card": False, "available-limit": 750}}]
ACCOUNT_CREATION_OUTPUT = [{"account": {"active-card": False, "available-limit": 750}, "violations": []}]

# Criando uma conta que viola a lógica do Autorizador
ACCOUNT_CREATION_FAIL_INPUT = [{"account": {"active-card": True, "available-limit": 175}},
                               {"account": {"active-card": True, "available-limit": 350}}]
ACCOUNT_CREATION_FAIL_OUTPUT = [{"account": {"active-card": True, "available-limit": 175}, "violations": []},
                                {"account": {"active-card": True, "available-limit": 175},
                                 "violations": ["account-already-initialized"]}]

# Processando uma transação com sucesso
TRANSACTION_CREATION_INPUT = [
    {"account": {"active-card": True, "available-limit": 100}},
    {"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:00.000Z"}},
]
TRANSACTION_CREATION_OUTPUT = [
    {"account": {"active-card": True, "available-limit": 100}, "violations": []},
    {"account": {"active-card": True, "available-limit": 80}, "violations": []}
]

# Processando uma transação que viola a lógica account-not-initialized
TRANSACTION_WITH_ACCOUNT_NOT_INITIALIZED_INPUT = [
    {"transaction": {"merchant": "Uber Eats", "amount": 25, "time": "2020-12-01T11:07:00.000Z"}},
    {"account": {"active-card": True, "available-limit": 225}},
    {"transaction": {"merchant": "Uber Eats", "amount": 25, "time": "2020-12-01T11:07:00.000Z"}}
]
TRANSACTION_WITH_ACCOUNT_NOT_INITIALIZED_OUTPUT = [
    {"account": {}, "violations": ["account-not-initialized"]},
    {"account": {"active-card": True, "available-limit": 225}, "violations": []},
    {"account": {"active-card": True, "available-limit": 200}, "violations": []}
]

# Processando uma transação que viola a lógica insufficient-limit
TRANSACTION_WITH_INSUFFICIENT_LIMIT_INPUT = [
    {"account": {"active-card": True, "available-limit": 1000}},
    {"transaction": {"merchant": "Vivara", "amount": 1250, "time": "2019-02-13T11:00:00.000Z"}},
    {"transaction": {"merchant": "Samsung", "amount": 2500, "time": "2019-02-13T11:00:01.000Z"}},
    {"transaction": {"merchant": "Nike", "amount": 800, "time": "2019-02-13T11:01:01.000Z"}},
]
TRANSACTION_WITH_INSUFFICIENT_LIMIT_OUTPUT = [
    {"account": {"active-card": True, "available-limit": 1000}, "violations": []},
    {"account": {"active-card": True, "available-limit": 1000}, "violations": ["insufficient-limit"]},
    {"account": {"active-card": True, "available-limit": 1000}, "violations": ["insufficient-limit"]},
    {"account": {"active-card": True, "available-limit": 200}, "violations": []}
]

# Processando uma transação que viola a lógica high-frequency-small-interval
TRANSACTION_WITH_HIGH_FREQUENCY_SMALL_INTERVAL_INPUT = [
    {"account": {"active-card": True, "available-limit": 100}},
    {"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:00.000Z"}},
    {"transaction": {"merchant": "Habbib's", "amount": 20, "time": "2019-02-13T11:00:01.000Z"}},
    {"transaction": {"merchant": "McDonald's", "amount": 20, "time": "2019-02-13T11:01:01.000Z"}},
    {"transaction": {"merchant": "Subway", "amount": 20, "time": "2019-02-13T11:01:31.000Z"}},
    {"transaction": {"merchant": "Burger King", "amount": 10, "time": "2019-02-13T12:00:00.000Z"}},
]
TRANSACTION_WITH_HIGH_FREQUENCY_SMALL_INTERVAL_OUTPUT = [
    {"account": {"active-card": True, "available-limit": 100}, "violations": []},
    {"account": {"active-card": True, "available-limit": 80}, "violations": []},
    {"account": {"active-card": True, "available-limit": 60}, "violations": []},
    {"account": {"active-card": True, "available-limit": 40}, "violations": []},
    {"account": {"active-card": True, "available-limit": 40}, "violations": ["high-frequency-small-interval"]},
    {"account": {"active-card": True, "available-limit": 30}, "violations": []},
]

# Processando uma transação que viola a lógica doubled-transaction
TRANSACTION_WITH_DOUBLED_TRANSACTION_INPUT = [
    {"account": {"active-card": True, "available-limit": 100}},
    {"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:00.000Z"}},
    {"transaction": {"merchant": "McDonald's", "amount": 10, "time": "2019-02-13T11:00:01.000Z"}},
    {"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:02.000Z"}},
    {"transaction": {"merchant": "Burger King", "amount": 15, "time": "2019-02-13T11:00:03.000Z"}},
]
TRANSACTION_WITH_DOUBLED_TRANSACTION_OUTPUT = [
    {"account": {"active-card": True, "available-limit": 100}, "violations": []},
    {"account": {"active-card": True, "available-limit": 80}, "violations": []},
    {"account": {"active-card": True, "available-limit": 70}, "violations": []},
    {"account": {"active-card": True, "available-limit": 70}, "violations": ["doubled-transaction"]},
    {"account": {"active-card": True, "available-limit": 55}, "violations": []},
]

# Processando transações que violam multiplas lógicas
TRANSACTION_WITH_MULTIPLE_VIOLATIONS_INPUT = [
    {"account": {"active-card": True, "available-limit": 100}},
    {"transaction": {"merchant": "McDonald's", "amount": 10, "time": "2019-02-13T11:00:01.000Z"}},
    {"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:02.000Z"}},
    {"transaction": {"merchant": "Burger King", "amount": 5, "time": "2019-02-13T11:00:07.000Z"}},
    {"transaction": {"merchant": "Burger King", "amount": 5, "time": "2019-02-13T11:00:08.000Z"}},
    {"transaction": {"merchant": "Burger King", "amount": 150, "time": "2019-02-13T11:00:18.000Z"}},
    {"transaction": {"merchant": "Burger King", "amount": 190, "time": "2019-02-13T11:00:22.000Z"}},
    {"transaction": {"merchant": "Burger King", "amount": 15, "time": "2019-02-13T12:00:27.000Z"}},
]
TRANSACTION_WITH_MULTIPLE_VIOLATIONS_OUTPUT = [
    {"account": {"active-card": True, "available-limit": 100}, "violations": []},
    {"account": {"active-card": True, "available-limit": 90}, "violations": []},
    {"account": {"active-card": True, "available-limit": 70}, "violations": []},
    {"account": {"active-card": True, "available-limit": 65}, "violations": []},
    {"account": {"active-card": True, "available-limit": 65}, "violations": ["high-frequency-small-interval", "doubled-transaction"]},
    {"account": {"active-card": True, "available-limit": 65}, "violations": ["insufficient-limit", "high-frequency-small-interval"]},
    {"account": {"active-card": True, "available-limit": 65}, "violations": ["insufficient-limit", "high-frequency-small-interval"]},
    {"account": {"active-card": True, "available-limit": 50}, "violations": []},
]


TRANSACTION_NOT_CONSIDERING_PREVIOUS_TRANSACTION_WITH_VIOLATIONS_INPUT = [
    {"account": {"active-card": True, "available-limit": 1000}},
    {"transaction": {"merchant": "Vivara", "amount": 1250, "time": "2019-02-13T11:00:00.000Z"}},
    {"transaction": {"merchant": "Samsung", "amount": 2500, "time": "2019-02-13T11:00:01.000Z"}},
    {"transaction": {"merchant": "Nike", "amount": 800, "time": "2019-02-13T11:01:01.000Z"}},
    {"transaction": {"merchant": "Uber", "amount": 80, "time": "2019-02-13T11:01:31.000Z"}},
]
TRANSACTION_NOT_CONSIDERING_PREVIOUS_TRANSACTION_WITH_VIOLATIONS_OUTPUT = [
    {"account": {"active-card": True, "available-limit": 1000}, "violations": []},
    {"account": {"active-card": True, "available-limit": 1000}, "violations": ["insufficient-limit"]},
    {"account": {"active-card": True, "available-limit": 1000}, "violations": ["insufficient-limit"]},
    {"account": {"active-card": True, "available-limit": 200}, "violations": []},
    {"account": {"active-card": True, "available-limit": 120}, "violations": []},
]
