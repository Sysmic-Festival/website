# Site web Sysmic

Ce readme fait office de tutoriel complet pour développer et améliorer le site web de l'association Sysmic.

## Installations

### git
[Lien d'installation pour git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
### node.js et npm
[Lien d'installation pour node.js et npm](https://nodejs.org/en/download/package-manager)

Une fois installés, essayez la commande 
```sh
npm -v
```
pour vérifier que tout est en ordre (la version de npm devrait être affichée en réponse).
### vite
Enfin, installer vite à l'aide de la commande 
```sh
npm install -D vite
```

[Plus d'infos en cas de problème](https://vitejs.dev/guide/)

## Cloner le projet

Ouvrez un terminal, naviguez dans le dossier souhaité à l'aide de la commande **cd** pour le clonage du projet, par exemple 
```sh
cd C:\chemin\souhaité\pour\installation
```
Il est également possible d'aller dans le dossier via le gestionnaire de fichier et faire clic droit &rarr; ouvrir dans le terminal. \
Une fois fait, entrez 

```sh
git clone git@github.com:Sysmic-Festival/website.git
```

Git devrait créer une copie locale de ce repo.

[Plus d'infos en cas de problème](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Environnement de développement
Pour développer le site web, libre à vous d'utiliser l'IDE de votre choix. Il est néanmoins recommandé d'utiliser [Visual Studio Code](https://code.visualstudio.com).

### Simulation locale du site web
Ouvrez un terminal dans le projet et tapez
```sh
npm run dev
```
Vous devriez obtenir une réponse comme suit 
```sh
  VITE v3.2.10  ready in 857 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```
En suivant l'url donné, vous obtiendrez une simulation locale du site web. Quand vous faites une modification sur le code et que vous sauvegardez le fichier (ctrl+s), la simulation se met à jour instantanément.

Il est fortement recommandé d'utiliser cette fonctionnalité afin de se rendre compte de l'effet de nos modifications


### Compiler et minifier 
Pour convertir le projet en code web, utilisez la commande
```sh
npm run build
```
Une dossier **dist** devrait se créer, contenant le site web compilé.

## Bonnes pratiques 

### Branches git
Ne jamais travailler sur la branche principale du projet, toujours créer une branche avec 
```sh
git checkout -b "nom de la branche"
```
et faire une **pull request** afin qu'un autre collaborateur du projet puisse lire le code et l'approuver avant de la passer sur la branche principale.

L'utilisations de branches github et de pull requests n'étant pas un sujet facile, n'hésitez pas à vous renseigner et à demander de l'aide à un ancien I.T. Sysmic.

[Plus d'infos sur git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)

[Plus d'infos sur les pull requests](https://docs.github.com/fr/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

### Développement web 

#### Modularité
Quand vous concevez/modifiez un élément du site, pensez toujours au long terme et à son intégration dans le reste du site. 

Utilisez des classes css et  bannissez absolument les micro-changements sur un seul élément (exemple : style="transform...").

#### Inspecter l'élément
Dans un navigateur web, n'hésitez pas à faire clic droit &rarr; inspecter l'élément et à jouer avec le code source afin de regarder comment les différents éléments du site se comportent et agissent entre eux.


