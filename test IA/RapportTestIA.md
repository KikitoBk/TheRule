J'ai voulu tester différent modéle de langage open source, en cherchant un peu j'ai trouvé que le meilleur c'était falcon-40b (https://github.com/Decentralised-AI/falcon-40b), dessus ils disent que pour des taches moins complexe (comme nous) on peut utiliser son petit frère falcon-7b (https://huggingface.co/tiiuae/falcon-7b).

Je lance le programme pour falcon-7b, après plusieur bug j'ai fini pas passer sur python 3.10.11 et j'ai reussi à lancer le programme sauf que ... le modèle fait plus de 100go, j'ai pas de wifi et donc j'utilise ma 4g et ca serait trop a herberger.

J'en ai testé d'autre qui était trop lourd et j'ai fini pas télécharger bloom-1b7 (3go le modèle je crois) et ca retourner aucun résultat, pas d'erreur -> théorie : pc pas assez performant donc il give up.

J'ai fini par essayer bloom-560m (environ 1go) et c'est claqué, il sait écrire francais mais c'est tout mais il comprend pas ce qu'on lui écrit.


==> Conclusion : mon pc peut pas faire tourner des trucs python, donc a voir si on essayer llamacpp comme prévu de base

J'ai testé des trucs rigolo quand meme -> google colab
Ca permet de faire tourner des trucs plus puissant et c'est assez rapide



==> J'ai testé llama.cpp (sur python bizarre a dire mais c'était sur leur page github) et les derniers test ca avait rien donné