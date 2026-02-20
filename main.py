import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

save_folder = "./plots"
dataset_folder = "./datasets"

class NetflixPlot():
    df = pd.read_csv(f"{dataset_folder}/netflix_titles.csv")

    def movies_vs_tv(self):
        counts = self.df['type'].value_counts()

        plt.figure(figsize=(6,6))
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=['#1f77b4','#ff7f0e'])
        plt.title("Доля фильмов и сериалов на Netflix")
        plt.savefig(f"{save_folder}/movies_vs_tv.png", dpi=300, bbox_inches='tight')
        #plt.show()

    def top_10_countries(self):
        top_countries = self.df['country'].value_counts().head(10)

        plt.figure(figsize=(10,6))
        sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")

        for i, v in enumerate(top_countries.values):
            plt.text(v + 0.5, i, str(v), va='center')

        plt.xlabel("Количество шоу")
        plt.ylabel("Страна")
        plt.title("Топ-10 стран по количеству шоу на Netflix")
        plt.savefig(f"{save_folder}/top_10_countries.png", dpi=300, bbox_inches='tight')
        #plt.show()

    def shows_by_year(self):
        shows_count = self.df['release_year'].value_counts().sort_index()

        plt.figure(figsize=(12,6))
        sns.lineplot(x=shows_count.index, y=shows_count.values, marker='o')
        plt.xlabel("Год выпуска")
        plt.ylabel("Количество шоу")
        plt.title("Количество шоу на Netflix по годам")
        
        plt.savefig(f"{save_folder}/shows_by_year.png", dpi=300, bbox_inches='tight')

    def make_plots(self):
        self.movies_vs_tv()
        self.top_10_countries()
        self.shows_by_year()


class ImdbPlot():
    df = pd.read_csv(f"{dataset_folder}/imdb_top_1000.csv")

    def genre_distribution(self):
        # Берём только первый жанр из списка (если несколько через запятую)
        self.df['Primary_Genre'] = self.df['Genre'].str.split(',').str[0]
        
        # Считаем топ-10 жанров
        counts = self.df['Primary_Genre'].value_counts().head(10)

        # Горизонтальный barplot вместо круга для удобочитаемости
        plt.figure(figsize=(10,6))
        sns.barplot(x=counts.values, y=counts.index, palette="tab10")

        # Подписи с числами
        for i, v in enumerate(counts.values):
            plt.text(v + 0.1, i, str(v), va='center', fontsize=10)

        plt.xlabel("Количество фильмов")
        plt.ylabel("Жанр")
        plt.title("Топ-10 жанров в IMDb Top 1000", fontsize=14)
        
        # Сохраняем график
        plt.savefig(f"{save_folder}/imdb_genre_distribution.png", dpi=300, bbox_inches='tight')
        #plt.show()

    def top_10_directors(self):
        top_directors = self.df['Director'].value_counts().head(10)

        plt.figure(figsize=(10,6))
        sns.barplot(x=top_directors.values, y=top_directors.index, palette="magma")

        for i, v in enumerate(top_directors.values):
            plt.text(v + 0.1, i, str(v), va='center')

        plt.xlabel("Количество фильмов")
        plt.ylabel("Режиссёр")
        plt.title("Топ-10 режиссёров по количеству фильмов в IMDb Top 1000")
        plt.savefig(f"{save_folder}/imdb_top_10_directors.png", dpi=300, bbox_inches='tight')
        #plt.show()

    def movies_by_year(self):
        # Преобразуем в число, пропустим пустые
        self.df['Released_Year'] = pd.to_numeric(self.df['Released_Year'], errors='coerce')
        df_years = self.df.dropna(subset=['Released_Year'])

        movies_count = df_years['Released_Year'].value_counts().sort_index()

        plt.figure(figsize=(12,6))
        sns.lineplot(x=movies_count.index, y=movies_count.values, marker='o')
        plt.xlabel("Год выпуска")
        plt.ylabel("Количество фильмов")
        plt.title("Количество фильмов по годам в IMDb Top 1000")
        plt.savefig(f"{save_folder}/imdb_movies_by_year.png", dpi=300, bbox_inches='tight')
        #plt.show()

    def make_plots(self):
        self.genre_distribution()
        self.top_10_directors()
        self.movies_by_year()




nplot = NetflixPlot()
imdb_plot = ImdbPlot()

nplot.make_plots()
imdb_plot.make_plots()