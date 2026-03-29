# Homelab

Configurações do meu homelab.

### Variáveis de ambiente

As variáveis de ambiente necessárias para o arquivo `docker-compose.yml` estão no arquivo criptografado `.env.gpg`, para descriptogafá-lo basta executar:

```shell
gpg --output .env --decrypt .env.gpg
```