import os
import argparse
from reschearch import load_csv, search_product, generate_summary, sort_data, export_data, equality_check


def main():
    """
    PRE: Les fonctions load_csv, equality_check, search_product, generate_summary, sort_data, export_data et interactive_mode sont implémenter correctement.
         Les librairie os et argparse sont bien importées.
    POST:utilise la bibliothèque argparse pour gérer les lignes de commandes, traite les données pour les montrées à l'utilisateur via des print
         Si aucun argument n'est passé, le mode interactif est activé par la fonction interactive_mode
    """
    parser = argparse.ArgumentParser(description="Gestionnaire d'inventaire via ligne de commande.")
    parser.add_argument("--load", help="Chemin du dossier contenant les fichiers CSV à charger.")
    parser.add_argument("--search", help="Rechercher un produit par son nom.")
    parser.add_argument("--summary", action="store_true", help="Générer un résumé par catégorie.")
    parser.add_argument("--sort", type=int, choices=[0, 1, 2], help="Trier les données : 0 pour nom, 1 pour quantité, 2 pour prix.")
    parser.add_argument("--reverse", action="store_true", help="Trier dans l'ordre décroissant.")
    parser.add_argument("--export", help="Chemin du fichier où exporter les données consolidées.")
    parser.add_argument("--display", action="store_true", help="Afficher toutes les données chargées.")

    args = parser.parse_args()

    # Mode interactif si aucun argument n'est fourni
    if not any(vars(args).values()):  # Vérifie si aucun argument n'est passé
        interactive_mode()
        return

    inventory_data = []
    header = []

    if args.load:
        folder = args.load
        try:
            files = [f for f in os.listdir(folder) if f.endswith('.csv')]
            if not files:
                print(f"Aucun fichier CSV trouvé dans le dossier spécifié ({folder})")
            for file in files:
                file_path = os.path.join(folder, file)
                print(f"Traitement du fichier : {file_path}...")
                new_header, new_data = load_csv(file_path)

                if header and not equality_check(header, new_header):
                    print(f"Les en-têtes du fichier {file} ne correspondent pas à celles chargées précédemment. Fichier ignoré.")
                    continue

                if not header:
                    header = new_header
                inventory_data.extend(new_data)
            print("Tous les fichiers CSV ont été chargés avec succès.")
        except FileNotFoundError as e:
            print(f"Erreur : {e}")

    if args.search:
        product_name = args.search
        found_products = search_product(inventory_data, product_name)
        if found_products:
            print("Résultats de la recherche :")
            for product in found_products:
                print(product)
        else:
            print("Aucun produit correspondant trouvé.")

    if args.summary:
        summary = generate_summary(inventory_data)
        print("Résumé des stocks par catégorie :")
        for category, stats in summary.items():
            print(f"Catégorie : {category} | Quantité totale : {stats['total_quantity']} | Prix moyen : {stats['average_price']:.2f}")

    if args.sort is not None:
        column_choice = args.sort
        reverse = args.reverse

        if column_choice in [0, 1, 2]:
            sorted_data = sort_data(inventory_data, column_choice, reverse)
            print("Les données ont été triées avec succès.")
            inventory_data = sorted_data
        else:
            print("Choix invalide pour le tri.")

    if args.export:
        export_path = args.export
        export_data(export_path, inventory_data, header)
        print(f"Les données ont été exportées dans le fichier : {export_path}.")

    if args.display:
        if not inventory_data:
            print("L'inventaire est vide, aucune donnée à afficher.")
        else:
            print("\nEn-tête :", header)
            for row in inventory_data:
                print(row)

def interactive_mode():
    """
    PRE: Les fonctions load_csv, equality_check, search_product, generate_summary, sort_data, export_data et interactive_mode sont implémenter correctement.
         Les librairie os et argparse sont bien importées.
         Les fichiers CSV doivent contenir des données bien structurées. 
    POST:L'interaction utilisateur détermine les opérations exécutées : importation, tri, recherche, résumé, exportation ou affichage des données.
    """
    inventory_data = []
    header = []

    while True:
        print("\nBienvenue dans le gestionnaire d'inventaire")
        print("1. Importer un fichier CSV")
        print("2. Effectuer une recherche de produit")
        print("3. Créer un résumé des stocks par catégorie")
        print("4. Trier l'inventaire")
        print("5. Exporter les données vers un fichier CSV")
        print("6. Afficher toutes les données")
        print("7. Quitter le programme")

        choice = input("Veuillez choisir une option : ")

        if choice == "1":
            folder = input("Spécifiez le chemin du dossier contenant les fichiers CSV : ")
            try:
                files = [f for f in os.listdir(folder) if f.endswith('.csv')]
                if not files:
                    print(f"Aucun fichier CSV trouvé dans le dossier spécifié ({folder})")
                    continue
                for file in files:
                    file_path = os.path.join(folder, file)
                    print(f"Traitement du fichier : {file_path}...")
                    new_header, new_data = load_csv(file_path)

                    if header and not equality_check(header, new_header):
                        print(f"Les en-têtes du fichier {file} ne correspondent pas à celles chargées précédemment. Fichier ignoré.")
                        continue

                    if not header:
                        header = new_header
                    inventory_data.extend(new_data)
                print("Tous les fichiers CSV ont été chargés avec succès.")
            except FileNotFoundError as e:
                print(f"Erreur : {e}")

        elif choice == "2":
            product_name = input("Indiquez le nom du produit à rechercher : ")
            found_products = search_product(inventory_data, product_name)
            if found_products:
                print("Résultats de la recherche :")
                for product in found_products:
                    print(product)
            else:
                print("Aucun produit correspondant trouvé.")

        elif choice == "3":
            summary = generate_summary(inventory_data)
            print("Résumé des stocks par catégorie :")
            for category, stats in summary.items():
                print(f"Catégorie : {category} | Quantité totale : {stats['total_quantity']} | Prix moyen : {stats['average_price']:.2f}")

        elif choice == "4":
            print("1. Trier par nom de produit")
            print("2. Trier par quantité")
            print("3. Trier par prix unitaire")
            column_choice = input("Sélectionnez une colonne pour trier : ")
            reverse_choice = input("Souhaitez-vous un tri en ordre décroissant ? (o/n) : ")

            reverse = reverse_choice.lower() == "o"

            if column_choice == "1":
                sorted_data = sort_data(inventory_data, 0, reverse)
            elif column_choice == "2":
                sorted_data = sort_data(inventory_data, 1, reverse)
            elif column_choice == "3":
                sorted_data = sort_data(inventory_data, 2, reverse)
            else:
                print("Sélection invalide, veuillez réessayer.")
                continue

            print("Les données ont été triées avec succès.")
            inventory_data = sorted_data

        elif choice == "5":
            export_path = input("Spécifiez le nom du fichier de destination (exemple : export.csv) : ")
            export_data(export_path, inventory_data, header)
            print(f"Les données ont été exportées dans le fichier : {export_path}.")

        elif choice == "6":
            if not inventory_data:
                print("L'inventaire est vide, aucune donnée à afficher.")
            else:
                print("\nEn-tête :", header)
                for row in inventory_data:
                    print(row)

        elif choice == "7":
            print("Merci d'avoir utilisé le gestionnaire d'inventaire. Au revoir !")
            break

        else:
            print("Option invalide. Veuillez entrer un choix valide.")

if __name__ == "__main__":
    main()
