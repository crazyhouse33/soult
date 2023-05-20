# soult

Ce document n'est PAS produit par un professionel et n'a pas vocation à être utilisé pour imposer des conditions ou à se substituer à un juge en cas de procés. Je publie simplement ici les solutions que je propose au problème rencontré lors de la liquidation de biens entre deux personnes suite a un divorce sous le regime de séparation de biens. Il y'a un vide juridique alors que qu'il n'est pas si dur de répartir un bien équitablement. Pourtant le notaire et les parties concernés arrivent à des propositions mathématiquement injustes et relevent souvent plus du marchandage de tapis que de calculs réels, et si vous cherchez sur internnet un calcul qui fait référence, vous trouverez des simulateurs payant ou des formules extrement incomplètes sur des sites de notaires/avocats cherchant a vous faire acheter leurs services. C'est pourquoi j'expose ici ce que j'ai expliqué à mon amie dans le but d'établir une proposition juste sur le partage d'un bien. Le mieux avant d'arriver à l'accord à l'amiable suite a une séparation est de mettre dés l'accord de vente les conditions de liquidations https://paris.notaires.fr/fr/actualites/achat-et-revente-dun-bien-en-indivision-quotes-parts-dacquisition-et-repartition-du-prix-de-vente

Soulevez une issue qui explique votre point de vue si le calcul est faux ou lèse d'une manière ou d'une autre un parti ou si vous avez une question. Faites une PR si vous voulez généraliser la formule/apporter plus d'informations.

Un script python dans le repo permet de simuler vos part dans un partage à deux avec un pret partagé.

## Partage des biens propres

Voici comment se partager équitablement un ensemble de biens entre un investisseur A et J. 

### Quote part
La première étape consiste à mesurer la quote part de chaque participant. Elle traduit le fait que chaque participant détient un pourcentage X des biens au moment de la séparation. Pour établir cette valeur de manière juste, il faut qu’elle soit proportionnel au dépenses investies à ce jour.  La part de j est donc:
```
Dj / (Dj + Da) avec
Dj= Dépenses de J avant signature
Da= Dépenses de A avant signature
```

On incluera dans les dépenses, tout ce qui est indivisible. Par exemple, dans le cas ou A veut garder le bien, si J a payé la télé, il peut simplement récupéré la télé. Par contre si J ou A a payé la terrasse, il pourra difficilement récupéré sa terrasse, c'est donc une dépense indivible et lié au bien qu'il faudra donc intégrer dans le calcul de la quotepart. Pareillement, si A et J ont acheté un canapé à 80% 20 %, on ne va pas se partager des tranches de canapés coupés, on l'integrera plutot au calcul de la quote part.

### Valeur à partager
Le prêt n’est pas fini ce qui veut dire que la banque détient encore un pourcentage de la valeur de l’appartement. La véritable valeur que les investisseurs se partagent à la séparation est la valeur estimé du bien moins la valeur du prêt qu’il reste à payer (V-P). 

### Calcul des parts
```
Pj = (V-P) x Dj / (Dj+Da) 
Pa= (V-P) x Da / (Dj+Da) 
```

Ce calcul ce lit comme ceci : 

J a payé X% des dépenses de l’appartement à ce jour. Il est donc propriétaire de X% des parts de l’appartement que le couple possède aujourd’hui (en ignorant la part restante qui est à la banque). Si A veut se retrouver propriétaire de la part de l’appartement que le couple possède aujourd’hui, il doit lui payer la part Pj. 


Remarques:

On a totalement écarté le pret dans l'étape précédante. De fait, si une vente total a lieu, les parts calculés correspondent à la somme que l'un et l'autre gagneraient en plus du remboursement du pret. Si un des investisseur garde le bien, il devra payer la part de l'autre, puis voir avec la banque pour récupérer l'autre partie du pret. Cette passation de pret peut engendrer des frais si la banque le décide. Il faudra voir avec eux pour chiffrer l'operation.

## Partage des gains

Il est courant que chaque investisseur profite d'avantage en nature ou de somme d'argent direct lors de l'investissement. Dans un couple par exemple trés souvent les deux participants vont jouir ensemble du lieu de vie et donc chacun économiser un loyer. Si on s'arrette à l'etape précedente pour un couple de 10 ans et qu'on imagine que l'un des époux a strictement rien dépensé, il ne touchera certe pas d'argent de la vente du bien en elle même, mais il aura vécus 10 ans sans payer de loyé, au frais de son autre époux, qui était de fait 100% propriétaire du bien au regard des sommes dépensés. C'est pourquoi il est injuste de ne pas quantifier et partager proportionnellement aux quote-parts des dépenses les gains récupérés par les deux partis

On ajoutera donc la somme suivante au calcul des parts précédants:
```
Pgj = (Qj x Gt ) – Gj
```

Ceci ce lisant:
Etant propriétaire de l’appartement à Qj % à ce jour, J doit toucher Qj% des gains générés par l'appartement à ce jour en plus de sa part de l’appartement en lui-même. Il doit préalablement rendre la partie qu’il a déjà touché pour redistribuer cet argent.

Les calculs deviennent donc:
```
Pj = Ancien Pj + Pgj 
Pj =  Qj x (V+Gt-P) - Gj
Pa=   Qa x (V+Gt-P) - Ga 
```

## Erreurs communes

Croire que le notaire va vous aider à aboutir à un calcul juste. Selon mon expérience, le notaire n'a soit pas la compréhension des calculs de partage, soit il a la flegme d'arbitrer un calcul juste entre les partis et va simplement essayer de signer le plus vite possible, quitte à ne pas expliquer a l'un ou à l'autre pourquoi le calcul est biaisé.

Prendre Qj tel qu'il serait à la fin du pret et non pas le veritable Qj au moment de la séparation. Cela va particulierement léser un participant si il y'a apport de pret.

Erreur de parenthèse, redistribution du pret plutot que soustraction direct avant application des quotes parts

Erreurs de valeurs (toujours vérifier avec vos comptes toutes les valeurs individuels du calcul). Vérifier qu'elles soient bien toutes datées du moment de la séparation.

Prendre V pour la valeur d'achat et non pas l'estimation actuelle.

Prendre P pour le pret déja payé au lieu du P restant.

Ne pas pas redistribuer le gain

## Generalisation


Pour plusieurs bien, on sommera chaque sous part.

Pour n investisseur, la part de l'investisseur j Pj sur le bien de valeur estimée V vaut:

```math
\frac{D_j}{\sum_{i=0}^n D_i} * (V + \sum_{i=0}^n G_i + \sum_{i=0}^n P_i) - G_j
```

