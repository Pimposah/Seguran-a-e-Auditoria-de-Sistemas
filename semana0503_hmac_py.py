# -*- coding: utf-8 -*-
"""semana0503_hmac.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vMR-PCZ6G7sHlVHkuKkcjb5lt4_e2MEY
"""

"""
Um Hmac é una construção que combina uma função hash com uma chave secreta
"""
import hmac
import hashlib

def hmac_auth(key, message):
  return hmac.new(key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

# Chamada
key = "Chave_secreta"
message = "mensagem_confidencial"
hmac_value = hmac_auth(key, message)

print(f"HMAC: ", hmac_value)

hmac_to_verify = hmac_value

def verify_hmac(key, massage, hmac_to_verify):
## Verifica se um HMAC corresponde a mensagem e a chave fornecida
  generated_hmac = hmac_auth(key, message)
  return hmac.compare_digest(generated_hmac, hmac_to_verify)

# Exemplo
key = "chave secreta"
message = "mensagem confidencial"
hmac_to_verify = hmac_auth(key, message)
is_valid = verify_hmac(key, message, hmac_to_verify)

print(f"O HMAC e valido? : " , is_valid)