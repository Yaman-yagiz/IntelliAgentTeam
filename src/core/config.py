import os
import sys
from pathlib import Path

# Temel dizin yapılandırmaları
# src/core/config.py'nin bulunduğu dizin: src/core
# Proje kök dizini için iki seviye yukarı çıkmalıyız
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SRC_DIR = BASE_DIR / "src"
INSTRUCTION_DIR = SRC_DIR / "data" / "instructions"
OUTPUT_DIR = SRC_DIR / "data" / "output"

# Proje yapılandırmaları
PROJECT_DESCRIPTION_FILE = "project_description.txt"
PROJECT_DESC_PATH = SRC_DIR / "data" / PROJECT_DESCRIPTION_FILE

# Gemini yapılandırmaları
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def setup_environment():
    """
    Çalışma ortamını hazırlar, gerekli dizinleri oluşturur ve varlığını kontrol eder.
    """
    # Talimat dizinini kontrol et
    if not INSTRUCTION_DIR.exists():
        print(f"❌ Talimat dizini bulunamadı: {INSTRUCTION_DIR}")
        print("   Lütfen 'src/data/instructions' dizininin mevcut olduğundan emin olun.")
        sys.exit(1)
        
    # Talimat dosyalarını kontrol et
    essential_files = [
        "project_manager_instructions.txt",
        "ux_designer_instructions.txt", 
        "software_architect_instructions.txt",
        "team_leader_instructions.txt"
    ]
    
    missing_files = []
    for file in essential_files:
        if not (INSTRUCTION_DIR / file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Aşağıdaki gerekli talimat dosyaları bulunamadı:")
        for file in missing_files:
            print(f"   - {file}")
        print(f"\nLütfen bu dosyaların '{INSTRUCTION_DIR}' dizininde olduğundan emin olun.")
        sys.exit(1)
    
    # Proje açıklaması dosyasını kontrol et
    if not PROJECT_DESC_PATH.exists():
        print(f"❌ Proje açıklaması dosyası bulunamadı: {PROJECT_DESC_PATH}")
        print(f"   Lütfen bu dosyayı oluşturun ve proje detaylarını içine ekleyin.")
        sys.exit(1)
    
    # Çıktı dizinini oluştur
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("✅ Çalışma ortamı hazır!") 
