# CSS Styles for Madeira Expedition Deck

def get_css():
    with open('/Users/luisechegorri/Documents/madeira/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract CSS from <style> to </style>
    start_tag = '<style>'
    end_tag = '</style>'
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)
    if start_idx != -1 and end_idx != -1:
        return content[start_idx:end_idx + len(end_tag)]
    raise ValueError("Could not find style block in original index.html")

if __name__ == '__main__':
    css = get_css()
    print(f"Extracted CSS: {len(css)} characters")
