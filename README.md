# LinkAI
LinkAI is an AI-powered professional networking platform built with Django, designed to help users enhance their job prospects. It features a resume parser that matches skills to job postings, provides career enhancement suggestions, and allows users to share posts, interact, and apply for jobs. The project is ongoing, with continuous improvements and new features being added.


Nous allons structurer le backlog en phases et sprints, en suivant la méthodologie Agile et les étapes CRISP-DM. Chaque sprint durera 2 à 3 semaines. Nous allons adapter l'exemple fourni pour qu'il soit plus clair et simple, en français courant, et en tenant compte des spécificités du projet (assistant local, 3 langues, confidentialité, etc.).

Voici le backlog détaillé :

### Phase 1 : Comprendre le domaine

**Objectif** : Définir clairement ce que l'assistant doit faire et pour qui.

#### Sprint 1 : Démarrer le projet et définir les objectifs (2 semaines)

- Tâche 1.1 : Rencontrer le client pour savoir exactement ce qu'il attend (à quoi servira l'assistant, dans quelles situations, etc.).

- Tâche 1.2 : Lister les fonctionnalités importantes (les 3 langues : arabe, anglais, français, surtout l'arabe ; comment il s'intégrera ; quelles tâches il fera).

- Tâche 1.3 : Écrire les objectifs clairs (ce qu'on fait maintenant, plus tard, etc.).

- Tâche 1.4 : Classer les fonctionnalités par ordre d'importance (ex: répondre aux questions courantes, comprendre le contexte, etc.).

### Phase 2 : Préparer les données

**Objectif** : Avoir les données nécessaires pour entraîner et tester l'assistant.

#### Sprint 2 : Trouver et préparer les données (2 semaines)

- Tâche 2.1 : Choisir un modèle open-source (LLaMA 2, Mistral, GPT-J) en comparant leur taille, leur performance, leur consommation mémoire, et leur compatibilité avec nos machines.

- Tâche 2.2 : Préparer les données pour l'entraînement (ex: questions-réponses en arabe, français, anglais ; dialogues ; documents du domaine).

- Tâche 2.3 : Vérifier que les données sont de bonne qualité et qu'elles couvrent bien les 3 langues.

### Phase 3 : Modéliser et développer le modèle

**Objectif** : Construire l'assistant et le rendre opérationnel localement.

#### Sprint 3 : Installer et configurer le modèle (3 semaines)

- Tâche 3.1 : Préparer l'environnement technique (installer Python, Docker, etc. sur une machine Linux avec GPU ou CPU).

- Tâche 3.2 : Installer le modèle choisi (avec Transformers, llama.cpp ou Ollama) et le faire tourner localement.

- Tâche 3.3 : Optimiser le modèle (quantisation, gestion de la mémoire) pour qu'il soit rapide et léger.

#### Sprint 4 : Créer l'API et gérer les conversations (2 semaines)

- Tâche 4.1 : Développer une API REST avec FastAPI pour que les applications puissent appeler l'assistant.

- Tâche 4.2 : Tester que l'API fonctionne bien (tests unitaires).

- Tâche 4.3 : Documenter comment utiliser l'API.

#### Sprint 5 : Gérer les prompts et le contexte (2 semaines)

- Tâche 5.1 : Intégrer SentenceTransformers pour que l'assistant comprenne le contexte de la conversation (historique, tâche en cours).

- Tâche 5.2 : Tester différents prompts pour avoir des réponses pertinentes.

- Tâche 5.3 : Mettre en place un système de logs pour enregistrer ce qui se passe (erreurs, temps de réponse, etc.).

### Phase 4 : Évaluer et tester

**Objectif** : Vérifier que l'assistant répond bien et respecte la confidentialité.

#### Sprint 6 : Tester les performances (2 semaines)

- Tâche 6.1 : Mesurer les performances (temps de réponse <2s, pertinence des réponses).

- Tâche 6.2 : Tester avec des cas réels (vérifier que l'assistant comprend bien les questions dans les 3 langues).

- Tâche 6.3 : Faire valider les réponses par des experts (vérifier la qualité).

#### Sprint 7 : Vérifier la sécurité et la confidentialité (1 semaine)

- Tâche 7.1 : Confirmer qu'aucune donnée ne sort de la machine locale (tout est 100% local).

- Tâche 7.2 : Vérifier que les données de conversation sont bien gardées en local.

### Phase 5 : Déployer

**Objectif** : Mettre l'assistant en production et le rendre utilisable.

#### Sprint 8 : Mettre en production (2 semaines)

- Tâche 8.1 : Déployer l'API et le modèle sur la machine de production (avec Docker).

- Tâche 8.2 : Intégrer l'assistant dans une application (web ou desktop).

- Tâche 8.3 : Tester que tout fonctionne bien en production.

#### Sprint 9 : Créer une interface de test (2 semaines)

- Tâche 9.1 : Développer une interface web simple pour tester l'assistant.

- Tâche 9.2 : Faire tester par des utilisateurs et recueillir leurs retours.

### Phase 6 : Suivre et optimiser

**Objectif** : Améliorer l'assistant en fonction de l'usage réel.

#### Sprint 10 : Surveiller et optimiser (en continu, 2 semaines par cycle)

- Tâche 10.1 : Surveiller les performances en temps réel (erreurs, temps de réponse, satisfaction).

- Tâche 10.2 : Améliorer le modèle et les prompts en fonction des retours.

- Tâche 10.3 : Ajouter des fonctionnalités si besoin (ex: fine-tuning supplémentaire, RAG pour intégrer une base de connaissances).

---

### Méthodologie Agile

- **Sprints de 2-3 semaines** : Chaque sprint se termine par un livrable testable.

- **Réunions quotidiennes** : Point rapide chaque jour pour suivre l'avancement.

- **Revue de sprint** : À la fin de chaque sprint, montrer ce qui a été fait et recueillir les feedbacks.

- **Rétrospective** : Réfléchir à ce qui a bien marché et ce qu'on peut améliorer pour le prochain sprint.

---

### User Stories (simplifiées et adaptées)

1. **En tant qu'utilisateur**, je veux poser des questions et avoir des réponses automatiques, pertinentes et dans ma langue (arabe, français, anglais).

- *Critères* : L'assistant répond en <2s, dans la bonne langue, et la réponse est utile.

2. **En tant qu'admin**, je veux configurer les prompts et mettre à jour le modèle facilement.

- *Critères* : Une interface admin permet de changer les prompts sans coder.

3. **En tant qu'utilisateur**, je veux que mes données restent 100% locales et sécurisées.

- *Critères* : Aucune donnée n'est envoyée sur internet ; l'interface montre que c'est sécurisé.

4. **En tant qu'admin**, je veux suivre les performances (temps de réponse, pertinence) et recevoir des alertes si ça dépasse les limites.

- *Critères* : Tableau de bord avec les KPI ; alertes si temps >2s ou pertinence <90%.

5. **En tant qu'utilisateur**, je veux une interface simple pour discuter avec l'assistant (web ou desktop).

- *Critères* : Interface intuitive, comme un chat.

6. **En tant qu'utilisateur**, je veux que l'assistant comprenne le contexte de ce que je fais (ex: si je suis dans un module RH, il adapte ses réponses).

- *Critères* : L'assistant utilise le contexte pour donner des réponses plus précises.

---

### KPIs (Indicateurs Clés)

- **Temps de réponse moyen** : < 2 secondes.

- **Pertinence des réponses** : > 90% de réponses jugées utiles.

- **Satisfaction utilisateur** : > 85% d'utilisateurs satisfaits.

- **Disponibilité** : 99.9% du temps.

- **Taux d'erreur** : < 5% de réponses inappropriées ou d'hallucinations.

---

### Livrables finaux

1. Code propre et commenté de l'assistant, de l'API et de l'interface.

2. Rapport technique expliquant les choix, les tests et comment améliorer.

3. Démonstration de l'assistant en action.

4. Documentation pour installer, utiliser et maintenir le système.

Ce backlog est conçu pour être simple, clair et aligné sur les objectifs du projet. On peut ajuster les tâches en cours de route selon les retours.
