# cd ~/OneDrive/Área\ de\ Trabalho/CARREIRA\ PROGRAMAÇÃO/CursoPythonRPA
# git init
# esse comando cria um repositório local
# e o cd é para entrar na pasta, e o git init é para iniciar o repositório
# git add .

# Como verificar se você tem um repositório remoto?
# Tente rodar:
# git remote -v
# Se não aparecer nada, significa que não há um repositório remoto configurado.
# Se aparecer algo como:
# origin    https://github.com/seu-usuario/seu-repo.git (fetch)
# origin    https://github.com/seu-usuario/seu-repo.git (push)
# Então seu repositório está conectado a um remoto.

# 📌 O que acontece ao deletar a branch main?
# 🔹 Se você rodar este comando:
# git branch -D main
# 🛠️ Isso só deleta a main no seu computador (localmente).w
# 🔹 Se você quiser deletar no repositório remoto (GitHub/GitLab/etc.), então precisa rodar:
# git push origin --delete main
# 🛠️ Isso deleta a main também no servidor remoto.


# 🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥
# ### 🚀 **Fazendo o Merge da `main` na `master` antes de deletar**
# Antes de deletar a branch `main`, você pode juntar as mudanças dela na `master` para **não perder nenhum código importante**.
# ---
# ### 🖥️ **No Terminal (Git Bash, PowerShell ou VS Code)**
# 1️⃣ **Troque para a branch `master`**  
#    ```bash
#    git checkout master
#    ```
# 2️⃣ **Faça o merge da `main` na `master`**  
#    ```bash
#    git merge main --allow-unrelated-histories
#    ```
#    🔹 Se não houver conflitos, o Git concluirá o merge automaticamente.  
#    🔹 Se houver **conflitos**, o Git mostrará os arquivos afetados, e você precisará editar manualmente.  
# 3️⃣ **Se houver conflitos, resolva-os e depois faça um commit**  
#    ```bash
#    git add .
#    git commit -m "Resolvendo conflitos do merge"
#    ```
# 4️⃣ **Agora que tudo foi mesclado, delete a branch `main`**  
#    ```bash
#    git branch -D main
# ### 🖱️ **No GitKraken**
# 1️⃣ **Mude para a branch `master`** (clique nela e faça checkout).  
# 2️⃣ No topo, clique no botão **"Merge"**.  
# 3️⃣ Escolha a branch `main` e clique em **"Merge `main` into `master`"**.  
# 4️⃣ Se houver conflitos, GitKraken permitirá que você escolha quais mudanças manter.  
# 5️⃣ Após resolver, clique em **"Commit Merge"**.  
# 6️⃣ Agora, delete a `main`:  
#    - Clique com o botão direito sobre `main`.  
#    - Selecione **"Delete `main`"**.  
# ### **🎯 Conclusão**
# 🔹 Agora **tudo que estava na `main` está na `master`**.  
# 🔹 Você pode trabalhar apenas na `master` sem perder nada.  
# 🔹 Se precisar, posso te guiar na resolução de conflitos! 
# 🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥🚀🔥  