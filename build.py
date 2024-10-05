import os
import markdown
from pathlib import Path

# Paths
md_dir = Path('./md')
wiki_dir = Path('./wiki')
template_file = 'template.html'
index_file = Path('./index.html')

# Function to generate the <div class="Menu"> content
def generate_menu(md_dir, prepend=''):
    menu_html = '<div class="Menu">\n'
    for category in sorted(md_dir.iterdir()):
        if category.is_dir():
            menu_html += f'    <h2>{category.name.capitalize()}</h2>\n'
            menu_html += '    <ul>\n'
            for md_file in sorted(category.glob('*.md')):
                html_file = md_file.with_suffix('.html').name
                menu_html += f'        <li><a href="{prepend}{category.name}/{html_file}">{md_file.stem.replace("_", " ").title()}</a></li>\n'
            menu_html += '    </ul>\n'
    menu_html += '</div>\n'
    return menu_html

# Function to convert Markdown to HTML with boilerplate
def convert_md_to_html(md_file, wiki_dir, template):
    # Convert Markdown to HTML content with footnote support
    md = markdown.Markdown(extensions=['meta', 'tables', 'footnotes', 'nl2br'])
    body_html = md.convert(md_file.read_text())
    title = md.Meta.get('title', [md_file.stem.replace('_', ' ').title()])[0]

    # Insert the content into the template
    html_content = template.replace('$title$', title).replace('$body$', body_html)
    
    # Write the final HTML file to the wiki directory
    output_file = wiki_dir / md_file.with_suffix('.html').relative_to(md_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(html_content)

# Main function to build the wiki
def build_wiki():
    # Generate the menu HTML
    menu_html = generate_menu(md_dir, prepend='../')
    
    # Prepare the template for regular pages
    template = f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>$title$</title>
        <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)" />
        <meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)" />
        <link rel="stylesheet" type="text/css" href="../../styles.css" />
    </head>
    <body>
        <div class="container">
            {menu_html}
            <div class="Text">
                <h1>$title$</h1>
                $body$
            </div>
        </div>
    </body>
    <footer>
    <img src="../../PublicDomain.png"><span> No rights reserved</span>
    </footer>
</html>
"""
    # Write the template with dynamic menu to the template file
    with open(template_file, 'w') as f:
        f.write(template)
    
    # Convert Markdown files to HTML and save in the wiki directory
    for md_file in md_dir.rglob('*.md'):
        convert_md_to_html(md_file, wiki_dir, template)
    
    # Generate index.html with links prepended by "wiki/"
    index_menu_html = generate_menu(md_dir, prepend='wiki/')
    
    index_html = f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>Index</title>
        <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)" />
        <meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)" />
        <link rel="stylesheet" type="text/css" href="styles.css" />
    </head>
    <body>
        <div class="container">
            {index_menu_html}
            <div class="Text">
            </div>
        </div>
    </body>
    <footer>
    <img src="PublicDomain.png"><span> No rights reserved</span> <a href="https://webring.xxiivv.com/#your-id-here" target="_blank" rel="noopener">
  <img src="https://webring.xxiivv.com/icon.black.svg" alt="XXIIVV webring"/>
</a>
    </footer>
</html>
"""
    # Write the index.html file
    with open(index_file, 'w') as f:
        f.write(index_html)

if __name__ == '__main__':
    build_wiki()
