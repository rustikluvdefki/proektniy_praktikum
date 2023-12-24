import os


def embed_svg_in_html(svg_file, html_file):
    with open(svg_file, 'r') as svg_file:
        svg_code = svg_file.read()

    with open(html_file, 'w') as html_file:
        html_content = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>SVG to HTML</title>
        </head>
        <body>
            <h1>SVG to HTML</h1>
            <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                {svg_code}
            </svg>
        </body>
        </html> 
        '''
        html_file.write(html_content)


if __name__ == "__main__":
    svg_file_path = "example.svg"
    html_file_path = "example.html"

    if not os.path.exists(svg_file_path):
        print(f"Error: SVG file '{svg_file_path}' not found!")
    else:
        embed_svg_in_html(svg_file_path, html_file_path)
        print(f"Conversion complete. HTML file: {html_file_path}")
