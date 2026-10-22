# CLAUDE.md — Homelab

Repositório de configurações do servidor homelab pessoal de Henrique Sebastião.

## Regra essencial: commits

**Claude nunca deve fazer commits.** Após qualquer alteração, descreva o que foi feito no arquivo `commit-message.md` na raiz do repositório (crie-o se não existir) com a mensagem de commit sugerida. O proprietário faz o commit manualmente.

## Estrutura do repositório

```
homelab/
├── docker-compose.yml       # Arquivo principal — todos os serviços
├── .env                     # Variáveis de ambiente (descriptografado, não versionado)
├── .env.gpg                 # Arquivo .env criptografado com GPG (versionado)
├── ports.txt                # Mapa de portas → serviços
├── Makefile                 # Tarefas utilitárias
├── containers/              # Configurações persistidas de cada serviço
│   ├── glance/config/       # Configuração do dashboard Glance
│   ├── nginx/conf.d/        # Virtual hosts do Nginx
│   └── nginx/snippets/      # Snippets reutilizáveis do Nginx (TLS, proxy)
├── letsencrypt/             # Certificados TLS (Let's Encrypt)
├── scripts/                 # Scripts utilitários (encrypt-env.sh, etc.)
├── secrets/                 # Arquivos de segredo (cloudflare.ini)
└── dotfiles/                # Dotfiles do servidor gerenciados por dotdrop
```

## Convenções do docker-compose.yml

### Ordenação e documentação
- Serviços ordenados **alfabeticamente**
- Cada serviço deve ter um comentário com link para a documentação oficial imediatamente acima da sua definição

### Âncoras YAML (`x-*`)
Configurações compartilhadas são definidas como âncoras no topo do arquivo e reutilizadas com `<<:`:

| Âncora | Propósito |
|---|---|
| `*cloudflare-dns` | DNS via Cloudflare (1.1.1.1 / 1.0.0.1) — serviços com acesso externo |
| `*local-dns` | DNS via Pi-hole (172.16.0.2) — serviços internos |
| `*timezone-env` | `TZ: ${TIMEZONE}` |
| `*user-permissions` | `PUID: 1000 / PGID: 1000` |
| `*restart` | `restart: unless-stopped` |
| `*docker-socket` | Monta `/var/run/docker.sock` |

Cada serviço usa `<<: [*local-dns, *restart]` ou `<<: [*cloudflare-dns, *restart]` conforme o caso.

### Imagens
- Imagens sempre **pinadas com digest SHA256**: `image: repo/image:tag@sha256:...`
- Isso garante reprodutibilidade e evita surpresas com tags mutáveis

### Volumes
- Volumes nomeados (Docker) para dados que não precisam de acesso direto no host
- Bind mounts usando `${BASE}/nome-do-serviço/subdir:/caminho-no-container` para configs que ficam em `~/homelab/containers/`
- `${BASE}` aponta para o diretório `containers/` dentro do repositório

### Variáveis de ambiente
- Valores sensíveis sempre via `${VARIAVEL}` referenciando o `.env`
- O `.env` é **criptografado** com GPG e versionado como `.env.gpg`
- Para descriptografar: `gpg --output .env --decrypt .env.gpg`
- Para re-criptografar: `make env`

## Rede e exposição de serviços

- **Nginx** atua como reverse proxy SSL na frente de todos os serviços
- Certificados TLS: Let's Encrypt em `letsencrypt/`
- Domínio externo: `server.henriquesebastiao.com` com portas dedicadas por serviço
- **Cloudflare Tunnel** (`cloudflared`) para acesso externo seguro sem abrir portas no roteador
- Consulte `ports.txt` para o mapeamento completo porta → serviço

### Adicionando um novo serviço ao Nginx
Adicione um bloco `server { listen <porta> ssl; ... }` em `containers/nginx/conf.d/services.conf` e registre a porta em `ports.txt`.

## Serviços em execução

| Serviço | Porta | Descrição |
|---|---|---|
| Pi-hole | 8001 | DNS com bloqueio de anúncios |
| Immich | 8002 | Galeria de fotos self-hosted |
| Zabbix | 8003 | Monitoramento de infraestrutura |
| Grafana | 8004 | Dashboards e métricas |
| Dozzle | 8005 | Logs de containers em tempo real |
| Umami | 8006 | Analytics web |
| Glance | 8007 | Dashboard pessoal |
| Calibre Web | 8008 | Biblioteca de e-books |
| MeTube | 8009 | Download de vídeos (yt-dlp) |
| Filebrowser | 8010 | Gerenciador de arquivos web |
| Stirling PDF | 8011 | Ferramentas PDF |
| Duplicati | 8018 | Backups para Google Drive |
| Vaultwarden | 8019 | Gerenciador de senhas (Bitwarden) |
| Downtify | 8020 | Downloader de músicas (Spotify) |
| Speedtest Tracker | 8021 | Histórico de velocidade de internet |
| Uptime Kuma | 8026 | Monitoramento de uptime |
| FreshRSS | 8036 | Leitor de RSS |

## Makefile

```
make env            # Re-criptografa o .env → .env.gpg
make docker-prune   # Remove imagens/containers/volumes não usados
make update         # Atualiza dotfiles com dotdrop
make install        # Instala dotfiles no servidor com dotdrop
make compare        # Compara dotfiles locais vs servidor
make encrypt-import # Importa arquivo com transformação de criptografia
```

## Dotfiles

Dotfiles do servidor são gerenciados via **dotdrop** com o perfil `server`, configurado em `config.yaml`.
