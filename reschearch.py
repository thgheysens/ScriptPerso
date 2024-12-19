import csv
import os

def load_csv(file_path):
    """
    Charge un fichier CSV et retourne son en-tête et les données sous forme de liste.
    PRE: file_path doit contenir un ou des fichier CSV
    POST: Lit le ou les fichier csv du dossier d'entré
        return: l'en-tête et les données de ces fichier
    RAISE: FileNotFoundError, si le chemin d'entrée n'existe pas
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier spécifié n'existe pas : {file_path}")

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader) 
        data = [row for row in reader]
    return header, data

def equality_check(header1, header2):
    """
    Vérifie que deux en-têtes de fichiers CSV sont identiques.
    PRE: header1 et header 2 doivent être des listes
    POST: compare header1 et header2 et retourne true si ils sont égaux  
    """
    return header1 == header2

def search_product(data, product_name):
    """
    Recherche un produit par son nom dans les données.
    PRE: data doit etre une liste non vide
        product_name doit être de type str
    POST: retourne un élément de data si il est égale à product_name
    """
    result = [row for row in data if row[0].strip().lower() == product_name.strip().lower()]
    return result

def generate_summary(data):
    """
    Génère un résumé par catégorie (quantité totale et prix moyen).
    PRE: data doit êttre une liste de liste de longueur 4(nom, quantité, prix, catégories)
    POST: ne modifie rien mais génère un dictionnaire qui regroupe les données de data.
    """
    summary = {}
    for row in data:
        try:
            category = row[3]  # Catégorie est dans la 4ème colonne
            quantity = float(row[1])  # Quantité est dans la 2ème colonne
            price = float(row[2])  # Prix unitaire est dans la 3ème colonne
        except (ValueError, IndexError) as e:
            print(f"Ligne ignorée en raison d'une erreur : {row} ({e})")
            continue

        if category not in summary:
            summary[category] = {'total_quantity': 0, 'total_price': 0.0, 'count': 0}

        summary[category]['total_quantity'] += quantity
        summary[category]['total_price'] += price * quantity
        summary[category]['count'] += 1

    for category, stats in summary.items():
        avg_price = stats['total_price'] / stats['total_quantity'] if stats['total_quantity'] > 0 else 0
        stats['average_price'] = avg_price

    return summary

def sort_data(data, column_index, reverse=False):
    """
    Trie les données selon une colonne donnée, avec option pour inverser l'ordre.
    PRE: Data est une liste de listes
    POST: NE modofie rien mais renvoie data trié en fonction de ce qui est demandé.
    """

    def safe_convert(value):
        try:
            return float(value)
        except ValueError:
            return float('inf')  

    try:
        sorted_data = sorted(data, key=lambda row: (safe_convert(row[column_index]), row[column_index]),
                             reverse=reverse)
        return sorted_data
    except Exception as e:
        raise ValueError(f"Impossible de trier les données : {e}")

def export_data(file_path, data, header):
    """
    Exporte les données vers un fichier CSV.
    PRE: file_path doit accessible ou inscriptible
         data est une liste de listes
         header est une liste contenant les titres des colonnes des listes de data
    POST: Crée ou réplace le fichier file_path

    """
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
