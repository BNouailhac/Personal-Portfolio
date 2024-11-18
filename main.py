import toml
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

class Portfolio:
    def __init__(self):
        self.en_toml = "config/en.toml"
        self.fr_toml = "config/fr.toml"

    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read() 
        return content

    def write_file(self, file_path, content):
        with open(file_path, 'w', encoding= 'utf-8') as file:
            file.write(content)

    def load_toml_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            data = toml.loads(content)
        return data

    def format_date(self, date: str):
        date_object = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = date_object.strftime("%b %d, %Y")
        return formatted_date

    def en(self):
        return self.load_toml_file(self.en_toml)
    
    def fr(self):
        return self.load_toml_file(self.fr_toml)


if __name__ == "__main__":

    portfolio = Portfolio()
    en = portfolio.en()
    fr = portfolio.fr()

    env = Environment(loader=FileSystemLoader('jinja'))
    env.filters['format_date'] = portfolio.format_date

    template = env.get_template('index.jinja')

    html_render = template.render(
        en = portfolio.en(),
        fr = portfolio.fr()
    )

    portfolio.write_file("index.html", html_render)