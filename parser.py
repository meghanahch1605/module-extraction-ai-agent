def extract_content(soup):
    content = []

    for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
        text = tag.get_text(strip=True)

        # Filter out very short or useless text
        if len(text) < 40:
            continue

        if "cookie" in text.lower():
            continue

        content.append((tag.name, text))

    return content

