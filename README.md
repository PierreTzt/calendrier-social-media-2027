# Calendrier social media 2027

Générateur de calendrier social media 2027 : 424 dates (journées mondiales, événements, dates décalées), un conseil et une idée de post par mois. On peut y ajouter ses propres dates et exporter le tout en PDF (A4 paysage).

- `index.html` : le générateur, autonome (aucune dépendance, aucun serveur). C'est ce qui est déployé sur Vercel.
- `src/build.py` : les données (dates, conseils, idées de post) et le rendu. Il régénère `index.html`.
- `src/app_template.html` : l'interface du générateur (formulaire, aperçu, impression) et le rendu des pages.
- `src/themes.css` : les styles Suisse, Cahier, Heatmap, Timbres et Écran (le style Riso vient de `build.py`).
- `src/themes-serie2.css` : les styles Ticket, Départs, Ardoise, Métro, BD et Game Boy.

## Styles

Douze styles au choix dans le formulaire : Riso, Suisse, Cahier, Heatmap, Timbres, Écran, Ticket, Départs, Ardoise, Métro, BD, Game Boy.
Un lien peut ouvrir directement un style : `?style=heatmap` (valeurs : `riso`, `suisse`, `cahier`, `heatmap`, `timbres`, `ecran`, `ticket`, `departs`, `ardoise`, `metro`, `bd`, `gameboy`).

## Modifier les dates de base

Éditer `src/build.py`, puis :

```bash
python src/build.py
```

Les dates ajoutées depuis l'interface restent dans le navigateur de chaque visiteur (localStorage) ; elles s'exportent et s'importent en `.json`.

## Exporter en PDF

Bouton « Télécharger le PDF », puis « Enregistrer au format PDF » et cocher « Graphiques d'arrière-plan ».
