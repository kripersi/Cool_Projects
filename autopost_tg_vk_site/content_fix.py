def fix_text(text, hashtags):
    forbidden_sites = ['instagram', 'facebook', 'twitter', 'tiktok', 'tik-tok', 'youtube']  # запрещенные соц сети

    note_sites = []
    for word in text.split():
        # проверяем есть ли в тексте эти соц сети
        if word.lower() in forbidden_sites or word.lower().replace(',', ' ') in forbidden_sites:
            text = text.replace(word, word+'*')
            note_sites.append(word)

    note = f'\nДеятельность {", ".join(set(note_sites))} запрещена на территории России' if note_sites else ''

    content = f'\n{text}{note}\n\n\n{hashtags}'
    return content

