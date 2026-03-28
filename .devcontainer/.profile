# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

# Command prompt color
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

# Custom Prompt
NORMAL="\[\033[m\]"
YELLOW="\[\033[33;1m\]"
GREEN="\[\033[1;32m\]"
CYAN="\[\033[1;36m\]"
RED="\[\033[1;91m\]"

# Kubernetes
alias k="kubectl"
alias kctx="kubectx"
alias kns="kubens"
k8s () {
    K8S_CLUSTER=$(kubectx -c 2> /dev/null)
    if [ -n "${K8S_CLUSTER}" ]; then
        echo "[$(kubectx -c):$(kubens -c)]"
    fi
}

git_branch () {
    git branch 2> /dev/null | sed -e "/^[^*]/d" -e "s/* \(.*\)/[\1]/"
}
export PS1="${RED}\$(k8s)${CYAN}\u${NORMAL}@${GREEN}\h${NORMAL}:${YELLOW}\w${NORMAL} ${RED}\$(git_branch)${NORMAL}\$\n"

# Windows Git Bash
# export PS1="${RED} $(k8s)${CYAN}\u${NORMAL}@${GREEN}\h${NORMAL}:${YELLOW}\w${NORMAL}${RED}`__git_ps1`${NORMAL}\$\n"

set -o vi
alias sudo="sudo "
alias l="ls -al"

# Terraform
alias tfc="terraform console"
alias tfl="terraform state list"
alias tfs="terraform state show"
alias tfv="terraform validate"
alias tfo="terraform output"

# Go
export PATH=$PATH:/home/keli/go/bin

# Start Docker daemon automatically when logging in if not running.
RUNNING=`ps aux | grep dockerd | grep -v grep`
if [ -z "$RUNNING" ]; then
    sudo service docker start > /dev/null
fi