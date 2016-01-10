Title: Le mirror GIT du pauvre (remotes multi URL)
Date: 2016-01-13 10:31
Author: Sebastien Badia
About_author: Engineer @RedHat.
Category: Asrall
Tags: git, mirror
Slug: git-multi-origin

Une petit astuce bien pratique! Non on ne va pas parler du `git add -p` :-)

Cette astuce là concerne le cas où vous avez deux repo GIT distant et que vous
souhaitez les tenir synchronisés (dans le cas où vous n'avez pas accès à ces
repos bare, et donc que le `git mirror` est compliqué).

On assume donc que nous avons un repo GIT local, avec un origin déjà
correctement configuré.

    :::bash
    ❯ git remote show origin -n
    * remote origin
      Fetch URL: git+ssh://github.com:22/sbadia/repo.git
      Push  URL: git+ssh://github.com:22/sbadia/repo.git

L'astuce consiste donc à ajouter une url à `origin`

    :::bash
    ❯ git remote set-url --add origin git+ssh://gogs@code.ffdn.org:55555/sbadia/repo.git

Dés lors, vous pouvez tout simplement pusher sur origin pour automatiquement
envoyer vers les deux repos GIT, ok c'est pas grand chose, mais ça m'a bien
rendu service dans mon cas :-)
