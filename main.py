from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from jinja2 import Environment, PackageLoader, select_autoescape

hernia=[
    {
        'head': 'The “Minimal-Repair Technique” is a revolutionary surgical procedure in the treatment for hernia. '
                'Initially intended for correcting inguinal hernia.',
        'name': 'Stacy Mc Neeley',
        'position': 'CEP’s Director',
        'avatar': 'img/author-pic.png'
    },
    {
        'head': 'The “Minimal-Repair Technique” is a revolutionary surgical procedure in the treatment for hernia. '
                'Initially intended for correcting inguinal hernia.',
        'name': 'Stacy Mc Neeley',
        'position': 'CEP’s Director',
        'avatar': 'img/author-pic.png'
    },
    {
        'head': 'The “Minimal-Repair Technique” is a revolutionary surgical procedure in the treatment for hernia. '
                'Initially intended for correcting inguinal hernia.',
        'name': 'Stacy Mc Neeley',
        'position': 'CEP’s Director',
        'avatar': 'img/author-pic.png'
    }
]

blog=[
    {
        'categories': 'Gym & Croosfit',
        'text': 'Many people sign up for affiliate programs'
    },
    {
        'categories': 'Gym & Croosfit',
        'text': 'Follow Our Classes Gyming on Instagram # BodyBuilding # photo'
    },
    {
        'categories': 'Gym & Croosfit',
        'text': 'Many people sign up for affiliate programs'
    },
    {
        'categories': 'Gym & Croosfit',
        'text': 'Many people sign up for affiliate programs'
    },
    {
        'categories': 'Gym & Croosfit',
        'text': 'Your Antibiotic One Day To 10 Day Options'
    },
    {
        'categories': 'Gym & Croosfit',
        'text': 'Many people sign up for affiliate programs'
    },
    {
        'categories': 'Gym & Croosfit',
        'text': 'Many people sign up for affiliate programs'
    },
    {
        'categories': 'Gym & Croosfit',
        'text': 'Your Antibiotic One Day To 10 Day Options'
    },
    {
        'categories': 'Gym & Croosfit',
        'text': 'Follow Our Classes Gyming on Instagram # BodyBuilding # photo'
    },
]

single = [
    {
       'data': 'January 31, 2019'
    },
    {
       'data': 'January 31, 2019'
    },
    {
       'data': 'January 31, 2019'
    },
    {
       'data': 'January 31, 2019'
    },
    {
        'data': 'Jan 31, 2019',
        'text2': 'Easy Home Remedy For Moisture Control Of Skin'
    },
]


food_kinds = [
    {
        'icon': 'lunch',
        'name': 'Dinner',
    },
    {
        'icon': 'food',
        'name': 'Breakfast',
    },
    {
        'icon': 'kitchen',
        'name': 'Lunch',
    }
]


class CustomHandler(SimpleHTTPRequestHandler):
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    def do_GET(self):
        if self.path.startswith('/media/'):
            super().do_GET()
        elif self.path == '/':
            self.render_index()
        elif self.path == '/about-us.html/':
            self.render_about()
        elif self.path == '/blog.html/':
            self.render_blog()
        elif self.path == '/blog-single.html/':
            self.render_blog()

    def render_index(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('index.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_about(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('about-us.html').render(hernia=hernia)
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_blog(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('blog.html').render(blog=blog)
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_blog_single(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('blog-single.html').render(single=single)
        print(body)
        self.wfile.write(body.encode('utf-8'))


def discover_models():
    pass


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=CustomHandler)
