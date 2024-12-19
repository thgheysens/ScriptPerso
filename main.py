import os
from reschearch import load_csv, search_product, generate_summary, sort_data, export_data, equality_check

def main():
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
