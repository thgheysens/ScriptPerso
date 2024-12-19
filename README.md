# **Gestionnaire d'inventaire CSV**
## **Description**
- Présentation rapide du programme et de son objectif principal : automatiser la gestion des inventaires à partir de fichiers CSV.

---

## **Fonctionnalités**
### **1. Chargement des fichiers**
- Chargement de plusieurs fichiers CSV depuis un dossier.
- Vérification de la compatibilité des en-têtes.

### **2. Recherche**
- Recherche rapide d’un produit par son nom.

### **3. Résumé des stocks**
- Génération d’un résumé par catégorie.
- Calcul de la quantité totale et du prix moyen par catégorie.

### **4. Tri des données**
- Tri des produits par nom, quantité ou prix.
- Possibilité de spécifier l’ordre (croissant ou décroissant).

### **5. Exportation des données**
- Sauvegarde des données consolidées dans un nouveau fichier CSV.

### **6. Affichage des données**
- Présentation claire des données consolidées dans la console.

### **7. Exit**
- Sortir du programme

---

## **Installation**
### **Prérequis**
- Python 3.7 ou une version ultérieure.
- Les bibliothèques Python suivantes :
  - `argparse`
  - `os`
  - `csv`

### **Étapes d'installation**
1. Clonez le dépôt Git :  
   ```bash
   git clone <lien_du_dépôt>
   ```
2. Accédez au dossier du projet :  
   ```bash
   cd <nom_du_projet>
   ```
3. Installez les dépendances (si nécessaire) :  
   ```bash
   pip install -r requirements.txt
   ```

---

## **Utilisation**
### **Mode ligne de commande**
- Exécutez le programme avec des options :  
  ```bash
  python main.py --load chemin/du/dossier --summary --export chemin/export.csv
  ```
- Options disponibles :
  - `--load` : Charger des fichiers CSV d’un dossier.
  - `--search` : Rechercher un produit par son nom.
  - `--summary` : Générer un résumé des stocks.
  - `--sort` : Trier par colonne (`0` pour nom, `1` pour quantité, `2` pour prix).
  - `--reverse` : Trier dans l’ordre décroissant.
  - `--export` : Exporter les données dans un fichier.
  - `--display` : Afficher toutes les données dans la console.

### **Mode interactif**
- Exécutez le programme sans argument pour accéder à un menu interactif :
  ```bash
  python main.py
  ```

---

## **Rapport sur l'utilisation des outils d'IA**
### **Outils utilisés**
- **ChatGPT** :
  - Génération de code pour les fonctionnalités principales.
  - Optimisation du code pour suivre les bonnes pratiques.
  - Révision et structuration des fonctionnalités SMART.

### **Expérience**
- **Ce qui a bien fonctionné** :
  - ChatGPT a permis de gagner du temps en générant du code initial et en fournissant des solutions précises pour résoudre des bugs.
  - Très utile pour l'implémentation du argparse étant donné que je n'avais jamais utilisé cette librairie.
- **Défis rencontrés** :
  - ChatGPT a parfois suggéré des fonctionnalités pas utile ou avec des lignes de code que je ne maitrisais pas. 

---

## **Structure du projet**
- **`main.py`** : Interface principale avec gestion des arguments CLI et mode interactif.
- **`reschearch.py`** : Contient les fonctions utilitaires (chargement, tri, recherche, etc.).
- **`README.md`** : Documentation principale du projet.
- **``data`** : Dossier avec les fichiers csv.

---

## **Démonstration**
- Lien vers une vidéo de démonstration (par exemple, via YouTube ou une plateforme de partage vidéo) :
  - https://www.youtube.com/watch?v=aVtm5x3TZgw

---

