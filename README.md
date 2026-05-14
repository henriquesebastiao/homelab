# Homelab

Configurações do meu homelab.

### Variáveis de ambiente

As variáveis de ambiente necessárias para o arquivo `docker-compose.yml` estão no arquivo criptografado `.env.gpg`, para descriptogafá-lo basta executar:

```shell
gpg --output .env --decrypt .env.gpg
```

## Configurações iniciais do servidor

Instalando dependências para configurações iniciais do servidor:

```shell
sudo apt install fontconfig -y
sudo apt install git -y
```

Configurando meu shell

```shell
sudo apt install zsh -y
chsh -s /bin/zsh hick

# Instalação do Oh My Zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Instalando tema Spaceship Prompt
git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

# APÓS ISTO REINSTALE OS DOTFILES COM DOTDROP

# Instalando plugins do ZSH
git clone https://github.com/zsh-users/zsh-autosuggestions "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}"/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}"/plugins/zsh-syntax-highlighting

# Configurando fontes para o funcionamento correto do Spaceship Prompt
mkdir -p ~/.fonts
git clone https://github.com/pdf/ubuntu-mono-powerline-ttf.git ~/.fonts/ubuntu-mono-powerline-ttf
fc-cache -vf
```

Instalação do Atuin

```shell
sudo apt install atuin -y
atuin login
```