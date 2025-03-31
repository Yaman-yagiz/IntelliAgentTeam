"""
Çeşitli yardımcı işlevler içeren modül.
"""
from pathlib import Path
from typing import Dict, List


def extract_project_name(project_description: str) -> str:
    """
    Proje açıklamasından proje adını çıkarır.
    
    Args:
        project_description: Proje açıklaması
        
    Returns:
        Proje adı
    """
    # İlk satırda "Proje: " veya "Proje Adı: " ile başlayan bir metin var mı diye kontrol et
    lines = project_description.split("\n")
    for line in lines[:5]:  # İlk 5 satırda kontrol et
        if line.startswith("Proje:") or line.startswith("Proje Adı:"):
            return line.split(":", 1)[1].strip()
    
    # Bulunamazsa, ilk satırı proje adı olarak kullan
    if lines and lines[0].strip():
        return lines[0].strip()
    
    # Hiçbir şey bulunamazsa, varsayılan ad
    return "Yazılım Projesi"


def ensure_directory_exists(directory: Path) -> None:
    """
    Belirtilen dizinin var olduğundan emin olur, yoksa oluşturur.
    
    Args:
        directory: Oluşturulacak dizin
    """
    directory.mkdir(parents=True, exist_ok=True)


def get_markdown_sections(markdown_text: str) -> Dict[str, str]:
    """
    Markdown metni bölümlere ayırır.
    
    Args:
        markdown_text: Markdown formatında metin
        
    Returns:
        Başlıkları anahtar, içeriği değer olarak içeren sözlük
    """
    lines = markdown_text.split('\n')
    sections = {}
    current_section = None
    current_content = []
    
    for line in lines:
        if line.startswith('# '):
            # Yeni ana başlık - önceki bölümü kaydet
            if current_section:
                sections[current_section] = '\n'.join(current_content)
            current_section = line[2:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)
    
    # Son bölümü ekle
    if current_section:
        sections[current_section] = '\n'.join(current_content)
        
    return sections


def extract_bullet_points(text: str) -> List[str]:
    """
    Metinden madde işaretli liste öğelerini çıkarır.
    
    Args:
        text: Kaynak metin
        
    Returns:
        Madde işaretli liste öğelerinin listesi
    """
    bullet_points = []
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('- ') or line.startswith('* '):
            bullet_points.append(line[2:])
    
    return bullet_points 