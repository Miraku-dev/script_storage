def remove_similar_domains(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    unique_domains = set()
    filtered_lines = []

    for line in lines:
        url = line.strip()
        domain = url.split('//')[-1].split('/')[0]

        if domain not in unique_domains:
            filtered_lines.append(line)
            unique_domains.add(domain)

    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

    removed_count = len(lines) - len(filtered_lines)
    print(f"Из файла {file_path} удалено {removed_count} ссылок.")

file_path = 'site.txt' 
remove_similar_domains(file_path)
