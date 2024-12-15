import os
import yaml
from datetime import datetime
import subprocess

def read_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config

def get_modified_and_untracked_files():
    # Get modified files
    result_modified = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=M'], capture_output=True, text=True)
    modified_files = result_modified.stdout.splitlines()
    
    # Get untracked files
    result_untracked = subprocess.run(['git', 'ls-files', '--others', '--exclude-standard'], capture_output=True, text=True)
    untracked_files = result_untracked.stdout.splitlines()
    
    # Combine both lists and filter for Markdown files
    all_files = modified_files + untracked_files
    print(f"Modified and untracked files: {all_files}")  # Debug statement
    return [file for file in all_files if file.endswith('.md')]

def update_last_modified_date(file_path, date_str):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith('last_modified_date:'):
            lines[i] = f'last_modified_date: {date_str}\n'
            break
    else:
        # If last_modified_date is not found, add it after the permalink line
        for i, line in enumerate(lines):
            if line.startswith('permalink:'):
                lines.insert(i + 1, f'last_modified_date: {date_str}\n')
                break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    print(f"Updated {file_path} with last_modified_date: {date_str}")  # Debug statement

if __name__ == "__main__":
    config_path = 'E:/repos/MyProjects/GameDevelopment/_config.yml'
    config = read_config(config_path)
    date_format = config.get('last_edit_time_format', '%b %e %Y at %I:%M %p')
    specific_date = datetime.now().strftime(date_format)
    print(f"Using date format: {date_format}, specific date: {specific_date}")  # Debug statement
    
    modified_and_untracked_files = get_modified_and_untracked_files()
    for file_path in modified_and_untracked_files:
        update_last_modified_date(file_path, specific_date)
